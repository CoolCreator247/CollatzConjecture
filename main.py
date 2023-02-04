import time

def collatz(num):
    while True:
        if (num % 2) == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        print(num)
        time.sleep(.1)
        if num == 1:
            quit()
#add the starting number in the function
collatz(10)
