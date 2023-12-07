def main():
    list = list()
    while True:
        a = int(input())
        if a > 1000 or a < -1000:
            break
        else:
            list.append(a)
    max1 = max(list)
    list.remove(max1)
    max2 = max(list)
    print(max2)


if __name__ == "__main__":
    main()