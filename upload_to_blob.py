from pathlib import Path
from azure.storage.blob import BlobServiceClient
from logger_config import setup_logger
import os
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv(
    "AZURE_STORAGE_CONNECTION_STRING"
)

logger = setup_logger()

connection_string = "hard coded secret"
container_name = "raw"

def upload_run_folder_to_blob(run_folder: Path):
    try:
        logger.info(f"Starting upload for folder: {run_folder}")

        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        for local_file in run_folder.rglob("*"):
            if local_file.is_file():
                blob_name = local_file.relative_to("data/raw").as_posix()

                blob_client = blob_service_client.get_blob_client(
                    container=container_name,
                    blob=blob_name
                )

                with open(local_file, "rb") as data:
                    blob_client.upload_blob(data, overwrite=True)

                logger.info(f"Uploaded file to Azure: {blob_name}")

        logger.info("Upload to Azure Blob Storage completed successfully")

    except Exception as e:
        logger.error(f"Upload to Azure Blob Storage failed: {e}")
        raise