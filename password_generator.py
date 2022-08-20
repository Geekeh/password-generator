from random import randint
import time
long = input("You long do you want your password? ")
amount = input("How many passwords do you want? ")
long = (int(long))
amount = (int(amount))

def amount_of_characters(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)

for x in range(amount): 
    print(amount_of_characters(long))
time.sleep(60)
