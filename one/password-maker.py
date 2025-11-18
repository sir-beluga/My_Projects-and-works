# making a password maker where first and last letter are only shown but remaining are *

password=input("enter your paassword :")
print("-"*70)
step1=len(password)-1
step2=password[0]+"x"*step1+password[-1]
print(step2.center(70))
print("-"*70)