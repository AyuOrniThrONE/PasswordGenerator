import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWZYZ"
NUMBER="0123456789"
symbols="[]{}#@!~$%^&*()_-><"
all=lower+upper+NUMBER+symbols
length=9
password="".join(random.sample(all,length))
print("Your password is :",password)
