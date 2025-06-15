import requests

HOST_ADDRESS = "127.0.0.1"
PORT = "5000"

response = requests.get(f'http://{HOST_ADDRESS}:{PORT}/movie')

if response.status_code == 200:
    print('health check status ok')
else:
    raise Exception('movies api failed health check')