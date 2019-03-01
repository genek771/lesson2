a = int(input("vash vozrast"))
def opred(age):
    if (age <= 7):
        print("sadik")
    elif (age > 7) and (age < 18):
        print("v shkolu")
    elif (age > 18) and (age < 25):
        print("v institute")
    else:
        print("truditsya")
opred(a)
    


def inp(str1, str2):
	if type(str1) == type(str2) == str:
		if str1 == str2:
			return 1
		if len(str1) > len(str2):
			return 2
		if str2 == "learn":
			return 3
	else:
		0

str1 = str(input("str1 "))
str2 = str(input("str2 "))

vivod = inp(str1, str2)
print(vivod)