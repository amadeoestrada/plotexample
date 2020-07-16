import matplotlib.pyplot as plt
import numpy as np
import time

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
#plt.show()
#fig2, ax2 = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1.5, 2.7, 3.1, 4.2], [7, 8, 4, 1])  # Plot some data on the axes.
#plt.show()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#x = np.linspace(0, 2, 100)     # en el rango de 0-2, 100 numeros
#fig, ax = plt.subplots()  # crea la figura y los ejes
#ax.plot(x, x, label='linear')  # pone los datos y asigna una etiqueta
#ax.plot(x, x**2, label='quadratic')  # lo mismo...
#ax.plot(x, x**3, label='cubic')  # ... y otra vez
#ax.set_xlabel('x label')  # Añade la etiqueta en el eje x
#ax.set_ylabel('y label')  # Añade la etiqueta en el eje y
#ax.set_title("Simple Plot")  # Añade un título
#ax.legend()  # añade la leyenda
#plt.draw()
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
#plt.draw()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#t2 = np.arange(0.0, 5.0, 0.02) # de 0.0 a 5.0 en pasos de 0.02
#s = len(t2)
#plt.figure()
#plt.show()
#for i in range(s):
#    plt.plot(t2[i], np.cos(2*np.pi*t2[i]), 'r.')
#    plt.draw()
#    for j in range(10000):    pass
#x =10

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#def f(t):
#    return np.exp(-t) * np.cos(2*np.pi*t)
#t1 = np.arange(0.0, 5.0, 0.1)
#t2 = np.arange(0.0, 5.0, 0.02)
#plt.figure()
#plt.subplot(221)   # renglons, , columnas, numero de grafico
#plt.plot(t2, np.cos(2*np.pi*t2), 'k')
#plt.subplot(222)
#plt.plot(t2, np.cos(2*np.pi*t2), 'k--', t1, np.cos(2*np.pi*t1), 'r.')
#plt.subplot(223)
#plt.plot(t2, f(t2), 'k')
#plt.subplot(224)
#plt.plot(t1, f(t1), 'r.', t2, f(t2), 'k--')
#plt.show()
#import matplotlib.pyplot as plt

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation

#fig, ax = plt.subplots()        # crear la figura
#xdata, ydata = [], []           # crear las estructuras
#ln, = plt.plot([], [], 'ro')    # tupla con estructuras

#def init():                     # función para iniciar
#    ax.set_xlim(0, 2*np.pi)     # definir limites de x
#    ax.set_ylim(-1, 1)          # definir límites de y
#    return ln,

#def update(frame):              # función cuadro x cuadro
#    xdata.append(frame)         # añadir en x
#    ydata.append(np.sin(frame)) # FUNCION SENO
#    ln.set_data(xdata, ydata)   # combinar en una tupla
#    return ln,

#ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                    init_func=init, blit=True, interval=50)
#plt.show()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#import numpy as np
#import matplotlib.pyplot as plt

#plt.rcParams['legend.fontsize'] = 10  # tamaño de letra
#fig = plt.figure()                    # crear la figura
#ax = fig.gca(projection='3d')         # crear los ejes 3D

# Preparar los arreglos x, y, z - 100 en total de -4pi a 4pi
#theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
#z = np.linspace(-2, 2, 100)
#r = z**2 + 1
#x = r * np.sin(theta)
#y = r * np.cos(theta)

# Mostrar el gráfico
#ax.plot(x, y, z, 'r', label='parametric curve')
#ax.legend()                                 # mostrar leyenda
#plt.show()

