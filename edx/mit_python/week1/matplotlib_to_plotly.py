import plotly.plotly as py
import matplotlib.pyplot as plt
from plotly.graph_objs import *

plt.figure(1)
principal = 10000
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate
plt.plot(range(years + 1), values)
plt.title('5% Growth, Compounded Annually')
plt.xlabel('Years of Compounding')
plt.ylabel('Value of Principal ($)')
py.plot_mpl(plt.figure(1))  # convert mpl object to plotly
figure = py.get_figure('https://plot.ly/~Rafeh01/36/_5-growth-compounded-annually/')
py.image.save_as(figure, 'mpl_to_plotly_image.png')
# plt.show()

# plot_url = py.plot(fig)
