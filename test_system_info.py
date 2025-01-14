import pytest
from system_info import (
    get_memory_info,
    get_system_info,
    get_disk_info,
    get_network_info,
)


class TestSystemInfo:
    def test_memory_info(self):
        """Test if memory info returns the correct structure"""
        memory_info = get_memory_info()

        # Check if all required keys are present
        required_keys = {"total_gb", "available_gb", "used_gb", "percentage"}
        assert set(memory_info.keys()) == required_keys

        # Check if values are of correct type and in valid ranges
        assert isinstance(memory_info["total_gb"], float)
        assert isinstance(memory_info["available_gb"], float)
        assert isinstance(memory_info["used_gb"], float)
        assert isinstance(memory_info["percentage"], float)

        # Check if values make sense
        assert memory_info["total_gb"] > 0
        assert memory_info["available_gb"] <= memory_info["total_gb"]
        assert memory_info["percentage"] >= 0
        assert memory_info["percentage"] <= 100

    def test_disk_info(self):
        """Test if disk info returns the correct structure"""
        disk_info = get_disk_info()

        # Check if we got any disk information
        assert len(disk_info) > 0

        # Check structure for each mount point
        for mount_point, info in disk_info.items():
            assert isinstance(mount_point, str)
            required_keys = {"total_gb", "used_gb", "free_gb", "percentage", "fstype"}
            assert set(info.keys()) == required_keys

            # Check value types and ranges
            assert isinstance(info["total_gb"], float)
            assert isinstance(info["used_gb"], float)
            assert isinstance(info["free_gb"], float)
            assert isinstance(info["percentage"], float)
            assert isinstance(info["fstype"], str)

            # Check if values make sense
            assert info["total_gb"] > 0
            assert info["percentage"] >= 0
            assert info["percentage"] <= 100

    def test_network_info(self):
        """Test if network info returns the correct structure"""
        network_info = get_network_info()

        # Check if we got any network information
        assert len(network_info) > 0

        # Check structure for each interface
        for interface, info in network_info.items():
            assert isinstance(interface, str)
            required_keys = {
                "bytes_sent_mb",
                "bytes_recv_mb",
                "packets_sent",
                "packets_recv",
                "errors_in",
                "errors_out",
                "dropped_in",
                "dropped_out",
            }
            assert set(info.keys()) == required_keys

            # Check value types
            assert isinstance(info["bytes_sent_mb"], float)
            assert isinstance(info["bytes_recv_mb"], float)
            assert isinstance(info["packets_sent"], int)
            assert isinstance(info["packets_recv"], int)

            # Check if values make sense
            assert info["bytes_sent_mb"] >= 0
            assert info["bytes_recv_mb"] >= 0
            assert info["packets_sent"] >= 0
            assert info["packets_recv"] >= 0

    def test_system_info(self):
        """Test if system info returns the correct structure"""
        system_info = get_system_info()

        # Check if all required keys are present
        required_keys = {
            "system",
            "platform",
            "processor",
            "cpu_usage",
            "memory",
            "disk",
            "network",
            "timestamp",
        }
        assert set(system_info.keys()) == required_keys

        # Check if values are of correct type
        assert isinstance(system_info["system"], str)
        assert isinstance(system_info["platform"], str)
        assert isinstance(system_info["processor"], str)
        assert isinstance(system_info["cpu_usage"], float)
        assert isinstance(system_info["memory"], dict)
        assert isinstance(system_info["disk"], dict)
        assert isinstance(system_info["network"], dict)
        assert isinstance(system_info["timestamp"], str)
