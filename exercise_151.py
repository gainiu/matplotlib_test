import matplotlib.pyplot as plt

# x_values=[1,2,3,4,5]
# y_values=[x**3 for x in x_values]
# plt.plot(x_values,y_values,linewidth=5)

# plt.title('Square Numbers',fontsize=24)
# plt.xlabel('Value',fontsize=14)
# plt.ylabel('Square of Value',fontsize=14)

# plt.tick_params(axis='both',labelsize=14)

# plt.show()

x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=40)

plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

plt.axis([0,5100,0,126000000000])

plt.show()