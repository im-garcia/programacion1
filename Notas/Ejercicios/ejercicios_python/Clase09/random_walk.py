import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()

N = 100000
num_walks = 12
walks = [randomwalk(N) for _ in range(num_walks)]

max_distances = [np.max(np.abs(w)) for w in walks]
i_max = np.argmax(max_distances)
i_min = np.argmin(max_distances)

fig = plt.figure()

plt.subplot(2, 1, 1)
for w in walks:
    plt.plot(w)
plt.title("12 Caminatas al azar")
plt.yticks([-500, 0, 500]), plt.xticks([])
plt.ylim(-1000, 1000)

plt.subplot(2, 2, 3)
plt.plot(walks[i_max])
plt.title("La caminata que más se aleja")
plt.yticks([-500, 0, 500]), plt.xticks([])
plt.ylim(-1000, 1000)

plt.subplot(2, 2, 4)
plt.plot(walks[i_min])
plt.title("La caminata que menos se aleja")
plt.yticks([-500, 0, 500]), plt.xticks([])
plt.ylim(-1000, 1000)

plt.show()
