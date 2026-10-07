import argparse
import json
import re
import sys

RULES = [
    ("bcrypt", r"^\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}$"),
    ("SHA-512crypt", r"^\$6\$.+"),
    ("SHA-256crypt", r"^\$5\$.+"),
    ("MD5crypt", r"^\$1\$.+"),
    ("Argon2", r"^\$argon2(id|i|d)\$.+"),
    ("SHA-512", r"^[a-fA-F0-9]{128}$"),
    ("SHA-256", r"^[a-fA-F0-9]{64}$"),
    ("SHA-1", r"^[a-fA-F0-9]{40}$"),
    ("MD5 / NTLM", r"^[a-fA-F0-9]{32}$"),
]


def identify(hash_str):
    hash_str = hash_str.strip()
    return [name for name, pattern in RULES if re.match(pattern, hash_str)]


def read_hashes(path):
    try:
        with open(path) as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        sys.exit(f"Error: file not found: {path}")


def main():
    parser = argparse.ArgumentParser(
        description="Identify hash types from their structure."
    )
    parser.add_argument("hash", nargs="?", help="a single hash to identify")
    parser.add_argument("-f", "--file", help="file with one hash per line")
    parser.add_argument("--json", action="store_true", help="output as JSON")
    args = parser.parse_args()

    if not args.hash and not args.file:
        parser.error("provide a hash or use --file")

    hashes = read_hashes(args.file) if args.file else [args.hash]
    results = [{"hash": h, "matches": identify(h)} for h in hashes]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            matches = ", ".join(r["matches"]) or "No match found"
            print(f"{r['hash']}\n  -> {matches}\n")


if __name__ == "__main__":
    main()
