print("--------------Binary to Deciaml Conversion--------------")
binary = input("Enter a binary number, max is 8 numbers: ")

def check (binary):
    if len(binary) > 8:
        print("Binary number is too long")
        return False
    
def check2(binary):
    for digit in binary:
        if digit != "0" and digit != "1":
            print("Not a binary number")
            return False

if check2(binary) == False:
    exit()

else:
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print("The decimal number is", decimal)
    
