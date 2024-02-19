---
title: Ejercicios de Algoritmos
author: Alejandro Leyva
---

![banner micro](https://www.alejandro-leyva.com/micro-21/web/imgs/banner.png)

# Ejercicios de Algoritmos

Por default se da por sentado que se deben pedir los datos al usuario para poder realizar las operaciones que se solicitan. Puedes personalizar tus algoritmos con mensajes especiales al inicio y al final (dale tu toque personal).

## Básicos

1. Realizar un programa que realice el **cálculo de Fuerza** en la segunda Ley de Newton. La formula es ==$Fuerza = masa * aceleración$==. Solicitando los valores de masa y aceleración, e imprimir el resultado de la fuerza.
2. Realizar una calculadora que **convierta de centímetros a pulgadas**, solicitando el dato al usuario el valor en centímetros, e imprimir el resultado
3. Hacer una caja registradora, que reciba el valor del producto y al final entregue el costo total con IVA y sin IVA; es decir, En total es *\$18.35* y con IVA son *\$21.28*, recordar que el IVA es del *16%*

## Decisiones

1. Hacer una calculadora de **áreas geométricas**, las opciones son:
      - Área del cuadrado
      - Área del círculo
      - Área del triángulo
      - Con opción de salir del programa y al final imprimir el resultado con la frase "El área de la figura 'nombre' es"
2. Hacer una calculadora de **ley de ohms**, las opciones son:
    - Calcular resistencia
    - Calcular corriente
    - Calcular voltaje
    - Con opción de salir del programa y al final debe imprimir el resultado con la frase, =="El resultado es valor es: 5 V"==, con su unidad, es decir, en función de lo que debía calcular.
3. Solicitar al usuario su promedio actual, en valor entero, el algoritmo debe tomar la decisión con basé al número ingresado, y dar un mensaje (ver la tabla) (Es aplicando operadores lógicos)

      | Rango de calificación  | Mensaje a imprimir                        |
      | ---------------------- | ----------------------------------------- |
      | 0 a menor que 6        | "lastima margarito"                       |
      | 6 a menor que 7        | "Aplícate"                                |
      | 7 a menor que 8        | "Apenitas y la libraste, metele papí"     |
      | 8 a menor que 9        | "Bastante bien, puedes mejorar"           |
      | 9 a menor que 10       | "muy bien amiguito, te ganaste la cheve!" |
      | Igual a 10             | "Excelente, tu muy bien"                  |
      | Menor a 0 y mayor a 10 | "Calificación no posible"                 |

4. Cálculo de BMI (**Indice de Masa Corporal**) para peso y altura, indicando cual es tu BMI y en que nivel de obesidad te encuentras (*Ver tabla*). La formula es $BMI = peso (kg) * estatura^2 (cm)$. (Es aplicando operadores lógicos)
   
      | IMC                | Nivel de peso |
      | ------------------ | ------------- |
      | Por debajo de 18.5 | Bajo peso     |
      | 18.5 – 24.9        | Normal        |
      | 25.0 – 29.9        | Sobrepeso     |
      | 30.0 o más         | Obesidad      |

5. Mandar la letra del múltiplo o submultiple correspondiente, es decir, si el usuario ingresa el valor de 1,000, el valor que se debe desplegar por pantalla es la letra "K", si el usuario ingresa el valor de 0.02, se debe desplegar por pantalla la letra "m". (Es aplicando operadores lógicos).<br> *Nota: Si usas `PSeint` no soporta números tan pequeños, hazlo hasta `nano`; sin embargo, si lo haces a mano no hay ningún problema de limitaciones de números.*
      
      | Unidad | Letra |    Valor    |
      | ------ | :---: | :---------: |
      | pico   | **p** | $x10^{-12}$ |
      | nano   | **n** | $x10^{-9}$  |
      | micro  | **u** | $x10^{-6}$  |
      | mili   | **m** | $x10^{-3}$  |
      | unidad |       |      1      |
      | kilo   | **K** |  $x10^{3}$  |
      | mega   | **M** |  $x10^{6}$  |
      | giga   | **G** |  $x10^{9}$  |

## Ciclos

Los siguientes ejercicios se debe aplicar ciclos, de lo contrario no se toma correcto el diagrama aun así resuelva lo solicitado.

1. Imprimir del 1 al 99
2. Leer 10 números enteros, solicitando uno a uno al usuario, e imprimir al final cuántos fueron par y cuántos impar.
3. Solicitar al usuario 5 números, uno a uno, ir sumando los números pares e imprimir el resultado de la suma
4.  **Calculadora de la segunda ley de Newton**. Tiene el menú indicando que desea calcular (fuerza, masa o aceleración) y la opción de salir. Después solicita al usuario los valores e imprimir el resultado, debe regresar al menú inicial, para volver a calcular otra cosa, solo si da la opción de salir, termina el programa. Si da una opción incorrecta, muestra un mensaje de error y vuelve a mostrar el menu.
5. Calcular la potencia de un número, solicita al usuario el número que desea elevar y después la base a la cuál lo elevara. Ejemplo: *==2^2= 4, 2^3=8==*
6. Leer 10 números, solicitando uno a uno al usuario, y al final se imprime por pantalla el número más alto ingresado de los 10.
7. Cálculo de la **media de un conjunto de datos**. Se le pregunta al usuario **cuantos números son**, comienza a pedirlos uno a uno y al final imprime el resultado de la media de todos los datos.
8. Cálculo de la **media de un conjunto de datos positivos**. En cada iteración **pregunta al usuario si quiere terminar** para conocer el resultado o ingresar otro valor. Cuando elija terminar, imprimir el valor total del promedio o media.
9. Imprimir la tabla de multiplicar que el usuario elija y también el usuario elije hasta que numero termina. Es decir, si da quiere la tabla del 15, y quiere ver hasta el 200, pues la ultima operación que vea por pantalla sera *15x200=3000*
10. Algoritmo para convertir número decimal a binario, debe ir mostrando el numero en binario uno a uno, no es todo el numero binario completo, comenzando por el bit mas significativo. Por ejemplo el usuario ingresa el valor de 95, debe imprimir 11111001. Dado que 5 en binario es 1011111. Investigar como hace la conversión.
11. Una pastelería nos solicita realizar un programa para una maquina de pastelitos, las opciones son las siguientes

      ![esquema](img/diagra1.svg)

    - Debe ir sumando las opciones que elije que elija el usuario. Pero cada vez que termine de elegir, debe volver a mostrar el menú, hasta que el usuario elija terminar debe imprimir la cantidad total a pagar. El usuario en cualquier momento puede terminar la orden y la maquina debe darle la cantidad a pagar.
    - Por ejemplo, al inicio muestra el menu de pastel, cupcake y salir. Si elije, pastel, ahora le muestra las opciones de chocolate, vainilla, natural y salir, el usuario elije vainilla, y por ultimo elije chispas, debe preguntar si añade algo mas, si es asi, vuelve a mostrar el menu inicial. En caso que elija que ya termino, debe imprimir la cantidad que debe pagar, es decir, (5+1+0.5) "Cantidad a pagar \$6.5".
    - Recuerda el usuario puede salir en cualquier momento y debe recibir la cantidad que debe pagar.
