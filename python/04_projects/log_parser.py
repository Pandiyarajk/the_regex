#!/usr/bin/env python3
"""
Log File Parser - Project Implementation

Parses Apache/Nginx log files and extracts structured data.
"""

import re
import csv
import sys
from collections import Counter


def parse_apache_log(log_line):
    """
    Parse Apache Common Log Format entry.
    
    Returns dict with parsed fields or None if parsing fails.
    """
    # Pattern for Apache Common Log Format
    pattern = r'(\d+\.\d+\.\d+\.\d+)\s+'  # IP
    pattern += r'-\s+'                     # Remote logname (usually -)
    pattern += r'-\s+'                     # Remote user (usually -)
    pattern += r'\[([^\]]+)\]\s+'          # Timestamp
    pattern += r'"(\w+)\s+'                # HTTP method
    pattern += r'([^\s]+)\s+'              # Path
    pattern += r'([^"]+)"\s+'              # Protocol
    pattern += r'(\d+)\s+'                 # Status code
    pattern += r'(\d+|-)'                  # Size
    
    match = re.match(pattern, log_line)
    
    if not match:
        return None
    
    return {
        'ip': match.group(1),
        'timestamp': match.group(2),
        'method': match.group(3),
        'path': match.group(4),
        'protocol': match.group(5).strip(),
        'status': match.group(6),
        'size': match.group(7) if match.group(7) != '-' else '0'
    }


def parse_log_file(filename):
    """Parse entire log file and return list of entries."""
    entries = []
    
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                
                entry = parse_apache_log(line)
                if entry:
                    entry['line_number'] = line_num
                    entries.append(entry)
                else:
                    print(f"Warning: Could not parse line {line_num}: {line[:50]}...")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return entries


def save_to_csv(entries, output_file):
    """Save parsed entries to CSV file."""
    if not entries:
        print("No entries to save.")
        return
    
    fieldnames = ['ip', 'timestamp', 'method', 'path', 'protocol', 'status', 'size']
    
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(entries)
        print(f"✓ Saved {len(entries)} entries to {output_file}")
    except Exception as e:
        print(f"Error saving CSV: {e}")


def analyze_logs(entries):
    """Analyze parsed log entries and print statistics."""
    if not entries:
        print("No entries to analyze.")
        return
    
    print("\n" + "="*50)
    print("LOG ANALYSIS")
    print("="*50)
    
    # Total entries
    print(f"\nTotal entries: {len(entries)}")
    
    # Status codes
    status_codes = Counter(entry['status'] for entry in entries)
    print("\nStatus codes:")
    for status, count in status_codes.most_common():
        print(f"  {status}: {count}")
    
    # HTTP methods
    methods = Counter(entry['method'] for entry in entries)
    print("\nHTTP methods:")
    for method, count in methods.most_common():
        print(f"  {method}: {count}")
    
    # Top IPs
    ips = Counter(entry['ip'] for entry in entries)
    print("\nTop 10 IP addresses:")
    for ip, count in ips.most_common(10):
        print(f"  {ip}: {count}")
    
    # Top paths
    paths = Counter(entry['path'] for entry in entries)
    print("\nTop 10 paths:")
    for path, count in paths.most_common(10):
        print(f"  {path}: {count}")


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python log_parser.py <log_file> [output.csv]")
        sys.exit(1)
    
    log_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'parsed_logs.csv'
    
    print(f"Parsing log file: {log_file}")
    entries = parse_log_file(log_file)
    
    if entries:
        print(f"✓ Parsed {len(entries)} entries")
        analyze_logs(entries)
        save_to_csv(entries, output_file)
    else:
        print("No entries parsed.")


if __name__ == "__main__":
    main()

