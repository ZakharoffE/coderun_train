import sys


def main():
    x = [int(i) for i in input().split()]
    m1 = m2 = m3 = -10**5 - 1
    n1 = n2 = 10**5 + 1
    for i in x:
        if i > m1:
            m1, m2, m3 = i, m1, m2
        elif i > m2:
            m2, m3 = i, m2
        elif i > m3:
            m3 = i
        if i < n1:
            n1, n2 = i, n1
        elif i < n2:
            n2 = i
            
    if m1*m2*m3 > m1*n1*n2:
        print(m1,m2,m3)
    else:
        print(m1,n1,n2)
    pass


if __name__ == '__main__':
    main()