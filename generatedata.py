#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

# Coefficients of a polynomial of 3rd order: y = a*x³ + b*x² + c*x + d.
a = 4
b = 1
c = 10
d = -50
coeff_orig = []
coeff_orig.append(a)
coeff_orig.append(b)
coeff_orig.append(c)
coeff_orig.append(d)

# Write the original parameters to file.
e = open('/home/nikhilesh/DataTextFiles/coeff_orig.txt', 'w')
for i in range(0, len(coeff_orig)):
	e.write(str(coeff_orig[i])+'\n')  # python will convert \n to os.linesep
e.close()  # you can omit in most cases as the destructor will call it

# Create the data set (and add noise).
x = np.linspace(-5.0, 5.0, 2000)
y = a*pow(x, 3) + b*pow(x, 2) + c*(x) + d				
noise = np.random.normal(0, 100, 2000)
y_noise = y + noise

# Write x, y(x) directly to file.
f = open('/home/nikhilesh/DataTextFiles/data.txt', 'w')
for i in range(0, len(x)):
	f.write(str(x[i])+' '+str(y_noise[i])+'\n')  # python will convert \n to os.linesep

f.close()  # you can omit in most cases as the destructor will call it

# Plot the data.
plt.plot(x, y_noise, 'ro')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

