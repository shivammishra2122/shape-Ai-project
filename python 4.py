import hashlib
print("Md5 = "+hashlib.md5((input("String for Md5 = ")).encode()).hexdigest() + "\nSHA1 = "+hashlib.sha1((input("String for SHA1 = ")).encode()).hexdigest() + "\nSHA256 = "+hashlib.sha256((input("String for SHA256 = ")).encode()).hexdigest())