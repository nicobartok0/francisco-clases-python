import matplotlib.pyplot as plt


# initializing the data
x = [9, 9.5, 10, 10.5, 10.7, 11.1]
y = [19.66, 39.22, 58.98, 78.64, 88.47, 98.3]

# plotting the data
plt.plot(x, y)

# Adding title to the plot
plt.title("Peso vs Estiramiento")

# Adding label on the y-axis
plt.ylabel('Y-Axis')

# Adding label on the x-axis
plt.xlabel('X-Axis')

plt.show()