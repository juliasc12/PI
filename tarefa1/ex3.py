import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4 * np.pi, 0.1) #começo,fim,intervalo de crescimento
y = np.sin(x)
z = np.cos(x)

#print('x:', x[:5])
#print('sen(x):', y[:5])
#print('cos(x):', z[:5])

plt.plot(x, y, 'r--', x, z, 'b-') #calcula o grafico

plt.xlabel('Valores de 0 a 4pi')
plt.ylabel('Sen(x) e Cos(x)')
plt.title('Grafico do Sen e Cos - Exercicio3')
plt.legend(['sen(x)','cos(x)'])
plt.show() #mostra o grafico
