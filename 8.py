def main():
    a = input().split()
    b = a[0]
    c = len(a) - 1
    n = 1
    while n != c:
        if len(b) > len(a[n]):
            b = a[n]
        else:
            pass
        n += 1
    print(b)


if __name__ == "__main__":
    main()
