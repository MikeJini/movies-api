import requests
import time

HOST_ADDRESS = "127.0.0.1"
PORT = "5000"
WAIT_TIME = 5

# Let the API wake up
time.sleep(WAIT_TIME)

response = requests.get(f'http://{HOST_ADDRESS}:{PORT}/movie')

if response.status_code == 200:
    print('health check status ok')
else:
    raise Exception('movies api failed health check')