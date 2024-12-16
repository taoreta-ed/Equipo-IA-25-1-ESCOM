

lr = 0.1
epocas = 1000
b0 = 0.1 # Se recomienda inicializar entre 0 y 1 de forma aleatoria
b1 = 0.2
# 
# B = np.array(dimensión = m)
lamda = 0.001
# Número de muestras
m = len(x)
grafica = []

for epoch in range (epocas):
    Yobt = b0 + b1*X
    # Calcular el ECM regulado
    J = (1/(2*m))*np.sum(yd-Yobt)**2 + (lambda/2)*np.sum(b1**2)
    grafica += J

    ## Calculo de B0 y B1
    b0 = b0 - (lr/m)*np.sum(Yobt-yd)
    b1 = b0 - (lr/m)*np.sum(Yobt-yd)*X + (lambda/m)*b1

print(f"Parámetro B0 = {b0}")
print(f"Parámetro B1 = {b1}")

# Graficar J
plt.figure(figsize(8,6))
plt.plot(range(len(grafica)), grafica, label = "Función de costo")
plt.xlabel("Épocas")
plt.ylabel("J")
plt.title("Comportamiento de J")
plt.legend()
plt.show()