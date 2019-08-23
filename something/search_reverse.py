line = ''
deep = 1

for _ in range(1000):
    line += '-'


def pal(number):
    if number == number[::-1]:
        return True
    else:
        return False


a = input()

while True:
    sm = int(a) + int(a[::-1])
    if not pal(str(sm)):
        print("[Fail - {}] ".format(deep) + str(sm))
        a = str(sm)
    else:
        print(line)
        print("[True] " + str(sm))
        print("Number of attempts: " + str(deep))
        exit()
    deep += 1
    # if deep > 10000:
    #     print("CRITICAL FOR YOUR COMPUTER ERROR")
    #     print("LENGTH OF LAST NUMBER = {}".format(len(str(sm))))
    #     exit()