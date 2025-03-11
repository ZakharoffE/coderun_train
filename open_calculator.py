import sys


def main():
    cyfri = set(input().split())
    chislo = set(list(input()))
    if cyfri == chislo:
        print(0)
    elif cyfri != chislo:
        chislo -= cyfri
        print(len(chislo))
    pass


if __name__ == '__main__':
    main()