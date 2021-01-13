import simplecrypt

with open("encrypted.bin", "rb") as in_data:
    encrypted = in_data.read()

with open('passwords.txt') as in_pw:
    pw = [_.strip() for _ in in_pw]

for p in pw:
    try:
        print(f"step {pw.index(p)} from {len(pw)}")
        msg = simplecrypt.decrypt(p, encrypted)
    except:
        print(f"password {p} is incorrect")
    else:
        print(f"password {p} is correct")
        print("Encrypted message is:\n", msg.decode('utf-8'), '\n')
