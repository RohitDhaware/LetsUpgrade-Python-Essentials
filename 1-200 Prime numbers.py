
  
print ("The Prime Numbers from 1 to 200 ")  
for number in range (1, 200 + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
