import subprocess
import os
import zipfile

zip_path = os.path.expanduser('./data/archive.zip') 
extract_path = os.path.expanduser('./data')

os.makedirs(extract_path, exist_ok=True)

curl_command = [
    'curl', '-L', '-o', zip_path,
    'https://www.kaggle.com/api/v1/datasets/download/mirichoi0218/insurance',
    "--ssl-no-revoke"
]

if not os.path.exists(zip_path):
    subprocess.run(curl_command)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)