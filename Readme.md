# Proyectos de Inteligencia Artificial(IA) 🤖

En este repositorio encontraras todos aquellos proyectos que he ido realizando mientras estudiaba el curso de Samsung orientado a Inteligencia Artificial.
Os muestro alguno de los que me siento más orgullosa:

## Categorización de números
Con el famoso dataset de MNIST reducido usando técnicas de Machine Learning, en concreto usando K-means.

Se realizaron técnicas de aumento de datos, en base a la rotación de los números:

![imagen](https://user-images.githubusercontent.com/47080611/155223189-dee82629-e817-4cc5-977a-5217114f1bb4.png)

Se calculo el número optimo de K para este dataset:

![imagen](https://user-images.githubusercontent.com/47080611/155223285-b1858c33-b43b-4c6e-af4c-3f596959d01f.png)

Llegando a un accuracy del 68% debido a que al ser un MNIST reducido, teniamos pocos datos de ciertos numeros:

![imagen](https://user-images.githubusercontent.com/47080611/155223422-17c894d9-0278-426c-917c-76314a2465bf.png)

## Estmiación de los costes médicos
En este caso se debía averiguar según datos personales, cual sería el coste médico para la aseguradora de dicha persona.
Se usaron ambas técnicas, tanto Machine Learning como Deep Learning, dando mejores resultados ML.

Datos antes de ser preprocesados:

![imagen](https://user-images.githubusercontent.com/47080611/155224007-8adb2843-41d4-47cd-88cc-9be67bb94aa7.png)


Datos después de ser preprocesados, realizando pasos de normalización de variables y eliminación de nulos:

![imagen](https://user-images.githubusercontent.com/47080611/155224186-a93a9c56-8e17-4f36-aa0e-5799e67536b5.png)

Llegando a ser mi mejor modelo con Polynomial Regression, alcalzando un score de 85%

![imagen](https://user-images.githubusercontent.com/47080611/155224397-f00f65ca-7688-47da-af20-7394a434f7e3.png)

También a destacar Random Forest Regressor que obtuvo resultados parecidos, usando en este caso técnicas con GridSearch para encontrar la mejor convinación de parámetros:

![imagen](https://user-images.githubusercontent.com/47080611/155224519-83356e14-3ed6-41a6-9e7d-c97ea05db960.png)

Para el mismo problema pero con técnicas de DL, usando función de activación RELU se obtuvieron peores resultados:

![imagen](https://user-images.githubusercontent.com/47080611/155224811-07fadcf4-f7c4-4b64-9e5e-ed2b233afa39.png)



