import requests
import random

# Function to generate advanced headers with HTTP/2 or HTTP/3 support
def generate_advanced_headers():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    ]
    return {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': random.choice(user_agents),
        'X-Forwarded-For': '192.168.1.1',
        'Origin': 'https://www.example.com',
    }

# Function to simulate GET requests with advanced options
def send_advanced_request(url):
    headers = generate_advanced_headers()
    try:
        response = requests.get(url, headers=headers, timeout=5)
        print(f"Sent request to {url} with status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error with {url}: {str(e)}")
