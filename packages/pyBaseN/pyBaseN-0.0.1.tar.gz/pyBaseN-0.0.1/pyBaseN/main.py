def decimal_binary(number):
    number=int(number)
    result=''
    while(number!=0):
        result=result+str(number%2)
        number=number//2
    return(result[::-1])


def decimal_octal(number):
    result=''
    while(number!=0):
        result=result+str(number%8)
        number=number//8
    return(result[::-1])

def decimal_hexadecimal(number):
    result=''
    while(number!=0):
        result_value=number%16
        if(result_value==10):
            result=result+'A'
        elif(result_value==11):
            result=result+'B'
        elif(result_value==12):
            result=result+'C'
        elif(result_value==13):
            result=result+'D'
        elif(result_value==14):
            result=result+'E'
        elif(result_value==15):
            result=result+'F'
        else:
            result=result+str(number%16)
        number=number//16
    return(result[::-1])

def binary_decimal(number):
    number=int(number)
    result=0
    i=0
    while(number):
        num=number%10
        number=number//10
        result=result+(num*(2**i))
        i+=1
    return(result)

def binary_octal(number):
    result=binary_decimal(number)
    return(decimal_octal(result))

def binary_hexadecimal(number):
    result=binary_decimal(number)
    return(decimal_hexadecimal(result))

def hexadecimal_decimal(number):
    result=0
    length=len(number)
    for i in number:
        if(i=='A' and length>=1):
            result=result+(10*(16**(length-1)))
        elif(i=='B' and length>=1):
            result=result+(11*(16**(length-1)))
        elif(i=='C' and length>=1):
            result=result+(12*(16**(length-1)))
        elif(i=='D' and length>=1):
            result=result+(13*(16**(length-1)))
        elif(i=='E' and length>=1):
            result=result+(14*(16**(length-1)))
        elif(i=='F' and length>=1):
            result=result+(15*(16**(length-1)))
        else:
            result=result+(int(i)*(16**(length-1)))
        length-=1
    return(result)

def hexadecimal_binary(number):
    result=hexadecimal_decimal(number)
    return(decimal_binary(result))

def hexadecimal_octal(number):
    result=hexadecimal_decimal(number)
    return(decimal_octal(result))

def octal_decimal(number):
    result=0
    i=0
    while(number):
        num=number%10
        number=number//10
        result=result+(num*(8**i))
        i+=1
    return(result)

def octal_binary(number):
    result=octal_decimal(number)
    return(decimal_binary(result))

def octal_hexadecimal(number):
    result=octal_decimal(number)
    return(decimal_hexadecimal(result))

def nines_complement(number):
    length=len(str(number))
    number=int(number)
    value=10**length
    return((value-1)-number)



def sign_magnitude_decimal(number):
    number=str(number)
    length=len(number)
    result=0
    for i in number[1:length]:
        result=result+(int(i)*(2**(length-2)))
        length=length-1
    result=str(result)
    if(number[0]=='1'):
        return(('-'+result))
    else:
        return(('+'+result))

def decimal_sign_magnitude(number,sign='+'):
    result=decimal_binary(number)
    if(sign=='-'):
        return('1'+result)
    else:
        return('0'+result)

def ones_complement(number):
    number=str(number)
    result=''
    for i in number:
        if(i=='1'):
            result=result+'0'
        elif(i=='0'):
            result=result+'1'
    return(result)

def binary_sum(number,number2):
    result=''
    carry=0
    number=str(number)
    number2=str(number2)
    len_number=len(number)
    len_number2=len(number2)
    length=max(len(number),len(number2))
    if(len_number<len_number2):
        number=number[::-1]
        for i in range(length-len_number):
            number=number+'0'
        number=number[::-1]
    elif(len_number2<len_number):
        number2=number2[::-1]
        for j in range(length-len_number2):
            number2=number2+'0'
        number2=number2[::-1]
    for i in range(length-1,-1,-1):
        if (int(number[i])+int(number2[i]))==0:
            result=result+str(0+carry)
            carry=0
        elif(int(number[i])+int(number2[i]))==1:
            result=result+ '1' if carry==0 else result+'0'
            if carry==1:
                carry=1
            else:
                carry=0
        else:
            result=result+'1' if carry==1 else result+'0'
            carry=1
            print(result)
    result=result+str(carry)
    return(result[::-1])        

def tens_complement(number):
    
    return(nines_complement(number)+1)

def twos_complement(number):
    value=ones_complement(number)
    result=binary_sum(value,1)
    return(result)
def ones_complement_decimal(number):
    if(number[0]=='0'):
        return('+'+str(binary_decimal(number)))
    else:
        value=ones_complement(int(number))
        return('-'+str(binary_decimal(value)))
def decimal_ones_complement(number,sign):
    if(sign=='+'):
        return('0'+str(decimal_binary(number)))
    else:
        result=decimal_binary(number)
        return('1'+ones_complement(result))
def twos_complement_decimal(number):
    if(number[0]=='0'):
        return('+'+str(binary_decimal(number)))
    else:
        return(int(ones_complement_decimal(number))+(-1))
def binary_subraction(number1,number2):
    value1=binary_decimal(number1)
    value2=binary_decimal(number2)
    result=int(value1)-int(value2)
    if(result<0):
        return(decimal_binary(str(result[1:])))
    else:
        return(decimal_binary(str(result)))

def binary_multiplication(number1,number2):
    value1=binary_decimal(number1)
    value2=binary_decimal(number2)
    result=int(value1)*int(value2)
    return(decimal_binary(str(result)))

def binary_division(number1,number2):
    value1=binary_decimal(number1)
    value2=binary_decimal(number2)
    result=int(value1)//int(value2)
    return(decimal_binary(str(result)))


