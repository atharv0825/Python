import matplotlib.pyplot as plt

labels = {'Apples','Bananas','Cherries','Dates'}
sizes = [25,35,20,20]
colors = ['Green','Orange','White','Red']
explode = (0,0,0,0)


plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct='%1.1f%%',shadow=True)
plt.title("Fruit Distribution")
plt.show() 