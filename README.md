# Inverted pendulum
Simple inverted pendulum simulation using Python

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Code Examples](#code-Examples)
* [Setup](#setup)

## General info
An exercise in visualization of the equations of motion. The ultimate goal is to simulate an inverted pendulum using a nonlinear system of equations. Additionally, the object can be stimulated by three signals (sine, triangle and square). 

**System Parameters:**
 - initial angle (Φ)
 - pendulum mass (m)
 - pendulum length (L)
 - coefficient of friction (b)
 - input signal (Ƭ)

**Fixed data:**
 - acceleration of gravity (g ≈ 9.81 ms/s^2)

![inverted-pendulum-scheme](https://user-images.githubusercontent.com/61761700/153585942-91f47c08-8c66-4e9a-832b-45f1067d18e5.png)

**Equations:**
 - moment of inertia (rod about end)
![image](https://user-images.githubusercontent.com/61761700/153587218-5b0f6332-68cb-4632-8994-140fce144e5f.png)
 - moment due to gravity
![image](https://user-images.githubusercontent.com/61761700/153587251-9177f800-07ad-4c2d-ae94-3230dc5b22cc.png)
 - moment due to friction
![image](https://user-images.githubusercontent.com/61761700/153587284-751dc298-093a-4f9e-8cda-fd1c74322b37.png)

**Model:**
- ω angular velocity
- φ angular displacement

![image](https://user-images.githubusercontent.com/61761700/153587513-6a49f4bb-4a7d-4e24-824e-197ee91483c0.png)

**A non-linear differential equation - solved with Fourth Order RK-Method**

![image](https://user-images.githubusercontent.com/61761700/153588203-50439f39-ffa2-4a54-8002-8cfa0fb13017.png)

## Technologies
Project is created with:
* Python 3.9
* PyQt5
* Numpy 1.21.4
* Matplotlib 3.5.0

## Code Examples
Running file named main.py

length and mass must by int values 
Angle and friction could be float values

1. Example
 * frition = 1
 * initial angle = 0.001 [°]
 * length = 3 [m]
 * mass = 1 [kg]

![image](https://user-images.githubusercontent.com/61761700/153590433-32ab21b1-1e1c-4846-82ca-286302704aff.png)

For these data we can observe that the pendulum from the vertical position (at the top) rotated (down) by 180° and due to the high value of friction it completely decelerated and remained in this position.

2. Example

3. Example

4. Example
	
## Setup
To run this project, install it locally using npm:
