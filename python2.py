import hashlib
x=input("String = ")
print("Md5 = "+hashlib.md5((x).encode()).hexdigest() + "\nSHA1 = "+hashlib.sha1((x).encode()).hexdigest() + "\nSHA256 = "+hashlib.sha256((x).encode()).hexdigest())