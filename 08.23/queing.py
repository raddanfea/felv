front = 0
rear = -1
maxi = 5
a = [0] * maxi


def enq():
    global rear
    if rear == maxi - 1:
        print("Overflow")
    else:
        ele = int(input("Ele:\t"))
        rear += 1
        a[rear] = ele


def deq():
    global front
    if front > rear:
        print("Underflow")
    else:
        print("DEL:\t", a[front])
        a[front] = 0
        front += 1


def display():
    if front > rear:
        print("Empty")
    else:
        for i in range(front, rear + 1):
            print(str(a[i]).center(5), end=">".center(5))
        print()


def main():
    while True:
        print('1 ENQ \t 2 DEQ \t 3 DISP \t 4 EXIT')
        ch = int(input("Choice:\t"))
        match ch:
            case 1:
                enq()
            case 2:
                deq()
            case 3:
                display()
            case 4:
                break


if __name__ == '__main__':
    main()
