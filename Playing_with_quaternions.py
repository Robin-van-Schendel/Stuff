# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 18:29:50 2021

@author: Robin
"""
""" Here I try to fuck around with calculating Quaternions. I basically take the
information from https://www.meccanismocomplesso.org/en/hamiltons-quaternions-and-3d-rotation-with-python/
 and use it  to get started on something. As such I will just be mimicking it"""

import math as m
import numpy as np
import matplotlib.pyplot as plt

# First we need to calculate the quaternion conjugate
def q_conjugate(q):
    w, x, y, z = q
    return (w, -x, -y, -z)
 
# We now have all the elements to carry out the multiplication
# P1 = qP0q*
# In fact P is none other than the pure quaternion obtained, using the vector v
# to rotate for the three imaginary terms and the real part w equal to zero
def qv_mult(q1, v1):
    q2 = (0.0, ) + v1
    return q_mult(q_mult(q1, q2), q_conjugate(q1))[1:]

# As we can see in the function, it is necessary to use the multiplication between 
# quaternions, and therefore we must implement it in Python using the equations 
# previously performed mathematically.
def q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z

# Conversion from Euler angles to quaternions and vice versa:
# Here we take the Euler angles phi, Theta and Psi to convert into Quaternion values
def euler_to_quaternion(phi, theta, psi):
    qw = m.cos(phi/2) * m.cos(theta/2) * m.cos(psi/2) + m.sin(phi/2) * m.sin(theta/2) * m.sin(psi/2)
    qx = m.sin(phi/2) * m.cos(theta/2) * m.cos(psi/2) - m.cos(phi/2) * m.sin(theta/2) * m.sin(psi/2)
    qy = m.cos(phi/2) * m.sin(theta/2) * m.cos(psi/2) + m.sin(phi/2) * m.cos(theta/2) * m.sin(psi/2)
    qz = m.cos(phi/2) * m.cos(theta/2) * m.sin(psi/2) - m.sin(phi/2) * m.sin(theta/2) * m.cos(psi/2)
    return [qw, qx, qy, qz]

# And here we do the reverse
def quaternion_to_euler(w, x, y, z):
    t0 = 2 * (w * x + y * z)
    t1 = 1 - 2 * (x * x + y * y)
    X = m.atan2(t0, t1)
    
    t2 = 2 * (w * y - z * x)
    t2 = 1 if t2 >  1 else t2
    t2 = -1 if t2 < -1 else t2
    Y = m.asin(t2)
    
    t3 = 2 * (w * z + x * y)
    t4 = 1 - 2 * (y * y + z * z)
    Z = m.atan2(t3, t4)
    
    return X, Y, Z

# now let's try a rotation using Euler angles
# Let's express a vector as a tuple
v1 = (0, 0, 1)

# Let's define the three Euler angles first and convert them into a quaternion
phi = 0
theta = m.pi/2
psi = m.pi/2 
q = euler_to_quaternion(phi, theta, psi)
print("First quaternion is as follows")
print("w = ", q[0])
print("x = ", q[1])
print("y = ", q[2])
print("z = ", q[3])
print("")

# Now let's do the multiplication between vector and quaternion
v2 = qv_mult(q, v1)
print("New vector after multiplication between vector and quaternion")
print(np.round(v2, decimals=2))
print("")

# Now let's see the rotation by plotting the vector (which describes the point)
# before and after the rotation on a graph with cartesian axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Cartesian axes
ax.quiver(-1, 0, 0, 3, 0, 0, color='#aaaaaa', linestyle='dashed')
ax.quiver(0, -1, 0, 0, 3, 0, color='#aaaaaa', linestyle='dashed')
ax.quiver(0, 0, -1, 0, 0, 3, color='#aaaaaa', linestyle='dashed')
# Vector before rotation
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='b')
# Vector after rotation
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='r')
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
plt.show()