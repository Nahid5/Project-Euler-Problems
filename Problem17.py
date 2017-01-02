"""
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
def turnToWords(x):
    underTwenty = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    overTwentyUnderOneHundred = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    overNinetyNineUnderOneThousand = ['One Hundred ', 'Two Hundred ','Three Hundred ',
                                      'Four Hundred ', 'Five Hundred ', 'Six Hundred ',
                                      'Seven Hundred ','Eight Hundred ', 'Nine Hundred ']
    if (x < 20):        #numbers under 20
        return underTwenty[x]
    elif (x < 100 and x > 19):      #over 19, under 100
        x = int(str(x)[0])        #for just the first number
        x -= 2      #to get the correct value
        return overTwentyUnderOneHundred[x]
    elif (x < 1000 and x > 99):     #over 99 uder 1000
        if (x == 100 or x == 200
            or x == 300 or x == 400
            or x == 500 or x == 600
            or x == 700 or x == 800
            or x == 900):
            x = int(str(x)[0])  # for just the first number
            x -= 1  # to get the correct value
            return overNinetyNineUnderOneThousand[x]
        else:       #add an and if number is not just a hundred number
            x = int(str(x)[0])  # for just the first number
            x -= 1  # to get the correct value
            return overNinetyNineUnderOneThousand[x] + "and"
    elif (x >= 1000 ):
        if (x == 1000):
            return "One Thousand"
        else:
            return "One Thousand and"


num = 5
ans = ""
"""
The first character is removed for the first three conditional statements after the number to word has been done
and it continues.  With the while the number will go one by one form the starting number until the 0 is reached
where is breaks.
"""
while (num != 0):
    if (len(str(num)) == 4):        #one thousand
        ans += turnToWords(num)
        tempNum = str(num)[1:]
        num = int(tempNum)
    elif (len(str(num)) == 3):      #hundreds
        ans += turnToWords(num)
        tempNum = str(num)[1:]
        num = int(tempNum)
    elif (len(str(num)) == 2):      #over 19, under 100
        ans += turnToWords(num)
        tempNum = str(num)[1:]
        num = int(tempNum)
    elif (len(str(num)) == 1):      #19 and below
        ans += turnToWords(num)
    num -= 1

print(len(ans.replace(" ", "")))        #removes empty characters