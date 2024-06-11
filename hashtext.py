import hashlib

type_f_hash = str(input("Enter type of Hash to crack: "))
path_t_file = str(input("Enter path to file: "))
hash_t_crack = str(input("Enter the hash value: "))

with open(path_t_file, "r") as file:
    for password in file.readlines():
        if type_f_hash == "md5":
            hash_crack = hashlib.md5(password.strip().encode()).hexdigest()
            if hash_crack == hash_t_crack:
                print('md5 password found: ' + password.strip())
                exit(0)
        elif type_f_hash == "sha256":
            hash_crack = hashlib.sha256(password.strip().encode()).hexdigest()
            if hash_crack == hash_t_crack:
                print('sha256 password found: ' + password.strip())
                exit(0)
        elif type_f_hash == "sha1":
            hash_crack = hashlib.sha1(password.strip().encode()).hexdigest()
            if hash_crack == hash_t_crack:
                print('sha1 password found: ' + password.strip())
                exit(0)
        elif type_f_hash == "sha3_256":
            hash_crack = hashlib.sha3_256(password.strip().encode()).hexdigest()
            if hash_crack == hash_t_crack:
                print('sha3_256 password found: ' + password.strip())
                exit(0)
        