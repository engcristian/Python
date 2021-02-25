import matplotlib.pyplot as plt
X = [[1.,1.], [2.,2.], [3.,3.]]
Y = [[1.,1.], [2.,2.], [3.,3.]]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X, Y)
ax.set_xlabel(r'$\rho$')
ax.yaxis.set_major_formatter('${x:.2f}')
ax.xaxis.set_major_formatter('R${x:.2f}')
plt.show()