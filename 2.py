def main:
    n = 0
    while True:
        a = input()
        if a[0] == '-': n += 1
        elif a >= '36.6':
            break
    print(n)


if __name__ == "__main__":
    main()