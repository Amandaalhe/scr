# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 08:29:39 2023

@author: amand
"""

# Initialise variable x0
x0 = 0
print("x0", x0)
# Initialise variable y0
y0 = 0
print("y0", y0)
# Change x0 and y0 randomly
import random
rn = random.random()
print(rn)
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)

rn = random.random()
print(rn)
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise variable x1
x1 = 0
print("x1", x1)

# Initialise variable y1
y1 = 0
print("y1", y1)

# Change x1 and y1 randomly
rn = random.random()
print(rn)
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print("x1", x1)


rn = random.random()
print(rn)
if rn < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print("y1", y1)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Calculate the difference in the x coordinates.
d1= (x1-x0)**2
d2= (y1-y0)**2
print ("dx", d1)
print ("dy", d2)

# Calculate the square root
d=(d1+d2)**0.5
print (d)

# Calculate the distance between the cartesian coordinates(0, 0) and (3, 4). 
x0=0
y0=0
x1=3
y1=4

print (x0, y0, x1, y1)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Calculate the difference in the x coordinates.
d1= (x1-x0)**2
d2= (y1-y0)**2
print ("dx", d1)
print ("dy", d2)

# Calculate the square root
d=(d1+d2)**0.5
print (d)

#AMB2
import random
import matplotlib.pyplot as plt
import operator

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Create a list to store agents
agents = []

# Initialise variable x0
x0 = random.randint(0, 99)
print("x0", x0)
# Initialise variable y0
y0 = random.randint(0, 99)
print("y0", y0)
agents.append([x0,y0]) # Append to the list agents
print(agents)


# Plot the agents in black
plt.scatter(agents[0][0], agents[0][1], color='black')
plt.scatter(agents[1][0], agents[1][1], color='black')
plt.show()
# Get the coordinates with the largest x-coordinate
print(max(agents, key=operator.itemgetter(0)))

#Plot the point with the largest x coordinate red
maxpoint= []
maxpoint.append(max(agents, key=operator.itemgetter(0)))
print(maxpoint)
plt.scatter(maxpoint[0][0], maxpoint[0][1], color='red')


agents.clear()
print(agents)

n_agents = 10
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])

print(agents)
max_value= max(agents)
print(max_value)


# Plot the agents in black in loop with the largest x coordinate red

for i in range(n_agents):
    if agents[i]==max_value:
        plt.scatter(agents[i][0], agents[i][1], color='red')
    else:
        plt.scatter(agents[i][0], agents[i][1], color='black')
    
plt.show()
