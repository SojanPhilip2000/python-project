# 1
num1 = 5
num2 = 0

try:
    print(num1 / num2)
except:
    print("error occured")

# 2
num1 = 5
num2 = 0

try:
    print(num1 / num2)
except Exception as e:
    print(e)
