def main():
    phrase = ''
    while True:
        a = input()
        if a == 'стоп': break
        phrase += a + ' '
    phrase = phrase.split('!')
    for str in phrase:
        if str.strip() != '':
            print(f'{str.strip()}!')


if __name__ == "__main__":
    main()
