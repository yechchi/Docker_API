import os
import requests

api_address = "fastapi"
api_port = 8000

test_cases = [
    {"sentence": "life is beautiful", "expected": "positive"},
    {"sentence": "that sucks", "expected": "negative"}
]

for case in test_cases:
    for version in ["v1", "v2"]:
        response = requests.get(
            f'http://{api_address}:{api_port}/{version}/sentiment',
            params={
                "username": "alice",
                "password": "wonderland",
                "sentence": case["sentence"]
            }
        )
        
        score = response.json().get("score", 0)
        result = "positive" if score > 0 else "negative"
        status = "SUCCESS" if result == case["expected"] else "FAILURE"
        
        output = f"""
============================
    Content Test ({version})
============================
Sentence: "{case["sentence"]}"
Expected: {case["expected"]}
Actual: {result} (score: {score})
==> {status}
"""
        print(output)
        
        if os.environ.get('LOG') == '1':
            with open('/logs/api_test.log', 'a') as f:
                f.write(output)