# Project: Email Validator CLI

Build a command-line email validator that checks if an email address is valid and provides detailed feedback.

## Project Overview

Create a CLI tool that:
- Validates email addresses using regex
- Provides detailed validation feedback
- Supports both Python and JavaScript implementations
- Can be used interactively or with command-line arguments

## Requirements

### Basic Validation
- Local part (before @): letters, digits, dots, underscores, hyphens, plus signs
- @ symbol required
- Domain name: letters, digits, dots, hyphens
- TLD: 2+ letters
- Overall format validation

### Advanced Validation
- Check for common typos
- Validate domain structure
- Provide specific error messages

## Implementation

### Python Version

**File: `email_validator.py`**

```python
#!/usr/bin/env python3
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
```

### JavaScript Version

**File: `email_validator.js`**

```javascript
#!/usr/bin/env node

function validateEmail(email) {
    const result = {
        valid: false,
        email: email,
        errors: [],
        warnings: []
    };
    
    // Basic pattern
    const pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    
    // Check basic format
    if (!pattern.test(email)) {
        result.errors.push("Invalid email format");
        return result;
    }
    
    // Split into local and domain parts
    const [localPart, domain] = email.split('@');
    
    // Check local part
    if (localPart.length > 64) {
        result.errors.push("Local part too long (max 64 characters)");
    }
    
    if (localPart.startsWith('.') || localPart.endsWith('.')) {
        result.errors.push("Local part cannot start or end with dot");
    }
    
    if (localPart.includes('..')) {
        result.errors.push("Local part cannot contain consecutive dots");
    }
    
    // Check domain
    if (domain.length > 255) {
        result.errors.push("Domain too long (max 255 characters)");
    }
    
    const domainParts = domain.split('.');
    if (domainParts.length < 2) {
        result.errors.push("Domain must have at least one dot");
    }
    
    const tld = domainParts[domainParts.length - 1];
    if (tld.length < 2) {
        result.errors.push("TLD must be at least 2 characters");
    }
    
    // Check for common typos
    if (domain.toLowerCase().includes('gmial')) {
        result.warnings.push("Did you mean 'gmail'?");
    }
    
    if (domain.toLowerCase().includes('yahooo')) {
        result.warnings.push("Did you mean 'yahoo'?");
    }
    
    // Final validation
    if (result.errors.length === 0) {
        result.valid = true;
    }
    
    return result;
}

function printResult(result) {
    const { email, valid, errors, warnings } = result;
    
    console.log('\n' + '='.repeat(50));
    console.log(`Email: ${email}`);
    console.log(`Status: ${valid ? '✓ VALID' : '✗ INVALID'}`);
    console.log('='.repeat(50));
    
    if (errors.length > 0) {
        console.log('\nErrors:');
        errors.forEach(error => console.log(`  ✗ ${error}`));
    }
    
    if (warnings.length > 0) {
        console.log('\nWarnings:');
        warnings.forEach(warning => console.log(`  ⚠ ${warning}`));
    }
    
    if (valid) {
        console.log('\n✓ Email address is valid!');
    }
}

// Main function
function main() {
    const args = process.argv.slice(2);
    
    if (args.length > 0) {
        // Command-line argument provided
        const email = args[0];
        const result = validateEmail(email);
        printResult(result);
    } else {
        // Interactive mode
        console.log("Email Validator CLI");
        console.log("Enter email addresses to validate (or 'quit' to exit)\n");
        
        const readline = require('readline');
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        
        function prompt() {
            rl.question('Email: ', (email) => {
                const trimmed = email.trim();
                
                if (trimmed.toLowerCase() === 'quit' || 
                    trimmed.toLowerCase() === 'exit' || 
                    trimmed === 'q') {
                    console.log("Goodbye!");
                    rl.close();
                    return;
                }
                
                if (trimmed) {
                    const result = validateEmail(trimmed);
                    printResult(result);
                    console.log();
                }
                
                prompt();
            });
        }
        
        prompt();
    }
}

if (require.main === module) {
    main();
}
```

## Usage Examples

### Python

```bash
# Interactive mode
python email_validator.py

# Command-line mode
python email_validator.py user@example.com
python email_validator.py invalid.email
```

### JavaScript

```bash
# Make executable (Unix/Mac)
chmod +x email_validator.js

# Interactive mode
node email_validator.js

# Command-line mode
node email_validator.js user@example.com
node email_validator.js invalid.email
```

## Testing

Test with various email formats:

```bash
# Valid emails
user@example.com
john.doe@company.co.uk
user+tag@example.org

# Invalid emails
invalid.email
@example.com
user@.com
user@example
user..name@example.com
```

## Extensions

1. **Add more validation rules**
   - Check for reserved domains
   - Validate MX records (requires DNS lookup)
   - Check for disposable email domains

2. **Batch processing**
   - Read emails from file
   - Validate multiple emails
   - Export results to CSV

3. **Enhanced feedback**
   - Suggest corrections
   - Provide regex explanation
   - Show which part failed

## Key Learning Points

- Using regex for email validation
- Combining regex with additional checks
- Building CLI tools
- Error handling and user feedback
- Pattern testing and refinement

---

**Next Project:** [project-log-parser.md](project-log-parser.md)

