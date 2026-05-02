import matplotlib.pyplot as plt

years = [2019,2020,2021,2022,2023]
sales = [500,350,345,588,996]

plt.plot(years, sales, marker= 'o' , linestyle='-',color ='green')

plt.title('Annual Sales from 2019 to 2023')
plt.xlabel('years')
plt.ylabel('sales')

plt.show()

hours_studied = [4,7,2,1,5,9]
scores = [89,34,69,81,90,87]

plt.scatter(hours_studied,scores ,color = 'yellow')
plt.title('Hours studied to scores gotten')
plt.xlabel('hours_studied')
plt.ylabel('scores')
plt.show()
