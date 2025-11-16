#!/usr/bin/env python3
"""
Character Classes - Intermediate Examples

Demonstrates:
- Basic character classes [abc]
- Character ranges [a-z]
- Negated character classes [^abc]
- Predefined classes (\d, \w, \s)
"""

import re


def example_basic_character_classes():
    """Basic character classes"""
    print("=" * 60)
    print("Basic Character Classes")
    print("=" * 60)
    
    text = "hello world"
    
    # Match vowels
    pattern1 = r'[aeiou]'
    matches1 = re.findall(pattern1, text)
    print(f"Pattern: {pattern1}")
    print(f"Text: {text}")
    print(f"Matches (vowels): {matches1}")
    
    # Match digits
    text2 = "abc123def456"
    pattern2 = r'[0-9]'
    matches2 = re.findall(pattern2, text2)
    print(f"\nPattern: {pattern2}")
    print(f"Text: {text2}")
    print(f"Matches (digits): {matches2}")
    print()


def example_character_ranges():
    """Character ranges"""
    print("=" * 60)
    print("Character Ranges")
    print("=" * 60)
    
    text = "Hello123World"
    
    patterns = [
        (r'[a-z]', "Lowercase letters"),
        (r'[A-Z]', "Uppercase letters"),
        (r'[0-9]', "Digits"),
        (r'[a-zA-Z]', "All letters"),
        (r'[a-z0-9]', "Lowercase and digits")
    ]
    
    for pattern, description in patterns:
        matches = re.findall(pattern, text)
        print(f"{pattern:15} ({description:25}) -> {matches}")
    print()


def example_negated_classes():
    """Negated character classes"""
    print("=" * 60)
    print("Negated Character Classes")
    print("=" * 60)
    
    text = "hello123"
    
    patterns = [
        (r'[^aeiou]', "Non-vowels"),
        (r'[^0-9]', "Non-digits"),
        (r'[^a-z]', "Non-lowercase")
    ]
    
    for pattern, description in patterns:
        matches = re.findall(pattern, text)
        print(f"{pattern:15} ({description:20}) -> {matches}")
    print()


def example_predefined_classes():
    """Predefined character classes"""
    print("=" * 60)
    print("Predefined Character Classes")
    print("=" * 60)
    
    text = "Hello_World 123!"
    
    patterns = [
        (r'\d', "Digits"),
        (r'\D', "Non-digits"),
        (r'\w', "Word characters"),
        (r'\W', "Non-word characters"),
        (r'\s', "Whitespace"),
        (r'\S', "Non-whitespace")
    ]
    
    for pattern, description in patterns:
        matches = re.findall(pattern, text)
        print(f"{pattern:5} ({description:20}) -> {matches}")
    print()


def example_hex_color_code():
    """Match hex color code"""
    print("=" * 60)
    print("Example: Hex Color Code")
    print("=" * 60)
    
    pattern = r'#[0-9a-fA-F]{6}'
    test_cases = [
        "#FF5733",
        "#00ff00",
        "#GGG",
        "#123456"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.match(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def example_extract_words():
    """Extract words (letters only)"""
    print("=" * 60)
    print("Example: Extract Words (Letters Only)")
    print("=" * 60)
    
    pattern = r'\b[a-zA-Z]+\b'
    text = "Hello123 world test456"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")
    print()


def example_valid_filename():
    """Match valid filename characters"""
    print("=" * 60)
    print("Example: Valid Filename Characters")
    print("=" * 60)
    
    pattern = r'^[a-zA-Z0-9._-]+$'
    test_cases = [
        "file.txt",
        "my-file_123",
        "file name",
        "file/name"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.match(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def main():
    """Run all character class examples"""
    print("\n" + "=" * 60)
    print("CHARACTER CLASSES - PYTHON EXAMPLES")
    print("=" * 60 + "\n")
    
    example_basic_character_classes()
    example_character_ranges()
    example_negated_classes()
    example_predefined_classes()
    example_hex_color_code()
    example_extract_words()
    example_valid_filename()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

