import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()
x, y = [], []

def animate(i):
    x.append(i)
    y.append(random.randint(0, 100))
    ax.clear()
    ax.plot(x, y)
    ax.set_title("Live Updating Plot")

ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()
