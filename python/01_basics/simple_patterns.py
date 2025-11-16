#!/usr/bin/env python3
"""
Basic Regex Patterns - Simple Examples

This module demonstrates basic regex patterns including:
- Literal matching
- Meta characters
- Anchors
- Simple quantifiers
"""

import re


def example_1_match_3_letter_word():
    """Example 1: Match a 3-letter word"""
    print("=" * 60)
    print("Example 1: Match a 3-letter word")
    print("=" * 60)
    
    pattern = r'\b[a-zA-Z]{3}\b'
    text = "The cat sat on the mat"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")
    print()


def example_2_match_only_digits():
    """Example 2: Match only digits"""
    print("=" * 60)
    print("Example 2: Match only digits")
    print("=" * 60)
    
    pattern = r'^\d+$'
    test_cases = ["123", "0", "999999", "123abc", "12 34", "12.34"]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.match(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}' -> {bool(match)}")
    print()


def example_3_validate_username():
    """Example 3: Validate a username"""
    print("=" * 60)
    print("Example 3: Validate a username")
    print("=" * 60)
    
    pattern = r'^[a-zA-Z0-9_]{3,16}$'
    usernames = ["john_doe", "user123", "admin", "ab", "this_username_is_too_long", "user-name"]
    
    print(f"Pattern: {pattern}")
    for username in usernames:
        match = re.match(pattern, username)
        result = "✓" if match else "✗"
        print(f"{result} '{username}' -> {bool(match)}")
    print()


def example_4_find_spaces_tabs():
    """Example 4: Find spaces and tabs"""
    print("=" * 60)
    print("Example 4: Find spaces and tabs")
    print("=" * 60)
    
    pattern = r'[\s\t]+'
    text = "hello    world\tand   more"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")
    
    # Replace multiple spaces with single space
    cleaned = re.sub(pattern, ' ', text)
    print(f"Cleaned: {cleaned}")
    print()


def example_5_words_starting_with_a():
    """Example 5: Match words starting with 'A'"""
    print("=" * 60)
    print("Example 5: Match words starting with 'A'")
    print("=" * 60)
    
    pattern = r'\b[Aa]\w+'
    text = "Apple and application are awesome"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")
    
    # Case-insensitive version
    pattern_ci = r'\ba\w+'
    matches_ci = re.findall(pattern_ci, text, re.IGNORECASE)
    print(f"\nCase-insensitive pattern: {pattern_ci}")
    print(f"Matches: {matches_ci}")
    print()


def example_6_phone_number_format():
    """Example 6: Match phone number format (Simple)"""
    print("=" * 60)
    print("Example 6: Match phone number format")
    print("=" * 60)
    
    pattern = r'\d{3}-\d{3}-\d{4}'
    text = "Call me at 123-456-7890 or 555-123-4567"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")
    print()


def example_7_basic_email():
    """Example 7: Match email (Basic Pattern)"""
    print("=" * 60)
    print("Example 7: Match email (Basic Pattern)")
    print("=" * 60)
    
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    text = "Contact admin@example.com or support@company.org"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")
    print()


def main():
    """Run all basic examples"""
    print("\n" + "=" * 60)
    print("BASIC REGEX PATTERNS - PYTHON EXAMPLES")
    print("=" * 60 + "\n")
    
    example_1_match_3_letter_word()
    example_2_match_only_digits()
    example_3_validate_username()
    example_4_find_spaces_tabs()
    example_5_words_starting_with_a()
    example_6_phone_number_format()
    example_7_basic_email()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

