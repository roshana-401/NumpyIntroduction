import numpy as np
import matplotlib.pyplot as plt

 
x = [1,2,3,4]
y = [10,12,13,14]
 
Zarib = np.polyfit(x,y,2)
polynomialFunction = np.poly1d(Zarib) 
 
plt.plot(x,y, 'r*', x, polynomialFunction(x))
plt.xlim(0, 5)
plt.ylim(0, 20)
plt.show()