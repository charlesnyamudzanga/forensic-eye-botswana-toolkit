#!/usr/bin/env python3
"""
hash_verify.py — Forensic Eye Botswana Toolkit
File hash verification for digital evidence integrity.
Author: Forensic Eye Botswana (Pty) Ltd
License: MIT
"""

import hashlib
import argparse
import os
import sys
from datetime import datetime


def compute_hashes(filepath):
    if not os.path.exists(filepath):
        print(f"[ERROR] File not found: {filepath}")
        sys.exit(1)

    hashes = {
        "MD5": hashlib.md5(),
        "SHA1": hashlib.sha1(),
        "SHA256": hashlib.sha256(),
    }

    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            for h in hashes.values():
                h.update(chunk)

    return {name: h.hexdigest() for name, h in hashes.items()}


def print_report(filepath, hashes, expected=None):
    filesize = os.path.getsize(filepath)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    print("=" * 60)
    print("  FORENSIC EYE BOTSWANA — HASH VERIFICATION REPORT")
    print("=" * 60)
    print(f"  File     : {os.path.abspath(filepath)}")
    print(f"  Size     : {filesize:,} bytes")
    print(f"  DateTime : {timestamp}")
    print("-" * 60)
    for name, value in hashes.items():
        print(f"  {name:<8}: {value}")
    print("-" * 60)

    if expected:
        expected = expected.strip().lower()
        match = any(v == expected for v in hashes.values())
        if match:
            print("  VERIFICATION : ✅ MATCH — Evidence integrity confirmed.")
        else:
            print("  VERIFICATION : ❌ MISMATCH — File may be altered.")
    else:
        print("  VERIFICATION : No expected hash provided.")

    print("=" * 60)
    print("  Forensic Eye Botswana (Pty) Ltd | Gaborone, Botswana 🇧🇼")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Forensic Eye Botswana — File Hash Verification Tool"
    )
    parser.add_argument("filepath", help="Path to the file to verify")
    parser.add_argument("--expected", help="Expected hash to verify against", default=None)
    args = parser.parse_args()

    hashes = compute_hashes(args.filepath)
    print_report(args.filepath, hashes, args.expected)


if __name__ == "__main__":
    main()
