#!/usr/bin/env python3
"""
Complex Regex Patterns - Advanced Examples

Demonstrates:
- Complex password validation
- Log parsing with named groups
- IP and port extraction
- JSON-like parsing
"""

import re


def example_complex_password():
    """Validate complex password"""
    print("=" * 60)
    print("Complex Password Validation")
    print("=" * 60)
    
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])(?!.*\s)(?!.*(.)\1{2,}).{8,}$'
    test_cases = [
        "Password123!",
        "PASS123!word",
        "password123!",
        "Pass123!",
        "Pass 123!",
        "Paass123!"
    ]
    
    print(f"Pattern: {pattern}")
    print("Requirements:")
    print("  - At least 8 characters")
    print("  - Contains uppercase")
    print("  - Contains lowercase")
    print("  - Contains digit")
    print("  - Contains special char")
    print("  - No spaces")
    print("  - No 3+ repeated chars")
    print()
    
    for text in test_cases:
        match = re.match(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def example_log_parsing_named_groups():
    """Parse log entry with named groups"""
    print("=" * 60)
    print("Log Parsing with Named Groups")
    print("=" * 60)
    
    pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+\[(?P<level>\w+)\]\s+(?P<message>.*)'
    log_line = "2023-12-25 10:30:45 [ERROR] Database connection failed"
    
    match = re.match(pattern, log_line)
    if match:
        print(f"Pattern: {pattern}")
        print(f"Log: {log_line}")
        print(f"\nParsed:")
        print(f"  Timestamp: {match.group('timestamp')}")
        print(f"  Level: {match.group('level')}")
        print(f"  Message: {match.group('message')}")
    print()


def example_extract_ip_port():
    """Extract IP and port combinations"""
    print("=" * 60)
    print("Extract IP and Port Combinations")
    print("=" * 60)
    
    pattern = r'(\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5})'
    text = "Server at 192.168.1.1:8080 and 10.0.0.1:443"
    
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print("\nExtracted:")
    for match in re.finditer(pattern, text):
        ip = match.group(1)
        port = match.group(2)
        print(f"  IP: {ip}, Port: {port}")
    print()


def example_parse_json_like():
    """Parse JSON-like logs (simplified)"""
    print("=" * 60)
    print("Parse JSON-like Logs")
    print("=" * 60)
    
    pattern = r'"(\w+)":\s*"([^"]*)"'
    log_line = '{"level": "ERROR", "message": "Connection failed", "code": "500"}'
    
    matches = re.findall(pattern, log_line)
    result = dict(matches)
    
    print(f"Pattern: {pattern}")
    print(f"Log: {log_line}")
    print(f"\nParsed: {result}")
    print()


def example_nested_parentheses():
    """Match nested parentheses (2 levels)"""
    print("=" * 60)
    print("Nested Parentheses (2 Levels)")
    print("=" * 60)
    
    pattern = r'\(([^()]+|\([^()]*\))*\)'
    test_cases = [
        "outer (inner (nested) more) text",
        "(simple)",
        "(level1 (level2) end)"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        if match:
            print(f"✓ '{text}' -> '{match.group()}'")
        else:
            print(f"✗ '{text}'")
    print()


def example_extract_url_components():
    """Extract URL components"""
    print("=" * 60)
    print("Extract URL Components")
    print("=" * 60)
    
    pattern = r'(https?)://([^/]+)(/[^\s?]*)?(\?[^\s]*)?'
    test_cases = [
        "https://www.example.com/path?param=value",
        "http://example.com"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        if match:
            protocol = match.group(1)
            domain = match.group(2)
            path = match.group(3) or "(none)"
            query = match.group(4) or "(none)"
            print(f"\nURL: {text}")
            print(f"  Protocol: {protocol}")
            print(f"  Domain: {domain}")
            print(f"  Path: {path}")
            print(f"  Query: {query}")
    print()


def main():
    """Run all complex pattern examples"""
    print("\n" + "=" * 60)
    print("COMPLEX REGEX PATTERNS - PYTHON EXAMPLES")
    print("=" * 60 + "\n")
    
    example_complex_password()
    example_log_parsing_named_groups()
    example_extract_ip_port()
    example_parse_json_like()
    example_nested_parentheses()
    example_extract_url_components()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

