import sys


def main():
    n = int(input())
    s = input().split()
    m = int(input())
    k = []
    for i in s:
        k.append(abs(m - int(i)))
    mi = min(k)
    out = k.index(mi)
    print(s[out])
    pass


if __name__ == '__main__':
    main()