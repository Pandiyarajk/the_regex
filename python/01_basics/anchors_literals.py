#!/usr/bin/env python3
"""
Anchors and Literal Matching Examples

Demonstrates:
- Start anchor (^)
- End anchor ($)
- Word boundaries (\b)
- Literal character matching
"""

import re


def example_start_anchor():
    """Demonstrate start anchor (^)"""
    print("=" * 60)
    print("Start Anchor (^)")
    print("=" * 60)
    
    pattern = r'^Hello'
    test_cases = [
        "Hello world",
        "Say Hello",
        "Hello",
        "hello world"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}' -> {bool(match)}")
    print()


def example_end_anchor():
    """Demonstrate end anchor ($)"""
    print("=" * 60)
    print("End Anchor ($)")
    print("=" * 60)
    
    pattern = r'world$'
    test_cases = [
        "Hello world",
        "world",
        "world hello",
        "Hello world!"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}' -> {bool(match)}")
    print()


def example_both_anchors():
    """Demonstrate both anchors for exact match"""
    print("=" * 60)
    print("Both Anchors (^ and $) - Exact Match")
    print("=" * 60)
    
    pattern = r'^Hello world$'
    test_cases = [
        "Hello world",
        "Hello world!",
        "Say Hello world",
        "Hello world and more"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.match(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}' -> {bool(match)}")
    print()


def example_word_boundary():
    """Demonstrate word boundaries (\b)"""
    print("=" * 60)
    print("Word Boundaries (\\b)")
    print("=" * 60)
    
    # Without word boundary
    pattern1 = r'cat'
    # With word boundary
    pattern2 = r'\bcat\b'
    
    text = "The cat sat on the category"
    
    matches1 = re.findall(pattern1, text)
    matches2 = re.findall(pattern2, text)
    
    print(f"Pattern without \\b: {pattern1}")
    print(f"Matches: {matches1}")
    print(f"\nPattern with \\b: {pattern2}")
    print(f"Matches: {matches2}")
    print()


def example_literal_characters():
    """Demonstrate literal character matching"""
    print("=" * 60)
    print("Literal Character Matching")
    print("=" * 60)
    
    # Dot as literal (escaped)
    pattern1 = r'example\.com'
    # Dot as meta character (matches any char)
    pattern2 = r'example.com'
    
    test_cases = [
        "example.com",
        "exampleXcom",
        "example.com/path"
    ]
    
    print(f"Pattern (escaped dot): {pattern1}")
    for text in test_cases:
        match = re.search(pattern1, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}' -> {bool(match)}")
    
    print(f"\nPattern (dot as meta): {pattern2}")
    for text in test_cases:
        match = re.search(pattern2, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}' -> {bool(match)}")
    print()


def example_escaping_special_chars():
    """Demonstrate escaping special characters"""
    print("=" * 60)
    print("Escaping Special Characters")
    print("=" * 60)
    
    special_chars = [
        (r'\.', "Literal dot"),
        (r'\*', "Literal asterisk"),
        (r'\+', "Literal plus"),
        (r'\?', "Literal question mark"),
        (r'\(', "Literal opening parenthesis"),
        (r'\)', "Literal closing parenthesis"),
        (r'\[', "Literal opening bracket"),
        (r'\]', "Literal closing bracket"),
        (r'\{', "Literal opening brace"),
        (r'\}', "Literal closing brace"),
        (r'\^', "Literal caret"),
        (r'\$', "Literal dollar"),
        (r'\|', "Literal pipe"),
        (r'\\', "Literal backslash"),
    ]
    
    print("Escaped special characters:")
    for pattern, description in special_chars:
        print(f"  {pattern:10} -> {description}")
    print()


def main():
    """Run all anchor and literal examples"""
    print("\n" + "=" * 60)
    print("ANCHORS AND LITERAL MATCHING - PYTHON EXAMPLES")
    print("=" * 60 + "\n")
    
    example_start_anchor()
    example_end_anchor()
    example_both_anchors()
    example_word_boundary()
    example_literal_characters()
    example_escaping_special_chars()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

