#!/usr/bin/env python3
"""
Lookaheads and Lookbehinds - Intermediate Examples

Demonstrates:
- Positive lookahead (?=)
- Negative lookahead (?!)
- Positive lookbehind (?<=)
- Negative lookbehind (?<!)
"""

import re


def example_positive_lookahead():
    """Positive lookahead"""
    print("=" * 60)
    print("Positive Lookahead (?=)")
    print("=" * 60)
    
    # Match word followed by digit
    pattern = r'\w+(?=\d)'
    text = "password123"
    
    match = re.search(pattern, text)
    if match:
        print(f"Pattern: {pattern}")
        print(f"Text: {text}")
        print(f"Match: '{match.group()}' (followed by digit)")
    print()


def example_negative_lookahead():
    """Negative lookahead"""
    print("=" * 60)
    print("Negative Lookahead (?!)")
    print("=" * 60)
    
    # Word not followed by 'ing'
    pattern = r'\w+(?!ing\b)'
    text = "running jumping walk"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches (not followed by 'ing'): {matches}")
    print()


def example_positive_lookbehind():
    """Positive lookbehind"""
    print("=" * 60)
    print("Positive Lookbehind (?<=)")
    print("=" * 60)
    
    # Extract amount after dollar sign
    pattern = r'(?<=\$)\d+'
    text = "Price is $100 and $50"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches (after $): {matches}")
    print()


def example_negative_lookbehind():
    """Negative lookbehind"""
    print("=" * 60)
    print("Negative Lookbehind (?<!)")
    print("=" * 60)
    
    # Number not preceded by dollar sign
    pattern = r'(?<!\$)\d+'
    text = "Price is $100 and 50 dollars"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches (not preceded by $): {matches}")
    print()


def example_validate_password():
    """Validate password with lookaheads"""
    print("=" * 60)
    print("Validate Password with Lookaheads")
    print("=" * 60)
    
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
    test_cases = [
        "Password123",
        "password123",
        "PASSWORD123",
        "Pass123"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.match(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def example_extract_quoted_text():
    """Extract text between quotes"""
    print("=" * 60)
    print("Extract Text Between Quotes")
    print("=" * 60)
    
    pattern = r'(?<=")[^"]+(?=")'
    text = 'He said "hello world" and left'
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")
    print()


def example_combining_lookarounds():
    """Combining lookarounds"""
    print("=" * 60)
    print("Combining Lookarounds")
    print("=" * 60)
    
    # Extract number between $ and .
    pattern = r'(?<=\$)\d+(?=\.)'
    text = "Price is $100.50"
    
    match = re.search(pattern, text)
    if match:
        print(f"Pattern: {pattern}")
        print(f"Text: {text}")
        print(f"Match: '{match.group()}' (between $ and .)")
    print()


def main():
    """Run all lookaround examples"""
    print("\n" + "=" * 60)
    print("LOOKAHEADS AND LOOKBEHINDS - PYTHON EXAMPLES")
    print("=" * 60 + "\n")
    
    example_positive_lookahead()
    example_negative_lookahead()
    example_positive_lookbehind()
    example_negative_lookbehind()
    example_validate_password()
    example_extract_quoted_text()
    example_combining_lookarounds()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

