---
title: Practicas
author: Alejandro Leyva
---

![banner micro](https://www.alejandro-leyva.com/micro-21/web/imgs/banner.png)

# Practicas - Parcial 2

## Básicos

1. Realizar el calculo del perímetro de un rectángulo, solicitando el lado de la figura al usuario
2. Realizar el calculo del area de un cuadrado, solicitando el lado de la figura al usuario
3. Realizar un programa que realice el calculo de Fuerza en la segunda Ley de Newton. La formula es ==$Fuerza = masa * aceleracion$==
4. Realizar una calculadora que convierta de centímetros a pulgadas

## Decisiones

1. Realizar una calculadora básica, que realice la operación de sumar, restar, multiplicar, dividir. Al comenzar muestre un menu y el usuario elija la opción deseada. Se debe pedir el primer valor y el segundo, con ello realizar la operación
2. Solicitar un número entero al usuario, e imprimir por pantalla si es valor par o impar
3. Hacer una calculadora de áreas geométricas, las opciones son:
   - Área del cuadrado
   - Área del círculo
   - Área del triángulo
   - Con opción de salir del programa y al final imprimir el resultado con la frase "El área del figura nombre de la figura elegida es resultado"

4. Hacer una calculadora de ley de ohms, las opciones son:
   - Calcular resistencia
   - Calcular corriente
   - Calcular voltaje
   - Calcular potencia
   - Con opción de salir del programa y al final debe imprimir el resultado con la frase "El resultado es: "

5. Que resuelva una ecuación de segundo orden, aplicando la fórmula general; recuerda que no existen las raíces negativas. Debe entregarte los valores de las raíces o en caso que alguna o ninguna raíz exista, indicarlo. *==Nota: Debes usar las funciones matemáticas que vienen en el lenguaje==*
6. Realizar una calculadora de Teorema de Pitagoras, el usuario debe elegir, cateto opuesto, adyacente o hipotenusa, salir, que desear calcular. *==Nota: Debes usar las funciones matemáticas que vienen en el lenguaje==*
7. Hacer una caja registradora, que reciba el valor del producto y al final entregue el costo total con IVA y sin IVA; es decir, En total es *\$18.35* y con IVA son *\$21.28*, recordar que el IVA es del *16%*

## Operadores lógicos

1. Solicitar al usuario su promedio actual, en valor entero, el algoritmo debe tomar la decisión con basé al número ingresado; si es menor a 6, imprimir "lastima margarito", sí es igual a 6 y menor que 7 imprimir el mensaje "Aplicate", sí la calificación es igual a 7 y menor a 8, "Apenitas y la libraste, metele", si es igual a 8 y menos a 9, debe decir "Bastante bien, puedes mejorar" y sí la calificación es igual a 9 y menor que 10, decir "muy bien amiguito", y en caso de obtener 10 decirle al usuario "Excelente, tu muy bien". Si da un valor por encima de 10 o menor a 0, el mensaje dirá "Calificación no posible"
2. Calculo de BMI (Indice de Masa Corporal) para peso y altura, indicando cual es tu BMI y en que nivel de obesidad te encuentras (*Ver tabla*). La formula es $BMI = peso (kg) * estatura^2 (cm)$
   
      |IMC|Nivel de peso|
      |-|-|
      |Por debajo de 18.5	|Bajo peso|
      |18.5 – 24.9|	Normal|
      |25.0 – 29.9|	Sobrepeso|
      |30.0 o más	| Obesidad|

## Ciclos `while`

Todos estos ejercicios se debe implementar un ciclo `while`. No esta permitido hacer uso de las funciones propias del lenguaje que pueden resolver algún problema o alguna parte de el, a menos que lo indique en la instrucción.

1. Imprimir del 1 al 99.
2. Calcular el promedio final, solicita al usuario sus calificaciones parciales una a una, y al final da el mensaje "Aprobado", en caso que haya pasado arriba de 6 y "Estas en repite" si es menor. Considerando que son 3 parciales.
3. Imprimir la tabla del 8, desde ==*8x1=8 hasta 8x10=80*==.
4. Realizar un programa para visualizar la tabla de multiplicar que desee el usuario, el usuario dará el valor para la tabla, la tabla debe de ir desde el 1 hasta el 10, es decir, por ejemplo si da el numero 3, la tabla comienza en *==3x1=3 ... hasta 3x10=30==*
5. Realizar un programa para visualizar la tabla de multiplicar que desee el usuario, el usuario dará el valor para la tabla, también debe dar el limite donde comienza hasta donde termina, es decir, por ejemplo si da el numero 5, comenzando desde *==el 3 hasta el 25, comenzara la tabla 5x3 = 15 ... 5x25=125==*
6. Leer 10 números enteros, solicitando uno a uno al usuario, e imprimir al final cuántos fueron par y cuántos impar.
7. Calcular el factorial de un número entero. Se le solicita al usuario que ingrese un número entero el cuál quiere calcular el factorial del mismo. ==Ejemplo: 5! = 120==
8. Calcular la potencia de un número, solicita al usuario el número que desea elevar y después la base a la cuál lo elevara. Ejemplo: *==2^2= 4, 2^3=8==*
9. Leer 10 números, solicitando uno a uno al usuario, y al final se imprime por pantalla el número más alto ingresado de los 10.
10. Calculadora de la segunda ley de newton. Sale el menú indicando que desea calcular y la opción de salir. Después solicita al usuario los valores que conocé e imprimir el resultado, una vez termina de hacer todas las operaciones, debe regresar al menú inicial, debe existir una opción para terminal el programa, en caso que coloque una opción no existen, debe volver a mostrar el mensaje.
11. Cálculo de la media de un conjunto de datos. Se le pregunta al usuario cuantos números son, comienza a pedirlos uno a uno y al final imprime el resultado de la media de todos los datos.
12. Cálculo de la media de un conjunto de datos positivos. En cada iteración pregunta al usuario si quiere terminar para conocer el resultado o ingresar otro valor. Cuando elija terminar, imprimir el valor total del promedio o media.
13. Realizar un programa que solicite las calificaciones del parcial; es decir, irá pidiendo una a una las calificaciones, y al final que diga si te vas a *recursamiento o no* 
14. Algoritmo para convertir número decimal a binario, debe ir mostrando el numero en binario uno a uno, no es todo el numero binario completo, comenzando por el bit mas significativo. Por ejemplo el usuario ingresa el valor de 5, debe imprimir 101. Dado que 5 en binario es 101. Estos no son necesarios entregar, es para poner a prueba conocimientos

## Reto

- Realizar una calculadora de ley de Ohm, al inicio te da el menu para seleccionar que se desea calcular; para terminar el programa se debe dar la opción de salida, si no el programa sigue mostrando el menu inicial, si el usuario ingresa un valor y "no existe en el menu", manda mensaje que la opción no existe y vuelve a mostrar el menu. El resultado lo debe lanzar en el mejor formato, es decir, si el resultado es 1,000 ohms, en pantalla debe salir 1k, si es posible agregar el símbolo de Omega ($\Omega$) para resistencias. Si el resultado es 0.005A en pantalla debe salir 5mA. El usuario puede ingresar el valor a como se esta acostumbrado, es decir, el valor que ingresa es 5mA e internamente se obtenga el valor de 0.05 y se pueda realizar el calculo correspondiente

<!-- text autogenerated footer --><hr><blockquote>Facebook <a href="https://www.facebook.com/mecatronica85/" target="_blank">Mecatrónica 85</a></blockquote><blockquote>Realizado por <a href="https://www.alejandro-leyva.com" target="_blank">Alejandro Leyva</a></blockquote>