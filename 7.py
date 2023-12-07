def main():
    a = input().split()
    b = input().split()
    vbig = int(a[0]) * int(a[1]) * int(a[2])
    vskinny = 0
    k = 0
    while True:
        if int(b[k]) == 0: break
        v = int(b[k]) * int(b[k + 1]) * int(b[k + 2])
        k += 3
        vskinny += v
    if vbig >= vskinny:
        print('Да')
    else:
        print('Нет')


if __name__ == "__main__":
    main()
