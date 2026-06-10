from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


KEY_VAULT_NAME = "storage-connection"
KEY_VAULT_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net/"


def get_secret(secret_name: str) -> str:
    credential = DefaultAzureCredential()
    client = SecretClient(
        vault_url=KEY_VAULT_URI,
        credential=credential
    )

    secret = client.get_secret(secret_name)
    return secret.value