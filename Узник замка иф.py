import sys


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a <= d  and  b <= e or b <= d and a <= e or c <= d and b <= e or b <= d and c <= e or a <= d and c <= e or c <= d and a <= e:
        print('YES')
    else:
        print('NO')
    pass


if __name__ == '__main__':
    main()