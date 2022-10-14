
# Import libraries
import matplotlib.pyplot as plt

# Creating dataset
data_1 = (10,50,300,400,550,60,70) 
data_2 = (0,10,30,45,5,80,70) 
data = [data_1, data_2]

# Creating plot
plt.boxplot(data)
 
# show plot
plt.show() 