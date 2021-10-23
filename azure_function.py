# https://www.twilio.com/blog/media-file-storage-python-flask-amazon-s3-buckets
#https://stackabuse.com/file-management-with-aws-s3-python-and-flask/
from azure.storage.blob import BlobServiceClient, BlobClient
import uuid
import os

DOWNLOAD_FOLDER = os.getcwd() + '/buffer/download_buffer/'
connect_str = 'DefaultEndpointsProtocol=https;AccountName=storage1342;AccountKey=bDX43vnW8wqNNKupoeJUwKgCckiHTdbpoxzRSe3sxqzK+42twzED02UfSmMkrat2bM77/3hDTAULInchX5tQlQ==;EndpointSuffix=core.windows.net'

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
# Create a unique name for the container
container_name = '79ff98f4-25d0-4d89-95a1-cceb112d9add'#str(uuid.uuid4())
# Create the container
# container_client = blob_service_client.create_container(container_name)

def azure_upload_file(file_name,file_path):
    blob_client = blob_service_client.get_blob_client(
        container = container_name, # container to write to
        blob = file_name )
    print(container_name,'''container_client''',blob_client)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

def azure_download_file(file_name):
    blob_client = blob_service_client.get_blob_client(
        container = container_name, # container to write to
        blob = file_name )
    path = DOWNLOAD_FOLDER + file_name
    with open(path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())





