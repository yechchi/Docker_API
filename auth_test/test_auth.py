import os
import requests

api_address = "fastapi" 
api_port = 8000

# Test cases
test_cases = [
    {"username": "alice", "password": "wonderland", "expected": 200},
    {"username": "bob", "password": "builder", "expected": 200},
    {"username": "clementine", "password": "mandarine", "expected": 403}
]

for case in test_cases:
    response = requests.get(
        f'http://{api_address}:{api_port}/permissions',
        params={"username": case["username"], "password": case["password"]}
    )
    
    status = "SUCCESS" if response.status_code == case["expected"] else "FAILURE"
    
    output = f"""
============================
    Authentication Test
============================
Request to /permissions
| username: {case["username"]}
| password: {case["password"]}
Expected: {case["expected"]}
Actual: {response.status_code}
==> {status}
"""
    print(output)
    
    if os.environ.get('LOG') == '1':
        with open('/logs/api_test.log', 'a') as f:
            f.write(output)