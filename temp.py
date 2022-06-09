from matplotlib import pyplot as plt
import numpy as np


x = np.array([])
for i in range(450,510,10): x = np.append(x,i) 
for i in range(510, 530,2): x = np.append(x,i)
for i in range(530,610,10): x = np.append(x,i)
y = np.array([168,227,274,328,374,394,395,396,404,402,400,395,363,378,360,354,345,245,168,109,62,29,25,5])
for i in y: i *= 1/1000
xlin = np.linspace(450,600)







P = np.polyfit(x,y,5)

def epsilon(x):
    return x/1.5

for i in range(0,len(y)): y[i] = epsilon(y[i]) 


P = np.polyfit(x,y,5)
plt.figure()
plt.plot(x,y,'.')
plt.plot(xlin, np.polyval(P,xlin))
plt.title("Remazol")
plt.xlabel("Longitud de onda (nm)")
plt.ylabel("Coeficiente de absorción molar (L/(cm*mol))")



