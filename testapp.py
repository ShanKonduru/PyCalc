import requests
import time

def test_add_numbers(num1, num2, expected_result):
    url = "http://localhost:5000/add"
    data = {
        "num1": num1,
        "num2": num2
    }

    start_time = time.time()
    response = requests.post(url, json=data)
    end_time = time.time()

    response_time = end_time - start_time

    if response.status_code == 200:
        result = response.json()["result"]
        if result == expected_result:
            print(f"Test passed: Response time={response_time:.6f}s, Result={result}")
        else:
            print(f"Test failed: Unexpected result. Expected={expected_result}, Actual={result}")
    else:
        print("Test failed: Error in response")

# Test cases
test_add_numbers(5, 3, 8)  # Test case 1: 5 + 3 = 8
test_add_numbers(-2, 7, 5) # Test case 2: -2 + 7 = 5
