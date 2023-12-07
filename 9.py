def main():
    c = input()
    if c == 'стоп':
        exit()
    c = int(c)
    d = ''
    while True:
        a = input()
        if a == 'стоп':
            break
        elif a in '+-/*':
            d = a; continue
        elif d == '+':
            c += int(a)
        elif d == '-':
            c -= int(a)
        elif d == '/':
            c /= int(a)
        elif d == '*':
            c *= int(a)
    print(int(c))


if __name__ == "__main__":
    main()
