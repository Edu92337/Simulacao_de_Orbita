# Orbit Simulation - Verlet Method

## Description
This project simulates the motion of a body orbiting a star, using a physics-based approach grounded in Newton's law of gravitation.

Initially, a simple numerical integration method, the **Euler method**, was implemented. However, after noticing cumulative errors in the calculation of the body’s position and velocity, the algorithm was switched to the **Verlet method**, which is more stable for this type of simulation.

## Objective
The main goal of this project is to simulate the orbit of a body around a star and observe how the trajectories change depending on physical parameters.

## How it works?
1. The code uses the **pygame** library to render the simulation in real-time.
2. The gravitational forces between the star and the body are calculated based on Newton’s Universal Law of Gravitation.
3. The body’s acceleration is calculated from the force and the body’s mass.
4. The body’s position is updated using the **Verlet method**, which is an efficient way of integrating motion without accumulating significant rounding errors.

## Euler Method vs. Verlet Method

### Euler Method (Initial):
The Euler method was the first chosen for the simulation because it is simple and intuitive. However, the Euler method has **cumulative errors** that affect the accuracy of simulations, especially in systems with complex and long-term motions. Since the method uses first-order approximations for position and velocity, the errors can grow rapidly, causing the orbit to distort over time.

### Verlet Method (Current):
The Verlet method was adopted after the problems with the Euler method. It provides a more stable solution, without accumulating errors as significantly. The Verlet method is particularly suitable for simulating particles under conservative forces (such as gravity) because it calculates the position based on previous and current positions, making it more accurate for simulations with large time intervals.
