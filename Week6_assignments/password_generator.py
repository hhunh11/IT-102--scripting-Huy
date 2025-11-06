from passlib.hash import sha512_crypt
import string,random,secrets
def yes_or_no(mess:str)-> bool:
    while(True):   
        ans=input(f'{mess} yes or no (y/n): ').strip().lower()
        if ans in ("y","yes"):
            return True
        if ans in ("n","no"):
            return False
        print("please type yes or no (y/n): ")


count_passwords=input("how many passwords to generate? (default 5)?: ").strip()
if count_passwords.isdigit() and int(count_passwords)>0:
    count_passwords=int(count_passwords)
else: count_passwords=5

len_pw=input("How long of each password (min=8, default=12)? ").strip()
if len_pw.isdigit() and int(len_pw)>=8:
    len_pw=int(len_pw)
else: len_pw=12


upper_included=yes_or_no("include Upper Letters ? ")
lower_included=yes_or_no("include Lower Letters ? ")
digits_included=yes_or_no("include Digits ? ")
special_included=yes_or_no("include Special Characters ? ")


if not any((upper_included,lower_included,digits_included,special_included)):
    print("-----------------------------")
    print("No classes wewe chosen\n automatically lower class + digits !")
    lower_included=True
    digits_included=True

print("-----------------------------")

pool=""
if upper_included:
    pool+=string.ascii_uppercase
if lower_included:
    pool+=string.ascii_lowercase
if digits_included:
    pool+=string.digits
if special_included:
    pool+="!@#$%^&*()_+=-][\|{}];':,./?><"


for a in range(count_passwords):
    chars =[]
    if upper_included:
        chars.append(secrets.choice(string.ascii_uppercase))
    if lower_included:
        chars.append(secrets.choice(string.ascii_lowercase))
    if special_included:
        chars.append(secrets.choice("!@#$%^&*()_+=-][\|{}];':,./?><"))
    if digits_included:
        chars.append(secrets.choice(string.digits))
    while(len(chars)<len_pw):
        chars.append(secrets.choice(pool))

    for i in range(len(chars)-1,0,-1):
        j=secrets.randbelow(i+1)
        chars[j],chars[i]=chars[i],chars[j]
    password="".join(chars)
    hashed_pw=sha512_crypt.hash(password)
    print(f'Password: {password}')
    print(f'hashed password: {hashed_pw}')

