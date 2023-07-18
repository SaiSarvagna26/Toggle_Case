string=input()
upper_str=""
lower_str=""
for i in string:
    if i.isupper():
        lower_str+=i.lower()
    else:
        upper_str+=i.upper()
print(lower_str+upper_str)