#!/usr/bin/python3
import hashlib

mystring = str(input("Enter String to hash: "))

print(f"MD5 hash of your string is: {hashlib.md5(mystring.encode()).hexdigest()}")
print(f"SHA1 hash of your string is: {hashlib.sha1(mystring.encode()).hexdigest()}")
print(f"SHA256 hash of your string is: {hashlib.sha256(mystring.encode()).hexdigest()}")