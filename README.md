# System Information Utility

A Python-based system monitoring utility that provides detailed information about your system's resources.

## Features

- System information (OS, Platform, Processor)
- CPU usage monitoring
- Detailed memory statistics
  - Total memory
  - Available memory
  - Used memory
  - Memory usage percentage

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
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
