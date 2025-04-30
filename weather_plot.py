import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temps = [22, 21, 23, 24, 20, 19, 22]

plt.plot(days, temps, marker='o', linestyle='-', color='green')
plt.title("Weekly Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
