# System Information Utility

A Python-based system monitoring utility that provides comprehensive information about your system's resources.

## Features

- System information (OS, Platform, Processor)
- CPU usage monitoring
- Detailed memory statistics
  - Total memory
  - Available memory
  - Used memory
  - Memory usage percentage
- Disk usage information
  - Total, used, and free space for each partition
  - File system type
  - Usage percentage
- Network statistics
  - Bytes sent/received
  - Packets sent/received
  - Error and drop counts
  - Per-interface statistics

## Requirements

- Python 3.x
- psutil==5.9.5

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nived2/git-practice.git
cd git-practice
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python3 system_info.py
```

Example output:
```
=== System Information ===
System: Linux
Platform: Linux-x86_64
Processor: x86_64
CPU Usage: 8.8%

Memory Details:
  Total GB: 15.31 GB
  Available GB: 10.80 GB
  Used GB: 2.85 GB
  Percentage: 29.4%

Disk Usage:
  Mount Point: /
    Total GB: 512.0 GB
    Used GB: 125.3 GB
    Free GB: 386.7 GB
    Percentage: 24.5%
    Fstype: ext4

Network Statistics:
  Interface: eth0
    Bytes Sent MB: 258.5 MB
    Bytes Recv MB: 1024.2 MB
    Packets Sent: 156942
    Packets Recv: 984521
    Errors In: 0
    Errors Out: 0
    Dropped In: 0
    Dropped Out: 0
```

## Development

### Running Tests

```bash
python3 -m unittest test_system_info.py -v
```

### Type Hints

The code includes type hints for better IDE support and code documentation.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
