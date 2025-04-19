import os
import requests

api_address = "fastapi"
api_port = 8000

test_cases = [
    {"user": "alice", "password": "wonderland", "version": "v1", "expected": 200},
    {"user": "alice", "password": "wonderland", "version": "v2", "expected": 200},
    {"user": "bob", "password": "builder", "version": "v1", "expected": 200},
    {"user": "bob", "password": "builder", "version": "v2", "expected": 403}
]

for case in test_cases:
    response = requests.get(
        f'http://{api_address}:{api_port}/{case["version"]}/sentiment',
        params={
            "username": case["user"],
            "password": case["password"],
            "sentence": "test sentence"
        }
    )
    
    status = "SUCCESS" if response.status_code == case["expected"] else "FAILURE"
    
    output = f"""
============================
    Authorization Test ({case["version"]})
============================
User: {case["user"]}
Endpoint: /{case["version"]}/sentiment
Expected: {case["expected"]}
Actual: {response.status_code}
==> {status}
"""
    print(output)
    
    if os.environ.get('LOG') == '1':
        with open('/logs/api_test.log', 'a') as f:
            f.write(output)