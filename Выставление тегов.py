import sys


def main():
    n = int(input())
    t = []
    if n > 2:
        t.append(1)
        t.append(1)
        for i in range(2, n):
            t.append(int(t[i-2] + t[i-1]))
        print(sum(t))
    elif n == 2:
        print(2)
    elif n == 1:
        print(1)
    elif n == 0:
        print(0)
    pass


if __name__ == '__main__':
    main()