def main():
    while True:
        a = int(input())
        if a == 0:
            break
        elif a % 3 == 0 and a % 7 == 0:
            print('Караул!')
        elif a % 3 == 0:
            print('Несчастливое')
        elif a % 7 == 0:
            print('Опасное')
        else:
            print(a)


if __name__ == "__main__":
    main()