def card_check():
    card_number=input("Enter Card_Number:")
    length=len(card_number)
    card_number=card_number[::-1]
    """
    we want to convert the string into integer using typecast
    """
    if(length==16):

        digit_sum=0
        
        for i in range(0,length,1):

            if(i%2!=0):
                
                number=int(card_number[i])*2
                digit_sum=digit_sum+(number%10)
                number=number//10
                digit_sum=digit_sum+number

            else:

                digit_sum=digit_sum+int(card_number[i])

        if(digit_sum%10==0):

            return("card is valid")

        else:

            return("Invalid")

    else:

        return("Invalid")

def card_type(s):
    if(s==1 or s ==2):
        return("Airlines")

    elif(s==3):
        return("Travel and Entertainment")

    elif(s==4 or s==5 ):
        return("Banking and Financial")

    elif(s==6):
        return("Merchandising and Banking")

    elif(s==7):
        return("Petroleum")

    elif(s==9):
        return('National Assignment')

    elif(s==8):
        return("Healthcare and Telecommunications")

    else:
        return("Enter a valid Number")

