for x in '0123456789abcdefghi':
    a = int('98897' + x + '21', 19) + int('2' + x + '923', 19)
    if a%18 == 0:
        print(a//18)
