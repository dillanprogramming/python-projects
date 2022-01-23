import zipfile, random

charset = ("abcdefghijklmnopqrstuvwxyz")

def get_pwd(ZP,LENGHT):
    file = zipfile.ZipFile(ZP, 'r')
    print("Zipcracker v.1 by D####n and T####s")
    print("Cracking...")
    while True:
        pswd = ""
        for a in range(LENGHT):
            pswd += random.choice(charset)
        try:
            file.extractall(pwd = bytes(pswd, 'utf-8'))
            return pswd 
            break
        except:
            pass

fname = str(input("Filename: "))
lenght = int(input("Lenght: "))
print("Password is: "+get_pwd(fname,lenght))