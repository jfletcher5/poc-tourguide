import os
from google.cloud import secretmanager

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Function to access a secret version in Secret Manager
def access_secret_version(project_id, secret_id, version_id="latest"):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode('UTF-8')

# Retrieve the OpenAI API key
def get_api_key():
    #local
    # return os.getenv('OPENAI_API_KEY')

    # GCP
    project_id = os.getenv('GCLOUD_PROJECT_ID')
    return access_secret_version(project_id, "OPENAI_API_KEY")