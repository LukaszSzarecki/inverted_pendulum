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
* Lorem version: 12.3
* Ipsum version: 2.33
* Ament library version: 999

## Code Examples
	
## Setup
To run this project, install it locally using npm:
