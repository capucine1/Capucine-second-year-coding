#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:25:40 2017

@author: capucine
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:29:03 2017

@author: capucine
"""
import numpy as np
import math
#define a function for the user input of N and a while loop to ensure only positive integer values are used as N
def inputN():
    N= input("Input a value for N, where N is the number of terms in the Taylor Series. The higher the value for N, the more precise the value for arctan(x) will be. N must be a whole number. Input N:")
        #Making sure only values of N that satisfy the conditions are accepted
    while True:
        try:
            float(N)       #To eliminate values for N that are not numerical
        except ValueError:
            N= input("Value is not a number, try again:")
            continue
        N = float (N)
        if N%1!=0:         #To eliminate any values for N that are not integers
            N = input("Value for N not an integer, input an integer value for N:")
            continue
        elif 0>N:      #To eliminate values of N that are negative
            N = input("Value for N is smaller than zero, input a whole number for N:")
            continue
        else:
            print ("Value inputted correctly.")
            return N
            break
#Define a function for arctan(x)
def arctan(x,N):
            global g   #make g global so it can be used anywhere in the code
            if abs(x)<=1:  
                e = x
            else:
                e = 1/x
            z= float(0)        
            n= float(0)
            while (n <= N):    
                z += (((-1)**n)*(e**((2*n)+1)))/((2*n)+1)
                n += 1
            if x>1:
                g = ((math.pi/2)-z)
            elif x<-1:
                g = (-(math.pi/2)-z)
            else:
                g = z
            return g

Myinput = "v"
while Myinput != "q": #creating a menu for the user to select which part of the programme they would like to run
    Myinput = input ("Enter a choice to select which part of the programme you would like to run: 'a' to calculate a value for arctan(x), 'd' to plot the calculated vs real value, 'e' to find the value pi to 7sf, or 'q' to quit:")
    if Myinput == 'a':
        print ('You have chosen choice (a)')
        x= input("Input a value for x, where |x|is less than or equal to one:")
        #Making sure only values of x that satisfy the conditions are accepted
        while True:
            try:
                float(x)  #A non numerical value of x will show 'ValueError' for float(x)
            except ValueError:  #If a non numerical value is entered, and 'ValueError' shows, then the user will be asked to enter a new value for x 
                x= input("Value is not a number, try again:")     
                continue
            x = float (x)    
            if abs(x)>1:
                x = input("Value outside of bounds, try again:")   #To ensure the code only accepts values for x for which the modulus of x is less than, or equal to, one
            else:
                print ("Value inputted correctly.")
                break
        userN=inputN()  #run the function inputN to obtain a user value for N
        arctan(x,userN)  #run the function arctan(x) to obtain arctan(x) for the user inputted x and N
        print("The value of arctan("+str(x)+") is "+str(g)+" radians.")  

    elif Myinput == 'd':
        print("You have chosen part (d)")
        print("The value of N entered below will be used to calculate the values of arctan(x)")     
        userN=inputN()  #run inputN to obtain a user value for N
        x=float(-2)
        clear = open("export1.txt","w")#open and rewrite the export file
        clear.close()
        
        while x<=2:  #a while loop to produce arctan(x) for values of x in the range between -2 and 2, at intervals of 0.02
            arctan(x,userN) 
            file = open("export1.txt","a") #open the text file again, and append all results in the file
            file.write(str(x) + ";" +str(g) + ";" + str(math.atan(x))+ "\n") #write the values of x, arctan(x) from my programme, and the real value of arctan(x), for each value of x and then start a new line
            file.close()
            x+=0.02  #add 0.02 to the value of x so the loop will continue with this value
            x=round(x,7) #To make sure that the value of 2 is included otherwise the maximum value will be less than 2 due to the limitations of binary storing
        print("The values for x and both values of arctan(x), from the built in Python and from this programme have been exported to file export1.txt.")
  
    elif Myinput == 'e':
        print("You have chosen part (e)")
        print("The value of N required to obtain pi to 7sf is being calculated, please wait.")
        compi = float("{:7.6f}".format(np.pi))        
        x=1
        N=0
        arctan(x,N)
        p=g*4   
        while float("{:7.6f}".format(p))/compi != 1:
            N+=1
            p+=4*(((-1)**N)/(2*N+1))#as x=1, do not need to include the term x**(2n+1)
        print("The value of N required to obtain pi to 7sf is " + str(N) +". The value for pi calculated is"+str(compi)+".") 
        

    elif Myinput != 'q':
        print("This is not a valid choice")

print ("You have chosen to finish - Goodbye")
    
    
    
           