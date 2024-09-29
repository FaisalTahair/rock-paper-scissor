import random
import string
print("****WELCOME TO PASSWORD-GENERATOR****")
length=int(input("   Enter the length of Password : "))
pass_chars=string.ascii_letters+string.digits
password=''.join(random.choice(pass_chars) for el in range(length))
print("     Password :",password)
print("          Thankyou !!!!!")