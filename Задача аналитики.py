import sys


def main():
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    discr = b ** 2 - 4 * a * c
    if discr < 0:
        print(0)
    elif discr == 0:
        x = (-b)/ (2 * a)
        print(1)
        print(x)
    if discr > 0:
        s = []
        x1 = (-b + discr ** 0.5 )/ (2 * a)
        x2 = (-b - discr ** 0.5 )/ (2 * a)
        print(2)
        if x1 > x2:
            s.append(x2)
            s.append(x1)
        if x1 < x2:
            s.append(x1)
            s.append(x2)
        print(*s)
        
        
    
    pass


if __name__ == '__main__':
    main()