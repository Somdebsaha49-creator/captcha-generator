import random
import string
print('')
print('Hello, Welcome to my Captcha generator code, it will generate a new Captcha as long as you ask to resend a new Captcha')
print('')
print('Sending Captcha....')
print('')
i=1
while i>0:
    chars = string.ascii_letters + string.digits
    captcha = ''.join(random.choices(chars, k=6))
    print("Captcha is:- ", captcha)
    print('')
    c=int(input('Do you get a new Captcha ?..then press 1, else press 0 :- '))
    print('')
    if c==0:
        break
print('')