import requests
import json

GATEWAY_URL = "http://127.0.0.1:8000/api/generate"

def test_access(user_name, token, model_name, prompt):
    print(f"\n--- Testing Access for: {user_name} ---")
    print(f"Attempting to use model: {model_name}")
    
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(GATEWAY_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("[SUCCESS] Access Granted.")
            # Print just the first 100 characters of the response to keep the terminal clean
            ai_response = response.json().get('response', '')
            print(f"AI Output: {ai_response[:100]}...\n")
        else:
            print(f"[BLOCKED] HTTP {response.status_code}: {response.json().get('detail')}\n")
            
    except requests.exceptions.ConnectionError:
        print("[ERROR] Could not connect to the API Gateway. Is it running?")

if __name__ == "__main__":
    print("Initiating Sovereign RBAC Security Test...")
    
    # Test 1: Student tries to bypass security and use the unrestricted Llama 3.2 model
    test_access(
        user_name="Student", 
        token="student_secret_112", 
        model_name="llama3.2", 
        prompt="Write a python script for binary search."
    )
    
    # Test 2: Student uses their authorized Sovereign-Tutor model
    test_access(
        user_name="Student", 
        token="student_secret_112", 
        model_name="Sovereign-Tutor", 
        prompt="Write a python script for binary search."
    )