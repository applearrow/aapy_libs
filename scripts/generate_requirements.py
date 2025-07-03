#!/usr/bin/env python3
"""
Script to generate requirements.txt from Poetry dependencies.
This is useful when working with uv or pip without Poetry.
"""
import subprocess
import sys

def main():
    print("Generating requirements.txt from Poetry dependencies...")
    try:
        subprocess.run(
            ["poetry", "export", "--format", "requirements.txt", "--output", "requirements.txt", "--without-hashes"], 
            check=True
        )
        print("✅ requirements.txt generated successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to generate requirements.txt: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
