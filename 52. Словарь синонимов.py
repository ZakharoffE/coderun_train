import sys


def main():
    dict1 = {}
    dict = {}
    n = int(input())
    if n > 0:
        for _ in range(n):
            i, j = input().split()
            dict1[i] = j
            dict[j] = i
        s = input()
        if s in dict.keys():
            print(dict[s])
        else:
            print(dict1[s])
        
    pass


if __name__ == '__main__':
    main()