x = (int(input("Enter your number 1 : ")))
y = (int(input("Enter your number 2 : ")))

max = max(x,y)

while (True):
    if ( max%x == 0 and max%y == 0 ):
        break
    max = max + 1

print(f"yor Lcm of {x} and {y} is {max}")