import random
import requests
from time import sleep

# Random User-Agent for Header Spoofing
def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4085.127 Mobile Safari/537.36"
    ]
    return random.choice(user_agents)

# Spoofing the X-Forwarded-For header (IP Spoofing)
def spoof_x_forwarded_for():
    ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
    return ip

# Function to send sophisticated requests
def send_sophisticated_request(url, threads, time_duration):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': random_user_agent(),  # Randomize User-Agent
        'Referer': 'https://www.example.com',
        'X-Forwarded-For': spoof_x_forwarded_for(),  # IP Spoofing
        'Origin': 'https://www.example.com',
    }
    
    try:
        for _ in range(time_duration):
            response = requests.get(url, headers=headers, timeout=5)
            print(f"Sent request to {url} with status: {response.status_code}")
            sleep(random.uniform(0.2, 0.5))  # Adding a small delay between requests
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")
