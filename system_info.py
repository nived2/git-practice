#!/usr/bin/env python3

import platform
import psutil
import datetime

def get_memory_info():
    """Get detailed memory information."""
    memory = psutil.virtual_memory()
    return {
        'total_gb': round(memory.total / (1024**3), 2),
        'available_gb': round(memory.available / (1024**3), 2),
        'used_gb': round(memory.used / (1024**3), 2),
        'percentage': memory.percent
    }

def get_system_info():
    """Get basic system information."""
    info = {
        'system': platform.system(),
        'platform': platform.platform(),
        'processor': platform.processor(),
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory': get_memory_info(),
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return info

def display_info(info):
    """Display system information in a formatted way."""
    print("\n=== System Information ===")
    for key, value in info.items():
        if key == 'memory':
            print("\nMemory Details:")
            for mem_key, mem_value in value.items():
                print(f"  {mem_key.replace('_', ' ').title()}: {mem_value} {'GB' if 'gb' in mem_key else '%'}")
        else:
            print(f"{key.replace('_', ' ').title()}: {value}")

if __name__ == "__main__":
    system_info = get_system_info()
    display_info(system_info)
