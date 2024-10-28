# Divisible by 3 and 5
x  = int(input("Enter x: "))

# range starts from (1 to x+1) to include 1 and number entered as x
for i in range(1,x+1):
    
    # check if number i is divisible by both numbers 3 & 5 where remainder is zero
    if i%3 == 0 and i%5 == 0:
        print(i)