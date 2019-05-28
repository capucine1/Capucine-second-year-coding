#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:43:34 2018

@author: capucine
"""
import numpy as np
import math
import matplotlib.pyplot as plt


def simpson(f, a, b, n):    #define the function simpson function
    h = (b - a) / n       #calculating the width of each parabola section
    s = f(a) + f(b)       
    i = 1
    while True:
        if(a + i*h)<= b and i%2!=0:     #for f1,f3,f5...
            s+= 4 * f(a + i*h)
            i= i + 1
            continue
        elif(a+ i*h)<= b and i%2==0:     #for f2,f4,f6.....
            s+= 2 * f(a + i*h)
            i= i + 1
            continue
        elif (a +i*h) >= b:
            break
    return s*(h/3)    #return the integration value calculated from Simpson's rule

def interval(N):
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
        elif N%2!=0:
            N= input ("The N input is odd, input an even integer:")   #can only have even numbers for N
        else:
            print ("Value inputted correctly.")   
            N= int(N)              
            break
    return N

def eq5(xprime,k,z,x):    
    e=np.exp((1j*k)/2*z * (x-xprime)**2)            
    return e

def X(f, a, b, n, z, x, k):    #define the function simpson function        
    if n % 2:
        raise ValueError ("An odd value for n was inputted. N must be positive")

    h = (b - a) / n       #calculating the width of each parabola section
    s = f(a,k,z,x)+f(b,k,z,x)       
    i = 1
    while True:
        if(a + i*h)<= b and i%2!=0:     #for f1,f3,f5...
            s+= 4 * f(a + i*h,k,z,x)
            i+=1
            continue
        elif(a+ i*h)<= b and i%2==0:     #for f2,f4,f6.....
            s+= 2 * f(a + i*h,k,z,x)
            i+= 1
            continue
        elif (a +i*h) >= b:
            break
    return s* (h/3) 

def eqn5y(yprime,k,z,y):
     e=np.exp((1j*k)/2*z * (y-yprime)**2)            
     return e

def Q(f,k,z,E0):     
    v=1/0.5E-6*1
    xy= X(eq5,0,0.05E-3,I,10E-3,xvals[i],(2*np.pi/(.5E-6))) *eqn5y*v
    return xy 

    
def X2(f, c, d, n, z, y, k):    #define the function simpson function for eq4
    if n % 2:
        raise ValueError ("An odd value for n was inputted. N must be positive")

    h = (d - c) / n       #calculating the width of each parabola section
    s = f(c,k,z,y)+f(d,k,z,y)       
    i = 1
    while True:
        if(c + i*h)<= d and i%2!=0:     #for f1,f3,f5...
            s+= 4 * f(c + i*h,k,z,y)
            i+=1
            continue
        elif(c+ i*h)<= d and i%2==0:     #for f2,f4,f6.....
            s+= 2 * f(c + i*h,k,z,y)
            i+= 1
            continue
        elif (c +i*h) >= d:
            break
    return s* (h/3) 





MyInput = 'p'
while MyInput != 'q':
    MyInput = input("Enter a choice, \'a' to calculate a simple integration using Simpson\'s rule, \'b' to integrate equation 5, \'c' to integrate Fresnel's equation, or \'q' to quit:")
    print('You entered the choice: ',MyInput)
    if MyInput == 'a':
        print('You have selected to calculate the integral for sin(x) in the range between 0 and pi')      
        I= input("Input a positive, even integer for number of intervals desired to integrate the function. The higher the number of intervals, the more accurate the integration. N:")  
        I= interval(I)
        print("The integral of sin(x) in the interval of 0 to pi is " + str(simpson(lambda x: math.sin(x),0,math.pi,I)))
    elif MyInput == 'b':
        print('You have selected to integrate equation 5')
        I= input("Input a positive, even integer for number of iterations to calculate the integral:")  
        I= interval(I)                        
        NumPoints = 200
        xmin = -4
        xmax = 4
        dx = (xmax - xmin) / (NumPoints - 1)
        xvals = [0.0] * NumPoints       #creating the arrays for x and y values
        yvals = np.zeros(NumPoints)
        for i in range(NumPoints):
            xvals[i] = xmin + i * dx
            yvals[i] = (abs(X(eq5,0,0.05E-3,I,10E-3,xvals[i],(2*np.pi/(.5E-6)))))**2
        plt.xlabel('x')
        plt.ylabel('(modulus(X(x))^2')
        plt.plot(xvals,yvals)     #plotting the graph
        plt.show()
    elif MyInput == 'c':
        print('You have selected to integrate the Fresnel integral.')   
        print('Input the number of intervals desired for integration. The image produced will be displayed below.')
        I= input("Input a positive, even integer for number of iterations to calculate the integral:")  
        I= interval(I)
        z=float(input("Enter a value for the spacing (mm):"))
        z*=10**(-3)
        NumPoints = 200
        xmin = 1E-3        #limits of integration
        xmax = 2E-3
        ymin = 1E-3
        ymax = 2E-3
        dx = (xmax - xmin) / (NumPoints - 1)
        dy = (ymax-ymin) /(NumPoints - 1)
        xrange = np.zeros((NumPoints), dtype=complex)         #x and y ranges
        yrange = np.zeros((NumPoints), dtype=complex)
        holder = np.zeros((NumPoints,NumPoints),dtype=complex)
        valuedisplay = np.zeros((NumPoints,NumPoints), dtype=complex)
        for n in range(NumPoints):
            xrange[n]=X(eq5,xmin,xmax,I, z, xmin+n*dx,(2*np.pi/(.5E-6)))
            for o in range (NumPoints):
                yrange[o]= X(eq5,ymin,ymax,I,z, ymin+o*dy,(2*np.pi/(.5E-6)))
                holder[n,o] = xrange[n]*yrange[o]            
        x=0
        laststep=0
        while x<NumPoints:                   #while loop to calculate the intensities
            y=0
            while y<NumPoints:
                laststep=holder[x,y]
                conjugatelaststep= np.conjugate(laststep)
                valuedisplay[x,y]=3E8*8.85E-12*conjugatelaststep*laststep
                y+=1
            x+=1
        plt.imshow(valuedisplay.real)     #plotting the graph
        plt.show()
        
    elif MyInput != 'q':
        print('This is not a valid choice')
print('You have chosen to finish - goodbye.')

