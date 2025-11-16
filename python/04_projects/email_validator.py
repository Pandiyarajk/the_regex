#!/usr/bin/env python3
"""
Email Validator CLI - Project Implementation

Validates email addresses using regex and provides detailed feedback.
"""

import re
import sys


def validate_email(email):
    """
    Validate email address and return result with details.
    
    Returns:
        dict: {
            'valid': bool,
            'email': str,
            'errors': list,
            'warnings': list
        }
    """
    result = {
        'valid': False,
        'email': email,
        'errors': [],
        'warnings': []
    }
    
    # Basic pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check basic format
    if not re.match(pattern, email):
        result['errors'].append("Invalid email format")
        return result
    
    # Split into local and domain parts
    local_part, domain = email.split('@', 1)
    
    # Check local part
    if len(local_part) > 64:
        result['errors'].append("Local part too long (max 64 characters)")
    
    if local_part.startswith('.') or local_part.endswith('.'):
        result['errors'].append("Local part cannot start or end with dot")
    
    if '..' in local_part:
        result['errors'].append("Local part cannot contain consecutive dots")
    
    # Check domain
    if len(domain) > 255:
        result['errors'].append("Domain too long (max 255 characters)")
    
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        result['errors'].append("Domain must have at least one dot")
    
    tld = domain_parts[-1]
    if len(tld) < 2:
        result['errors'].append("TLD must be at least 2 characters")
    
    # Check for common typos
    if 'gmial' in domain.lower():
        result['warnings'].append("Did you mean 'gmail'?")
    
    if 'yahooo' in domain.lower():
        result['warnings'].append("Did you mean 'yahoo'?")
    
    # Final validation
    if not result['errors']:
        result['valid'] = True
    
    return result


def print_result(result):
    """Print validation result in a formatted way."""
    email = result['email']
    valid = result['valid']
    
    print(f"\n{'='*50}")
    print(f"Email: {email}")
    print(f"Status: {'✓ VALID' if valid else '✗ INVALID'}")
    print(f"{'='*50}")
    
    if result['errors']:
        print("\nErrors:")
        for error in result['errors']:
            print(f"  ✗ {error}")
    
    if result['warnings']:
        print("\nWarnings:")
        for warning in result['warnings']:
            print(f"  ⚠ {warning}")
    
    if valid:
        print("\n✓ Email address is valid!")


def main():
    """Main function for CLI usage."""
    if len(sys.argv) > 1:
        # Command-line argument provided
        email = sys.argv[1]
        result = validate_email(email)
        print_result(result)
    else:
        # Interactive mode
        print("Email Validator CLI")
        print("Enter email addresses to validate (or 'quit' to exit)\n")
        
        while True:
            email = input("Email: ").strip()
            
            if email.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not email:
                continue
            
            result = validate_email(email)
            print_result(result)
            print()


if __name__ == "__main__":
    main()

