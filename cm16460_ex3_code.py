#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:01:37 2018

@author: capucine
"""

import numpy as np
import matplotlib.pyplot as plt
from operator import sub
m=100         #assigning values to all the key constants
p0=1.2
t0=0
v0=0
y0=1000
cd=1.2

def test(u):    #creating a funtion to test user inputs
    while True:
        try:
            float(u)       #To eliminate values for N that are not numerical
        except ValueError:
            u= input("Value is not a number, try again:")
            continue
        u = float (u)
        if 0>u:      #To eliminate values of N that are negative
            u = input("Value is smaller than zero, input a positive value:")
            continue
        else:
            print ("Value inputted correctly.")
            return u
            break
        
def graph(a1,a2,a3,b1,b2,b3):             #Creating a graphing function which can be used for all parts#
        fig, ax1 = plt.subplots()
        ax1.plot(a1,a2,'b')            #assigning what is plotted on each axis 
        ax1.set_xlabel(b1)            #labelling the axis
        ax1.set_ylabel(b2, color='b')
        ax1.tick_params('y', colors='b')
        if b3 and a3 !=0:                 #allows two variables to be plotted on separate y-axis
            ax2 = ax1.twinx()
            ax2.plot(a1,a3, 'r')
            ax2.set_ylabel(b3, color='r')
            ax2.tick_params('y', colors='r')        
        fig.tight_layout()
        plt.show()


def euler(t0,v0,y0,dt):      #defining the euler function
    V,Y,T=[],[],[]              #creating lists to append the values for V,T and Y to
    while (0.5<y0):          #setting the boundary condition so the while loop ends when the free faller reaches a height of 0
        k=(1.2*p0*0.7)/2 
        Y.append(y0)           #appending all the values to the above lists
        V.append(v0)
        T.append(t0)        
        y0+=(dt*v0)             #inputting the equations found for y and v using the Euler function
        v0+=-(dt*(9.81+(k/m)*abs(v0)*v0))
        t0+=dt    
    return V,Y,T       #returning the appended lists

def analytic(t0,v0,y0,dt):     #defining the analytic function
    VA,YA,TA=[],[],[]
    y1=1000              #setting the inital height for the free fall
    while (0.5<y1): 
        k=(1.2*p0*0.7)/2            #calculating k to be used below
        y1= y0 - (m/(2*k))*np.log((np.cosh(np.sqrt((k*9.81)/m)*t0))**2)   #inputting the analytical equations
        v1= - np.sqrt((m*9.81)/k)*np.tanh(np.sqrt((k*9.81)/m)*t0)
        YA.append(y1)    
        VA.append(v1)
        TA.append(t0)
        t0+=dt                #calculating the next time to be used
    return VA,YA,TA
   
def modeuler(t0,v0,y0,dt):        #defining the function for the modified Euler
    V,Y,T=[],[],[]
    k=(1.2*p0*0.7)/2              #defining the value for k
    while (0.00<y0):   
        Y.append(y0)
        V.append(v0)
        T.append(t0)
        vmid=v0-((dt/2)*(9.81+(k/m)*abs(v0)*v0))    #the equation to calculate vmid
        t0+=dt                    
        y0+=(dt*vmid)                #calculating the next height value
        v0-=((dt)*(9.81+(k/m)*abs(vmid)*vmid))               #calculating the next value for the velocity
    return V,Y,T

def peuler(t0,v0,y0,dt):      #defining the modified Euler function with varying density/drag
    V,Y,T=[],[],[]                 
    while (0.0000<y0):
        p=1.2*np.exp(-y0/7640)     #equation to calculate density at each height
        k=(cd*p*0.7)/2        #calculating the new value of k with the new density
        Y.append(y0)           #same code as used in modeuler function, but using the varying density
        V.append(v0)
        T.append(t0)              
        vmid=v0-((dt/2)*(9.81+(k/m)*abs(v0)*v0))
        t0+=dt
        y0+=(dt*vmid)
        v0-=((dt)*(9.81+(k/m)*abs(vmid)*vmid))                 
    return V,Y,T

MyInput = '8'          #creating a menu for the users to pick which section of the programme to run
while MyInput != 'q':
    MyInput = input('Enter a choice, "a" to calculate y(t) and v(t) for a falling body using Euler\'s method, "b" to compare this to the analytical predictions, "c" to calculate v(t) and y(t) with the modified Euler method for constant density, "d" to calculate with the modified Euler method and varying density, "e" to vary the mass and the inital height of the body, "f" to model a sphere, or "q" to quit:')
    print('You entered the choice: ',MyInput)
    if MyInput == 'a':
        print('You have chosen part (a)')
        dt=input ('Enter a positive number for step size; the smaller the number, the more accurate the result:')
        dt=test(dt)     #running the test function to ensure the value for dt is positive and numerical
        V,Y,T=euler(t0,v0,y0,dt)          #running the euler function to create the lists for velocity, height and time  
        graph(T,V,Y,'Time (s)', 'Velocity (m/s)', 'Height(m)' )       #plotting the graph for section a using the graphing function

    elif MyInput == 'b':
        print('You have chosen part (b)')
        dt=input ('Enter a positive number for step size; the smaller the number, the more accurate the result:')
        dt=test(dt)
        V,Y,T=euler(t0,v0,y0,dt)       #running the euler function to return lists for velocity, height and time
        VA,YA,TA=analytic(t0,v0,y0,dt)    #running the analytic function to calculate the predicted velocities and heights
        difV=map(sub, V, VA)       #using the inbuilt map function to subtract the list of the predicted velocities from the Euler velocities
        difV=list(difV)            #converting divV into a list that can then be plotted
        difY=map(sub, Y, YA)
        difY=list(difY)        
        graph(T,difV,difY,'Time (s)', 'Error in Velocity (m/s)', 'Error in height (m)' )  #using the graphing function to plot the errors
        
    elif MyInput == 'c':
        print('You have chosen part (c)')
        dt=input ('Enter a positive number for step size; the smaller the number, the more accurate the result:')
        dt=test(dt)
        V,Y,T=modeuler(t0,v0,y0,dt)     #running the modified Euler function to create lists for velocity, time and height
        graph(T,V,Y,'Time (s)', 'Velocity (m/s)', 'Height(m)' )    #graphing the trajectory calculated by modified Euler
        VA,YA,TA=analytic(t0,v0,y0,dt)
        difV=map(sub, V, VA)    #same method as in part b to compare results to the analytical predictions
        difV=list(difV)
        difY=map(sub, Y, YA)
        difY=list(difY)        
        graph(T,difV,difY,'Time (s)', 'Error in Velocity (m/s)', 'Error in height (m)' )
        print("The maximum reached speed is " +str(max(np.negative(V))) + "m/s")
            
    elif MyInput == 'd':
        print('You have chosen part (d)')
        dt=input ('Enter a positive number for step size; the smaller the number, the more accurate the result:')
        dt=test(dt)
        y0=39405       #setting the height of the fall to the actual height fallen by Baumgartner
        m=103       #Baumgartner's mass was approximately 73kg, and his equipment was approximately 30kg
        V,Y,T=peuler(t0,v0,y0,dt)
        graph(T,V,Y,'Time (s)', 'Velocity (m/s)', 'Height(m)' )   #plotting the modified Euler with varying density
        
    elif MyInput == 'e':
        print('You have chosen part (e)')
        dt=input ('Enter a positive number for step size; the smaller the number, the more accurate the result:')
        dt=test(dt)
        y0=input('Enter a positive number for the height of the fall:')  #allows the user to vary the height of the fall
        y0=test(y0)
        m=input('Enter the desired mass of the body in kg:')      #allows the user to input the mass of the body
        m=test(m)
        V,Y,T=peuler(t0,v0,y0,dt)
        graph(T,V,Y,'Time (s)', 'Velocity (m/s)', 'Height(m)' )
        print("The maximum reached speed is " +str(max(np.negative(V)))+ "m/s")    #printing the maximum speed reached by the body
        
    elif MyInput == 'f':
        print('You have chosen part (f)')
        dt=input ('Enter a positive number for step size; the smaller the number, the more accurate the result:')
        dt=test(dt)
        y0=input('Enter a positive number for the height of the fall:')  #allows the user to vary the height of the fall
        y0=test(y0)
        m=input('Enter the desired mass of the body in kg:')
        m=test(m)
        cd=0.47                  #setting the drag coefficent that is appropriate for a sphere
        V,Y,T=peuler(t0,v0,y0,dt)     #calculating the trajectory with the appropriate parameters for a sphere but using the modified Euler method
        graph(T,V,Y,'Time (s)', 'Velocity (m/s)', 'Height(m)' )
        print("The maximum reached speed is " +str(max(np.negative(V)))+ "m/s")

    elif MyInput != 'q':
        print('This is not a valid choice')
print('You have chosen to finish - goodbye.')