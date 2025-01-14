#!/usr/bin/env python3

import platform
import psutil
import datetime

def get_system_info():
    """Get basic system information."""
    info = {
        'system': platform.system(),
        'platform': platform.platform(),
        'processor': platform.processor(),
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory_usage': psutil.virtual_memory().percent,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return info

def display_info(info):
    """Display system information in a formatted way."""
    print("\n=== System Information ===")
    for key, value in info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

if __name__ == "__main__":
    system_info = get_system_info()
    display_info(system_info)
