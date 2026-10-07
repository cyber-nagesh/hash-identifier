# Hash Identifier

A lightweight Python CLI that identifies likely hash algorithms from a hash's structure (length, character set, and known prefixes). Useful as a first step in password auditing, digital forensics, and incident response.

> This tool is a **classifier, not a cracker**. It only suggests which algorithm probably produced a hash.

## Features
- Identifies MD5/NTLM, SHA-1, SHA-256, SHA-512, bcrypt, SHA-512crypt, SHA-256crypt, MD5crypt, and Argon2
- Single-hash and batch mode (one hash per line from a file)
- Human-readable and JSON output (easy to pipe into other tools)
- Handles uppercase hex, extra whitespace, and invalid input
- Unit tested with pytest

## Installation
```bash
git clone https://github.com/cyber-nagesh/hash-identifier.git
cd hash-identifier
python3 -m venv venv
source venv/bin/activate
pip install pytest   # only needed to run tests
```

## Usage
```bash
# Single hash
python3 hash_identifier.py 5d41402abc4b2a76b9719d911017c592

# Batch mode
python3 hash_identifier.py --file hashes.txt

# JSON output
python3 hash_identifier.py --json 5d41402abc4b2a76b9719d911017c592
```

### Example output
```
5d41402abc4b2a76b9719d911017c592
  -> MD5 / NTLM
```

## Limitations
- Many algorithms share the same output length (for example, 32 hex characters could be MD5, NTLM, or MD4), so results are **candidates, not proof**.
- Detection is rule-based; it does not verify a hash against any plaintext.

## Running tests
```bash
python3 -m pytest -v
```

## Roadmap
- [ ] Hashcat mode numbers and John the Ripper formats in the output
- [ ] Rules loaded from an external JSON file
- [ ] More hash types (NTLM variants, MySQL, Cisco, etc.)

## Skills demonstrated
Python, CLI design (argparse), regex, unit testing (pytest), Git, secure coding basics, digital forensics fundamentals.

## Disclaimer

This project was created by a final-year B.Sc. Cyber & Digital Science student for **educational and learning purposes** as part of my cybersecurity portfolio.

- The tool only **identifies** the likely type of a hash. It does not crack, reverse, or recover passwords.
- Use it only on hashes you own or have **explicit written permission** to analyze, such as your own lab, CTF challenges, or authorized security assessments.
- Do not use it for unauthorized access, or for any illegal or unethical activity. Misuse is solely the responsibility of the user.
- The software is provided "as is", without warranty of any kind. The author is not liable for any damage or misuse resulting from its use.
- Results are **candidates, not proof**. Always verify with additional context.

## Author

**Nagesh Bhure**, final-year B.Sc. Cyber & Digital Science student, aspiring SOC analyst / blue team professional.
[LinkedIn](https://linkedin.com/in/nagesh-bhure-a650793a3) | [GitHub](https://github.com/cyber-nagesh)

## License

Released under the MIT License. See the `LICENSE` file for details.
