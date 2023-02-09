import time

def main():
    num = float(input(">"))
    print(num)
    while num != 1:
        if (num % 2) == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        print(num)
        #time.sleep(.15)
main()
