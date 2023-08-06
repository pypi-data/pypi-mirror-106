import tarfile
import os
import errno
import shutil
from pathlib import Path
from aiofile import async_open
from azure.storage.blob.aio import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError, ResourceExistsError

class Decompressor():

    def __init__(self, conn_str):
        self.conn_str = conn_str

    async def process_blob_files(self, container_name, source_dir, dest_dir, local_temp_dir):
        self.init(local_temp_dir)

        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(self.conn_str)
        async with blob_service_client:
            container_client = blob_service_client.get_container_client(container_name)

            async for blob in container_client.list_blobs(name_starts_with=source_dir):
                if blob.name != "raw":
                    blob_client = container_client.get_blob_client(blob.name)
                    local_file = "{}/{}".format(local_temp_dir, os.path.basename(blob.name))
                    await self.process_blob_file(container_name, blob_client, dest_dir, local_file)

    async def process_blob_file(self, container_name, blob_client, dest_dir, local_file):
        await self.download_compressed_file(blob_client, local_file)
        
        decompression_dir = self.decompress(local_file)

        await self.upload_decompressed_files(container_name, dest_dir, decompression_dir)

    async def download_compressed_file(self, blob_client, local_file):
        async with async_open(local_file, 'wb') as afp:
            download_stream = await blob_client.download_blob()
            await afp.write(await download_stream.readall())

    def get_files_to_upload(self, decompression_dir):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(decompression_dir):
            for file in f:
                files.append(os.path.join(r, file))

        return files

    async def upload_decompressed_files(self, container_name, dest_dir, decompression_dir):
        files_to_upload = self.get_files_to_upload(decompression_dir)

        blob_service_client = BlobServiceClient.from_connection_string(self.conn_str)
        async with blob_service_client:
            for file in files_to_upload:
                await self.upload_decompressed_file(blob_service_client, file, container_name, dest_dir)   
    
    async def upload_decompressed_file(self, blob_service_client, file, container_name, dest_dir):
        blob_name = os.path.basename(file)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob="{}/{}".format(dest_dir, blob_name))

        async with async_open(file, "rb") as afp:
            await blob_client.upload_blob(await afp.read(), overwrite=True)   
            
    def decompress(self, downloaded_file):   
        decompression_dir = os.path.splitext(downloaded_file)[0]

        # decompress
        tar = tarfile.open(downloaded_file)
        tar.extractall(decompression_dir)
        tar.close()  

        return decompression_dir 

    # setup temporary directory for process
    def init(self, local_temp_dir):
        if os.path.exists(local_temp_dir):
            shutil.rmtree(local_temp_dir)
        
        try:
            os.makedirs(local_temp_dir)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise      