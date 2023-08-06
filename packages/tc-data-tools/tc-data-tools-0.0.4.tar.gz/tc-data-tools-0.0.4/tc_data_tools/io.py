from google.cloud import storage


def gcs_upload(gcp_project, gcs_bucket, gcs_file_path, local_file_path):
    """
    Upload a local local to google cloud storage
    """

    # create conncetion
    client = storage.Client(gcp_project)
    bucket = client.bucket(gcs_bucket)
    # upload
    blob = bucket.blob(gcs_file_path)
    blob.upload_from_filename(local_file_path)

    # INCLUIR LOGS


def gcs_download(gcp_project, gcs_bucket, gcs_file_path, local_file_path):
    """
    Downloads a google cloud storage file
    """

    # create conncetion
    storage_client = storage.Client(gcp_project)
    bucket = storage_client.bucket(gcs_bucket)
    # download
    blob = bucket.blob(gcs_file_path)
    blob.download_to_filename(local_file_path)

    # INCLUIR LOGS

