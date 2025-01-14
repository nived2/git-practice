#!/usr/bin/env python3

import platform
import psutil
import datetime
from typing import Dict, Any


def get_memory_info() -> Dict[str, float]:
    """Get detailed memory information."""
    memory = psutil.virtual_memory()
    return {
        "total_gb": round(memory.total / (1024**3), 2),
        "available_gb": round(memory.available / (1024**3), 2),
        "used_gb": round(memory.used / (1024**3), 2),
        "percentage": memory.percent,
    }


def get_disk_info() -> Dict[str, Any]:
    """Get disk usage information for all partitions."""
    disk_info = {}
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info[partition.mountpoint] = {
                "total_gb": round(usage.total / (1024**3), 2),
                "used_gb": round(usage.used / (1024**3), 2),
                "free_gb": round(usage.free / (1024**3), 2),
                "percentage": usage.percent,
                "fstype": partition.fstype,
            }
        except PermissionError:
            continue
    return disk_info


def get_network_info() -> Dict[str, Any]:
    """Get network interface statistics."""
    network_info = {}
    net_io = psutil.net_io_counters(pernic=True)

    for interface, stats in net_io.items():
        network_info[interface] = {
            "bytes_sent_mb": round(stats.bytes_sent / (1024**2), 2),
            "bytes_recv_mb": round(stats.bytes_recv / (1024**2), 2),
            "packets_sent": stats.packets_sent,
            "packets_recv": stats.packets_recv,
            "errors_in": stats.errin,
            "errors_out": stats.errout,
            "dropped_in": stats.dropin,
            "dropped_out": stats.dropout,
        }
    return network_info


def get_system_info() -> Dict[str, Any]:
    """Get comprehensive system information."""
    info = {
        "system": platform.system(),
        "platform": platform.platform(),
        "processor": platform.processor(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "network": get_network_info(),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return info


def display_info(info: Dict[str, Any]) -> None:
    """Display system information in a formatted way."""
    print("\n=== System Information ===")
    for key, value in info.items():
        if key == "memory":
            print("\nMemory Details:")
            for mem_key, mem_value in value.items():
                print(
                    f"  {mem_key.replace('_', ' ').title()}: {mem_value} {'GB' if 'gb' in mem_key else '%'}"
                )
        elif key == "disk":
            print("\nDisk Usage:")
            for mount, disk_data in value.items():
                print(f"\n  Mount Point: {mount}")
                for disk_key, disk_value in disk_data.items():
                    print(
                        f"    {disk_key.replace('_', ' ').title()}: {disk_value} {'GB' if 'gb' in disk_key else '%' if disk_key == 'percentage' else ''}"
                    )
        elif key == "network":
            print("\nNetwork Statistics:")
            for interface, net_data in value.items():
                print(f"\n  Interface: {interface}")
                for net_key, net_value in net_data.items():
                    print(
                        f"    {net_key.replace('_', ' ').title()}: {net_value} {'MB' if 'mb' in net_key else ''}"
                    )
        else:
            print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    system_info = get_system_info()
    display_info(system_info)
