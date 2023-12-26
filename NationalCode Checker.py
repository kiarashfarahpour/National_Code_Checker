def IsNationalCode(text):

    if len(text) != 10: return False
    if text == "0000000000": return False
    if text == "1111111111": return False
    if text == "2222222222": return False
    if text == "3333333333": return False
    if text == "4444444444": return False
    if text == "5555555555": return False
    if text == "6666666666": return False
    if text == "7777777777": return False
    if text == "8888888888": return False
    if text == "9999999999": return False

    n = int(text[0]) * 10
    n = n + int(text[1]) * 9
    n = n + int(text[2]) * 8
    n = n + int(text[3]) * 7
    n = n + int(text[4]) * 6
    n = n + int(text[5]) * 5
    n = n + int(text[6]) * 4
    n = n + int(text[7]) * 3
    n = n + int(text[8]) * 2

    lastChar = int(text[9])

    remain = n % 11

    if remain == 0 and remain == lastChar: return True
            
    if remain == 1 and lastChar == 1: return True

    if remain > 1 and lastChar == 11 - remain: return True

    return False