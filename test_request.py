import requests
print("Making request")
try:
    response = requests.get('http://127.0.0.1:8005/test')
    print('Status:', response.status_code)
    print('Response:', response.text)
except Exception as e:
    print('Exception:', e)
print("Request done")