#!/usr/bin/env python3
"""
Intermediate Regex Exercises - Solutions

This module contains solutions for intermediate regex exercises.
"""

import re


def exercise_1_validate_strong_password():
    """Exercise 1: Validate Strong Password"""
    print("=" * 60)
    print("Exercise 1: Validate Strong Password")
    print("=" * 60)
    
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$'
    test_cases = [
        "Password123!",
        "password123!",
        "PASSWORD123!",
        "Password!",
        "Password123",
        "Pass123!"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.match(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def exercise_2_extract_hashtags():
    """Exercise 2: Extract Hashtags"""
    print("=" * 60)
    print("Exercise 2: Extract Hashtags")
    print("=" * 60)
    
    pattern = r'#(\w+)'
    test_cases = [
        "Check out #regex and #coding!",
        "#python #javascript #webdev",
        "#123abc #test-case",
        "No hashtags here"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        matches = re.findall(pattern, text)
        if matches:
            print(f"✓ '{text}' -> {matches}")
        else:
            print(f"✗ '{text}' -> No hashtags")
    print()


def exercise_3_extract_prices():
    """Exercise 3: Extract Price Values"""
    print("=" * 60)
    print("Exercise 3: Extract Price Values")
    print("=" * 60)
    
    pattern = r'\$(\d+(?:\.\d{2})?)'
    test_cases = [
        "Price is $100",
        "Costs $99.99 each",
        "Total: $1,234.56",
        "Free item"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        matches = re.findall(pattern, text)
        if matches:
            print(f"✓ '{text}' -> {matches}")
        else:
            print(f"✗ '{text}'")
    print()


def exercise_4_capitalized_words():
    """Exercise 4: Match All Capitalized Words"""
    print("=" * 60)
    print("Exercise 4: Match All Capitalized Words")
    print("=" * 60)
    
    pattern = r'\b[A-Z][a-z]+\b'
    test_cases = [
        "Hello World from Python",
        "HELLO world",
        "iPhone and iPad",
        "The Quick Brown Fox"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        matches = re.findall(pattern, text)
        print(f"Text: '{text}'")
        print(f"  Matches: {matches}")
    print()


def exercise_5_extract_domain():
    """Exercise 5: Extract Domain from URLs"""
    print("=" * 60)
    print("Exercise 5: Extract Domain from URLs")
    print("=" * 60)
    
    pattern = r'https?://(?:www\.)?([^/]+)'
    test_cases = [
        "http://example.com",
        "https://www.google.com/search",
        "ftp://files.example.org",
        "https://sub.domain.example.com"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        if match:
            domain = match.group(1)
            print(f"✓ '{text}' -> Domain: {domain}")
        else:
            print(f"✗ '{text}'")
    print()


def exercise_6_parse_log_entry():
    """Exercise 6: Parse Log Entry"""
    print("=" * 60)
    print("Exercise 6: Parse Log Entry")
    print("=" * 60)
    
    pattern = r'\[([^\]]+)\]\s+(\w+):\s+(.*)'
    test_cases = [
        "[2023-12-25 10:30:45] ERROR: Database connection failed",
        "[2023-01-01 00:00:00] INFO: Server started"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.match(pattern, text)
        if match:
            timestamp = match.group(1)
            level = match.group(2)
            message = match.group(3)
            print(f"Text: '{text}'")
            print(f"  Timestamp: {timestamp}")
            print(f"  Level: {level}")
            print(f"  Message: {message}")
    print()


def exercise_7_validate_credit_card():
    """Exercise 7: Validate Credit Card Format"""
    print("=" * 60)
    print("Exercise 7: Validate Credit Card Format")
    print("=" * 60)
    
    pattern = r'^\d{4}([- ]?)\d{4}\1\d{4}\1\d{4}$'
    test_cases = [
        "1234-5678-9012-3456",
        "1234 5678 9012 3456",
        "1234567890123456",
        "1234-5678 9012-3456",
        "1234-5678-9012"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.match(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def exercise_8_extract_email_parts():
    """Exercise 8: Extract Email Local Part and Domain"""
    print("=" * 60)
    print("Exercise 8: Extract Email Local Part and Domain")
    print("=" * 60)
    
    pattern = r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    test_cases = [
        "user@example.com",
        "john.doe@company.co.uk",
        "user+tag@subdomain.example.org"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        if match:
            local = match.group(1)
            domain = match.group(2)
            print(f"Email: '{text}'")
            print(f"  Local part: {local}")
            print(f"  Domain: {domain}")
    print()


def main():
    """Run all intermediate exercises"""
    print("\n" + "=" * 60)
    print("INTERMEDIATE REGEX EXERCISES - PYTHON SOLUTIONS")
    print("=" * 60 + "\n")
    
    exercise_1_validate_strong_password()
    exercise_2_extract_hashtags()
    exercise_3_extract_prices()
    exercise_4_capitalized_words()
    exercise_5_extract_domain()
    exercise_6_parse_log_entry()
    exercise_7_validate_credit_card()
    exercise_8_extract_email_parts()
    
    print("=" * 60)
    print("All exercises completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

