# Kata: https://www.codewars.com/kata/52608f5345d4a19bed000b31
numerals={"-":"负",".":"点",0:"零",1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十",100:"百",1000:"千",10000:"万"}

def to_chinese_numeral(n):
    originalN = abs(n)
    wholeList = str(n).split('.')[0]
    decimalList = str(n).split('.')[1] if '.' in str(n) else []
    output = ''

    for digit in wholeList:
        if digit == '-':
            output += numerals[digit]
            n *= -1
            continue

        if digit == '0':
            output += numerals[0]
            continue

        if n >= 10000:
            output += numerals[n//10000]
            output += numerals[10000]
            n -= n//10000 * 10000
        elif n >= 1000:
            output += numerals[n//1000]
            output += numerals[1000]
            n -= n//1000 * 1000
        elif n >= 100:
            output += numerals[n//100]
            output += numerals[100]
            n -= n//100 * 100
        elif n >= 10:
            if originalN >= 20: output += numerals[n//10]
            output += numerals[10]
            n -= n//10 * 10
        else:
            output += numerals[int(digit)]
            if n >= 10:
                n -= 10
            else:
                n -= int(digit)

    if originalN >= 1:
        output = output.rstrip(numerals[0])
        output = list(output)
        for i, digit in enumerate(output):
            if digit == numerals[0] and (output[i+1] == numerals[0] or output[i-1] == numerals[0]):
                output.remove(numerals[0])
        output = ''.join(output)

    if decimalList:
        output += numerals['.']
        for digit in decimalList:
            output += numerals[int(digit)]

    return output

print(to_chinese_numeral(10006))
print('Expected: 一万零六')
