import matplotlib.pyplot as plt
import pandas as pd

# Simulated data
data = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Sales': [200, 220, 250, 270, 300]
})

plt.plot(data['Day'], data['Sales'], marker='o')
plt.title("Sales Over Days")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()
