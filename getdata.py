from google.cloud import storage
import requests
import json
from datetime import datetime


def api_getdata(api_url, bucket_name, file_name):
    data_json = requests.get(api_url).json()
    
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(str(datetime.now().strftime("%Y%m%d_%H%M%S")) + '_' + file_name + ".json")
    blob.upload_from_string(json.dumps(data_json), content_type= 'application/json')

if __name__ == '__main__':
    api_url = 'https://fakestoreapi.com/products'
    bn = input('Bucket_name: ')
    fn = input('File_name: ')

    api_getdata(api_url, bucket_name = bn, file_name = fn)
    print(f'Upload {fn} to {bn} succsess')
