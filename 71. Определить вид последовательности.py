import sys


def main():
    posled = []
    const = 0
    asc = 0
    desc = 0
    while (x := int(input())) != -2000000000:
        posled.append(x)
    
    for i in range(1, len(posled)):
        if posled[i - 1] == posled[i]:
            const += 1
            if const == len(posled) - 1:
                print('CONSTANT')
            
        elif posled[i - 1] < posled[i]:
            asc += 1
            if asc == len(posled) - 1:
                print('ASCENDING')
            
        elif posled[i - 1] > posled[i]:
            desc += 1
            if desc == len(posled) - 1:
                print('DESCENDING')
                
    if asc > 0 and const > 0 and desc == 0:
        print('WEAKLY ASCENDING')
    elif desc > 0 and const > 0 and asc == 0:
        print('WEAKLY DESCENDING')
    elif asc > 0 and desc > 0 and const > 0:
        print('RANDOM')
        
    pass


if __name__ == '__main__':
    main()