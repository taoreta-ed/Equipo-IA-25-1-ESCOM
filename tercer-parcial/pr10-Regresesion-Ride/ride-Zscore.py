import numpy as np
import matplotlib.pyplot as plt

#Fase de entrenamiento
#Definición de los datos de entrada
X_no_norm = np.array([[2019,4], [2020,2], [2021,4], [2022,4], [2023,2], [2024,4]]) #Año y segunda caracteristica (número de puertas)
#Etiquetas de salida
yd = np.array([4, 5, 6.5, 7, 8.5, 12])

#Normalización usando Z-score
def normalizacion_zscore(X):
    media = np.mean(X, axis=0)
    desviacion = np.std(X, axis=0)
    return (X - media)/desviacion, media, desviacion

def normalizacion_minmax(X):
    x_max = np.max(X, axis=0)
    x_min = np.min(X, axis=0)
    return (X - x_min)/(x_max - x_min), x_min, x_max

def normalizacion_decimal(X):
    J = np.ceil(np.log10(np.max(np.abs(X), axis=0)))
    scale = 10**J
    return X/scale, np.zeros_like(J), scale

def normalizacion_log(X):
    offset = np.min(X, axis=0)
    #Aseguramos valores positivos sumando el mínmo + 1
    X_shifted = X - offset + 1
    return np.log(X_shifted), offset, None

def normalizacion_robust(X):
    mediana = np.median(X, axis=0)
    q75, q25 = np.percentile(X, [75, 25], axis=0)
    iqr = q75 - q25
    return (X - mediana)/iqr, mediana, iqr

def main():
    #Normalizar las caracteristicas
    X, media, desviacion = normalizacion_zscore(X_no_norm) #Normalizar el dato de entrada para zscore
    #X, x_min, x_max = normalizacion_minmax(X_no_norm) #Normalizar el dato de entrada para minmax
    #X, offset, _ = normalizacion_log(X_no_norm) #Normalizar el dato de entrada para log
    #X, mediana, iqr = normalizacion_robust(X_no_norm) #Normalizar el dato de entrada para robust
    #X, _, scale = normalizacion_decimal(X_no_norm) #Normalizar el dato de entrada para decimal
    #X = X_no_norm #Sin normalización

    #Definición de hiperparámetros
    lr = 0.01 #Tasa de aprendizaje
    max_epocas = 20000 #Número de iteraciones
    epsilon = 1e-6 #Criterio de paro
    b = np.random.rand(3) #Inicialización de los parámetros (b0, b1 y b2)
    lamda = 0 #Factor de regularización
    m = len(X) #Número de muestras
    grafica = []

    #Entrenamiento con Early Stop
    early_stop_epoch = max_epocas
    for epoch in range(max_epocas):
        #Calcular Y obtenido
        Yobt = b[0] + b[1]*X[:,0] + b[2]*X[:,1]

        #Calcular el Error Cuadrático Medio
        J = (1 / (2*m)) * np.sum((yd - Yobt)**2) + (lamda / (2*m)) * np.sum(b[1:]**2)
        grafica += [J]

        #Verificar Early Stop
        if J < epsilon:
            early_stop_epoch = epoch + 1
            break

        #Gradiente descendente
        b[0] -= (lr/m) * np.sum(Yobt - yd)
        b[1] -= (lr/m) * np.sum((Yobt - yd) * X[:, 0]) + (lamda/m) * b[1]
        b[2] -= (lr/m) * np.sum((Yobt - yd) * X[:, 1]) + (lamda/m) * b[2]

    #Resultados del entrenamiento
    print(f"Parámetros finales b0 = {b[0]}, b1 = {b[1]}, b2 = {b[2]}")
    print(f"Épocas ejecutadas: {early_stop_epoch}")

    #Graficar la función de costo
    plt.figure(figsize=(8,6))
    plt.plot(range(len(grafica)), grafica, label="Función de costo")
    plt.xlabel("Épocas")
    plt.ylabel("J (ECM)")
    plt.title("Comportamiento de J")
    plt.legend()
    plt.show()

    #Fase de operación: Para hacer estimaciones
    X_test = np.array([[2025, 4]]) #Año y segunda caracteristica
    X_test_norm = (X_test - media)/desviacion #Normalizar el dato de prueba para zscore
    #X_test_norm = (X_test - x_min)/(x_max - x_min) #Normalizar el dato de prueba para minmax
    #X_test_norm = np.log(X_test - offset + 1) #Normalizar el dato de prueba para log
    #X_test_norm = (X_test - mediana)/iqr #Normalizar el dato de prueba para robust
    #X_test_norm = X_test/scale #Normalizar el dato de prueba para decimal
    X_test_norm = X_test_norm.reshape(1, -1) #Ajustar la forma del dato de prueba

    Y_test = b[0] + b[1]*X_test_norm[0,0] + b[2]*X_test_norm[0,1]
    print(f"Para el año {X_test[0,0]} con característica adicional {X_test[0,1]} se estiman {Y_test:.2f} millones de ventas de coches")

main()