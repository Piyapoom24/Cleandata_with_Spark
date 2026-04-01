from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from google.cloud import storage
from datetime import datetime
import os, io
import pandas as pd

load_dotenv()

client = storage.Client()
bucket = client.bucket(os.getenv('GCS_BUCKET'))
folder = 'shopping-mall'

engine = create_engine(
    f"mysql+pymysql://{os.getenv('MySQL_USER')}:{os.getenv('MySQL_PASSWORD')}"
    f"@{os.getenv('MySQL_HOST')}/{os.getenv('MySQL_DATABASE')}"
)

query = "SELECT TransactionNo, timestamp(Date) as Date_time, ProductNo, Price, Quantity, CustomerNo FROM transaction"
data = pd.read_sql(query, engine)

data['Date_time'] = data['Date_time'].astype('datetime64[us]')

buffer = io.BytesIO()
data.to_parquet(buffer, index=False)
buffer.seek(0)

blob = bucket.blob(f"{folder}/{datetime.now().strftime('%Y%m%d_%H%M%S')}_transaction.parquet")
blob.upload_from_file(buffer, content_type="application/octet-stream")

print(f"Uploaded: transaction.parquet to gs://raw-data02/{folder}/{blob.name}")