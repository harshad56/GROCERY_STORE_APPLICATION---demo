print("welcome to love calculator")
name1 = input("what is your name? \n")
name2 = input("what is their name? \n")


combined_string = name1+name2

lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t+r+u+e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l+o+v+e

love_no = int(str(true)+str(love))

if love_no == 0 or love_no <= 10 or love_no >= 90:
    print(f" your love score is {love_no} like a melodie")

elif love_no > 20 and love_no <= 50:
    print(f"your love score is {love_no} like a sunshine")

else:
    print(f"your love score is {love_no} means no love")
