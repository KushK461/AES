import matplotlib.pyplot as plt
import numpy
import scipy.stats as lr
import sklearn.linear_model as LR

x = [[4,6][7,3][3,8][6,5],[10,4],[5,1]]
#b1,b0,r,p,err = lr.linregress(x,y)

modelx=LR.LinearRegression()
modelx.fit(x,y)
print(modelx_coef[_0])

#n=len(x)
#yp=[0]*n
#for i in range(n):
 #   yp[i]=b0+b1*x[i]

plt.scatter(x,y, color='red')
plt.plot(x,yp)
plt.show()