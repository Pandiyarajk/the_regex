# Project: Log File Parser

Build a tool to parse Apache/Nginx log files and extract structured data using regex.

## Project Overview

Create a log parser that:
- Parses Apache Common Log Format or Nginx logs
- Extracts IP addresses, timestamps, URLs, status codes
- Saves parsed data to CSV
- Provides statistics and analysis

## Log Format

### Apache Common Log Format
```
127.0.0.1 - - [25/Dec/2023:10:30:45 +0000] "GET /page HTTP/1.1" 200 1234
```

Format: `IP - - [timestamp] "method path protocol" status size`

### Nginx Log Format (Similar)
```
127.0.0.1 - - [25/Dec/2023:10:30:45 +0000] "GET /page HTTP/1.1" 200 1234 "-" "Mozilla/5.0"
```

## Implementation

### Python Version

**File: `log_parser.py`**

```python
#!/usr/bin/env python3
import re
import csv
import sys
from datetime import datetime
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
```

### JavaScript Version

**File: `log_parser.js`**

```javascript
#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

function parseApacheLog(logLine) {
    // Pattern for Apache Common Log Format
    const pattern = /^(\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+\[([^\]]+)\]\s+"(\w+)\s+([^\s]+)\s+([^"]+)"\s+(\d+)\s+(\d+|-)$/;
    
    const match = logLine.match(pattern);
    
    if (!match) {
        return null;
    }
    
    return {
        ip: match[1],
        timestamp: match[2],
        method: match[3],
        path: match[4],
        protocol: match[5].trim(),
        status: match[6],
        size: match[7] === '-' ? '0' : match[7]
    };
}

function parseLogFile(filename) {
    try {
        const content = fs.readFileSync(filename, 'utf-8');
        const lines = content.split('\n');
        const entries = [];
        
        lines.forEach((line, index) => {
            const trimmed = line.trim();
            if (!trimmed) return;
            
            const entry = parseApacheLog(trimmed);
            if (entry) {
                entry.line_number = index + 1;
                entries.push(entry);
            } else {
                console.log(`Warning: Could not parse line ${index + 1}: ${trimmed.substring(0, 50)}...`);
            }
        });
        
        return entries;
    } catch (error) {
        console.error(`Error reading file: ${error.message}`);
        return [];
    }
}

function saveToCSV(entries, outputFile) {
    if (entries.length === 0) {
        console.log("No entries to save.");
        return;
    }
    
    const headers = ['ip', 'timestamp', 'method', 'path', 'protocol', 'status', 'size'];
    const csvLines = [
        headers.join(',')
    ];
    
    entries.forEach(entry => {
        const row = headers.map(header => {
            const value = entry[header] || '';
            // Escape commas and quotes in CSV
            if (value.includes(',') || value.includes('"')) {
                return `"${value.replace(/"/g, '""')}"`;
            }
            return value;
        });
        csvLines.push(row.join(','));
    });
    
    try {
        fs.writeFileSync(outputFile, csvLines.join('\n'), 'utf-8');
        console.log(`✓ Saved ${entries.length} entries to ${outputFile}`);
    } catch (error) {
        console.error(`Error saving CSV: ${error.message}`);
    }
}

function analyzeLogs(entries) {
    if (entries.length === 0) {
        console.log("No entries to analyze.");
        return;
    }
    
    console.log('\n' + '='.repeat(50));
    console.log("LOG ANALYSIS");
    console.log('='.repeat(50));
    
    // Status codes
    const statusCodes = {};
    entries.forEach(entry => {
        statusCodes[entry.status] = (statusCodes[entry.status] || 0) + 1;
    });
    
    console.log(`\nTotal entries: ${entries.length}`);
    console.log("\nStatus codes:");
    Object.entries(statusCodes)
        .sort((a, b) => b[1] - a[1])
        .forEach(([status, count]) => {
            console.log(`  ${status}: ${count}`);
        });
    
    // HTTP methods
    const methods = {};
    entries.forEach(entry => {
        methods[entry.method] = (methods[entry.method] || 0) + 1;
    });
    
    console.log("\nHTTP methods:");
    Object.entries(methods)
        .sort((a, b) => b[1] - a[1])
        .forEach(([method, count]) => {
            console.log(`  ${method}: ${count}`);
        });
    
    // Top IPs
    const ips = {};
    entries.forEach(entry => {
        ips[entry.ip] = (ips[entry.ip] || 0) + 1;
    });
    
    console.log("\nTop 10 IP addresses:");
    Object.entries(ips)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10)
        .forEach(([ip, count]) => {
            console.log(`  ${ip}: ${count}`);
        });
}

function main() {
    const args = process.argv.slice(2);
    
    if (args.length < 1) {
        console.log("Usage: node log_parser.js <log_file> [output.csv]");
        process.exit(1);
    }
    
    const logFile = args[0];
    const outputFile = args[1] || 'parsed_logs.csv';
    
    console.log(`Parsing log file: ${logFile}`);
    const entries = parseLogFile(logFile);
    
    if (entries.length > 0) {
        console.log(`✓ Parsed ${entries.length} entries`);
        analyzeLogs(entries);
        saveToCSV(entries, outputFile);
    } else {
        console.log("No entries parsed.");
    }
}

if (require.main === module) {
    main();
}
```

## Sample Log File

Create `sample.log`:

```
127.0.0.1 - - [25/Dec/2023:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.1 - - [25/Dec/2023:10:31:12 +0000] "POST /api/login HTTP/1.1" 200 567
10.0.0.1 - - [25/Dec/2023:10:32:00 +0000] "GET /page/notfound HTTP/1.1" 404 123
127.0.0.1 - - [25/Dec/2023:10:33:15 +0000] "GET /index.html HTTP/1.1" 200 1234
```

## Usage

### Python

```bash
python log_parser.py sample.log
python log_parser.py sample.log output.csv
```

### JavaScript

```bash
node log_parser.js sample.log
node log_parser.js sample.log output.csv
```

## Extensions

1. **Support multiple log formats**
   - Apache Combined Log Format
   - Nginx custom formats
   - Custom regex patterns

2. **Advanced analysis**
   - Error rate calculation
   - Response time analysis
   - Geographic IP lookup

3. **Real-time parsing**
   - Watch log files
   - Stream processing
   - Alert on errors

## Key Learning Points

- Parsing structured text with regex
- Extracting multiple groups
- Handling file I/O
- Data analysis and statistics
- CSV export functionality

---

**Next Project:** [project-scrape-html.md](project-scrape-html.md)

