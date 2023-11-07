import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Customer.csv")
plt.bar(data["first_name"],data["country"])
plt.show()


data = pd.read_csv("Customer.csv")
plt.scatter(data["first_name"],data["country"])
plt.show()


data = pd.read_csv("Customer.csv")
plt.hist(data["index"],bins=[1,2,3,4,5,6,7,8,9])
plt.show()


data = pd.read_csv("Customer.csv")
plt.plot(data["country"],data["city"])
plt.show()
