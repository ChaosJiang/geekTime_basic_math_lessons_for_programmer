# -*- coding: utf-8 -*-

class Lesson1_1:
    def decimal_to_binary (self,decimal):
        """
        {} places a variable into a string
        0 takes the variable at argument position 0
        : adds formatting options for this variable
        08 formats the number to eight digits zero-padded on the left
        b converts the number to its binary representation 
        """
        result = bin(decimal) # bin(decimal)/'{0:08b}'.format(decimal)
        """ 
        result=[]
        while num!=0:
            result.append(num & 1)
            num = num >> 1
        result.reverse() 
        """
        print('The the binary value of decimal {0} is {1}'.format(decimal,result))
        return result

    #Convert a Binary String to a decimal number.
    def binary_to_decimal (self,binaryStr):
        result = 0
        for bit in binaryStr:
            result *= 2
            if bit == '1':
                result += 1
        print('The the decimal value of binary {0} is {1}'.format(binaryStr,result))
        return result

class Lesson1_2:
    def left_shift(self,num,step):
        result = num << step
        print('数字{0}向左移动{1}位结果是{2}'.format(num,step,result))
        return result
    
    def right_shift(self,num,step):
        result = num >> step
        print('数字{0}向右移动{1}位结果是{2}'.format(num,step,result))
        return result

# The main method
def main():
    #Test for lesson1_1
    lesson1_1 = Lesson1_1()
    decimalNum = 250
    binaryStr = '11111110'
    lesson1_1.binary_to_decimal(binaryStr)
    lesson1_1.decimal_to_binary(decimalNum)

    #Test for lesson1_2
    lesson1_2 = Lesson1_2()
    lesson1_2.left_shift(128,4)
    lesson1_2.right_shift(-53,3)

if __name__ == '__main__':
    main()
