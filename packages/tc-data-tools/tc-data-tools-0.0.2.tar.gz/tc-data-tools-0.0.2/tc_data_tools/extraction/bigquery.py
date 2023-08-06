import pandas as pd
from data_tools.io import gcs_upload

def df_from_bigquery(query, gcp_project, gcs_bucket, gcs_file_path, local_file_path, mode='csv'):
    
    df = pd.read_gbq(query, gcp_project)
    
    if mode == 'csv':
        df.to_csv(local_file_path)
    elif mode == 'parquet':
        df.to_parquet(local_file_path)
        
    gcs_upload(gcp_project, gcs_bucket, gcs_file_path, local_file_path)
    
    return df