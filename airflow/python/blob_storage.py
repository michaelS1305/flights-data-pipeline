from pathlib import Path
from azure.storage.blob import BlobServiceClient
from key_vault_config import get_secret
from logger_config import setup_logger

logger = setup_logger()

CONTAINER_NAME = "data" 


def get_blob_service_client():
    connection_string = get_secret("azure-storage-connection-string").strip()
    return BlobServiceClient.from_connection_string(connection_string)


def upload_file_to_blob(local_file_path: Path, blob_name: str):
    blob_service_client = get_blob_service_client()

    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER_NAME,
        blob=blob_name
    )

    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    logger.info(f"Uploaded file to Azure: {blob_name}")


def download_latest_blob(prefix: str, local_download_path: Path):
    blob_service_client = get_blob_service_client()
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    blobs = list(container_client.list_blobs(name_starts_with=prefix))

    if not blobs:
        raise FileNotFoundError(f"No blobs found under prefix: {prefix}")

    latest_blob = sorted(blobs, key=lambda b: b.last_modified)[-1]

    logger.info(f"Latest blob found: {latest_blob.name}")

    blob_client = container_client.get_blob_client(latest_blob.name)

    local_download_path.parent.mkdir(parents=True, exist_ok=True)

    with open(local_download_path, "wb") as file:
        file.write(blob_client.download_blob().readall())

    logger.info(f"Downloaded blob to: {local_download_path}")

    return local_download_path


