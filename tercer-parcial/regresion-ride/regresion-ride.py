import numpy as np
import matplotlib.pyplot as plt

#Fase de entrenamiento
#Definición de los datos de entrada
X = np.array([1,3,6,9,11,15,16,19,24])
#DataSet: Datos ocupados para hacer el entrenamiento
yd = np.array([4,5,6.5,7,8.5,12,13,16,22])

#Definición de hiperparámetros
lr = 0.01
epocas = 20000
b0 = 0.1                        #Se recomienda inicializar entre 0 y 1 de forma random
b1 = 0.1
#b = np.array(dimension = m)
lamda = 0
m = len(X)                      #Número de muestras
grafica = []

for epoch in range(epocas):
    Yobt = b0 + b1*X

    #Calcular el ECM (Error Cuadrático Medio)
    J = (1/(2*m))*np.sum((yd - Yobt)**2) + (lamda/2)*np.sum(b1**2)
    grafica += [J]
    #Calculo de b0 y b
    b0 = b0 - (lr/m)*np.sum(Yobt - yd)
    b1 = b1 - (lr/m)*np.sum((Yobt - yd)*X) + (lamda/m)*b1 #lamda*b1 

print(f"Parámetro b0 = {b0}")
print(f"Parámetro b1 = {b1}")

#Fase de operación: Para hacer estimaciones
#Definición de DataTest
x_test = float(input("Introduce el valor de x: "))
y_test = b0 + b1*x_test
print(f"El valor de y es: {y_test}")

#Clasificación 
x_test_clas = float(input("Introduce el valor de x para clasificar: "))
y_test_clas = float(input("Introduce el valor de y para clasificar: "))
y_obt_clas = b0 + b1*x_test_clas
if(y_obt_clas > y_test_clas):
    print("El punto está por encima de la recta")
else:
    print("El punto está por debajo de la recta")


#Graficar J
plt.figure(figsize=(8,6))
plt.plot(range(len(grafica)),grafica,label="Función de costo")
plt.xlabel("Épocas")
plt.ylabel("J")
plt.title("Comportamiento de J")
plt.legend()
plt.show()

plt.figure(figsize=(8,6))
for i in range(m):
    plt.scatter(X[i],yd[i])

x_val = [min(X),max(X)]
y_val = [(b0 + b1*x) for x in x_val]
plt.plot(x_val,y_val)
plt.show()
