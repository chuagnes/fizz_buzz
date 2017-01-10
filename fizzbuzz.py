import sys 

if len(sys.argv) > 1:
    n = sys.argv[1]
else:
    n = input("What number would you like Fizzbuzz to stop at?")

try:
    n = int(n)
except:
    print("Input isn't an integer.")

print("Fizz buzz counting up to {0}".format(n))
for num in range(1,n+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)



    