from azure.storage.blob import BlobServiceClient
import keys

storage_account_key = keys.storage_account_key
storage_account_name = keys.storage_account_name
connection_string = keys.connection_string
container_name = keys.container_name

# Function to upload interview conversation to azure blob storage
def uploadToBlobStorage(file_path,file_name):
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)
   blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
   with open(file_path,"rb") as data:
      blob_client.upload_blob(data,overwrite=True)
      print(f"Uploaded {file_name}.")

