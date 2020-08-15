import hashlib

s = input()
encoded_s = s.encode()
result = hashlib.sha256(encoded_s).hexdigest()
print(result)