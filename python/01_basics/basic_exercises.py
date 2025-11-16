#!/usr/bin/env python3
"""
Basic Regex Exercises - Solutions

This module contains solutions for basic regex exercises.
Run this to see solutions in action.
"""

import re


def exercise_1_match_numbers():
    """Exercise 1: Match Numbers"""
    print("=" * 60)
    print("Exercise 1: Match Numbers")
    print("=" * 60)
    
    pattern = r'\d+'
    test_cases = [
        "Price is 123 dollars",
        "I have 5 apples",
        "Version 2.0.1",
        "No numbers here"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        matches = re.findall(pattern, text)
        print(f"Text: '{text}'")
        print(f"  Matches: {matches}")
    print()


def exercise_2_detect_mobile_number():
    """Exercise 2: Detect Mobile Number"""
    print("=" * 60)
    print("Exercise 2: Detect Mobile Number (10 digits)")
    print("=" * 60)
    
    # Simple 10 digits
    pattern1 = r'^\d{10}$'
    # With optional formatting
    pattern2 = r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}'
    
    test_cases = [
        "1234567890",
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "12-345-6789",
        "12345678901"
    ]
    
    print(f"Pattern (strict): {pattern1}")
    for text in test_cases:
        match = re.match(pattern1, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    
    print(f"\nPattern (with formatting): {pattern2}")
    for text in test_cases:
        matches = re.findall(pattern2, text)
        if matches:
            print(f"✓ '{text}' -> {matches}")
        else:
            print(f"✗ '{text}'")
    print()


def exercise_3_words_starting_with_a():
    """Exercise 3: Find All Words Starting with 'A'"""
    print("=" * 60)
    print("Exercise 3: Find All Words Starting with 'A'")
    print("=" * 60)
    
    pattern = r'\b[Aa]\w+\b'
    test_cases = [
        "Apple and application are awesome",
        "An apple a day",
        "Banana is yellow"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        matches = re.findall(pattern, text)
        print(f"Text: '{text}'")
        print(f"  Matches: {matches}")
    print()


def exercise_4_valid_pin_code():
    """Exercise 4: Match Valid PIN Code (4 or 6 digits)"""
    print("=" * 60)
    print("Exercise 4: Match Valid PIN Code")
    print("=" * 60)
    
    pattern = r'^(\d{4}|\d{6})$'
    test_cases = [
        "1234",
        "123456",
        "12345",
        "1234a",
        "12 34"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.match(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def exercise_5_extract_domain():
    """Exercise 5: Extract Domain Names"""
    print("=" * 60)
    print("Exercise 5: Extract Domain Names")
    print("=" * 60)
    
    pattern = r'https?://(?:www\.)?([^/]+)'
    test_cases = [
        "http://example.com",
        "https://www.google.com/search",
        "ftp://files.example.org",
        "example.com"
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


def exercise_6_time_format():
    """Exercise 6: Match Time Format (HH:MM)"""
    print("=" * 60)
    print("Exercise 6: Match Time Format (HH:MM)")
    print("=" * 60)
    
    # Strict pattern (00-23:00-59)
    pattern = r'([01]\d|2[0-3]):([0-5]\d)'
    test_cases = [
        "09:30",
        "23:59",
        "00:00",
        "24:00",
        "12:60",
        "9:30"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.match(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def exercise_7_repeated_words():
    """Exercise 7: Find Repeated Words"""
    print("=" * 60)
    print("Exercise 7: Find Repeated Words")
    print("=" * 60)
    
    pattern = r'\b(\w+)\s+\1\b'
    test_cases = [
        "the the cat",
        "hello hello world",
        "the cat sat",
        "Hello hello"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        matches = re.findall(pattern, text)
        if matches:
            print(f"✓ '{text}' -> Found: {matches}")
        else:
            print(f"✗ '{text}'")
    print()


def exercise_8_validate_username_strict():
    """Exercise 8: Validate Username (Stricter)"""
    print("=" * 60)
    print("Exercise 8: Validate Username (Stricter)")
    print("=" * 60)
    
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,19}$'
    test_cases = [
        "john_doe",
        "user123",
        "admin",
        "123user",
        "user_",
        "user-name"
    ]
    
    print(f"Pattern: {pattern}")
    for username in test_cases:
        match = re.match(pattern, username)
        result = "✓" if match else "✗"
        print(f"{result} '{username}'")
    print()


def exercise_9_simple_ip_address():
    """Exercise 9: Match IP Address (Simple)"""
    print("=" * 60)
    print("Exercise 9: Match IP Address (Simple)")
    print("=" * 60)
    
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    test_cases = [
        "192.168.1.1",
        "10.0.0.1",
        "256.1.1.1",
        "192.168.1",
        "192.168.1.1.1"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def exercise_10_remove_extra_spaces():
    """Exercise 10: Remove Extra Spaces"""
    print("=" * 60)
    print("Exercise 10: Remove Extra Spaces")
    print("=" * 60)
    
    pattern = r'\s{2,}'
    test_cases = [
        "hello    world",
        "text   with   spaces",
        "normal text"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        matches = re.findall(pattern, text)
        cleaned = re.sub(pattern, ' ', text)
        print(f"Original: '{text}'")
        print(f"  Found spaces: {matches}")
        print(f"  Cleaned: '{cleaned}'")
    print()


def main():
    """Run all basic exercises"""
    print("\n" + "=" * 60)
    print("BASIC REGEX EXERCISES - PYTHON SOLUTIONS")
    print("=" * 60 + "\n")
    
    exercise_1_match_numbers()
    exercise_2_detect_mobile_number()
    exercise_3_words_starting_with_a()
    exercise_4_valid_pin_code()
    exercise_5_extract_domain()
    exercise_6_time_format()
    exercise_7_repeated_words()
    exercise_8_validate_username_strict()
    exercise_9_simple_ip_address()
    exercise_10_remove_extra_spaces()
    
    print("=" * 60)
    print("All exercises completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

