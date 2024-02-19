---
title: Ejemplos con PSeint
author: Alejandro Leyva
---

![banner micro](https://www.alejandro-leyva.com/micro-21/web/imgs/banner.png)

# Ejemplos con PSeint

Ejemplos explicados y resueltos en clase

## Hola mundo

Mandar un mensaje a la pantalla 

### Código PSeint

```python
Algoritmo saludo
	Escribir "Hola mundo"
FinAlgoritmo
```
### Diagrama de flujo

![saludo](assets/saludo.png)

## Calculadora Suma

Realizar una calculadora que sume 2 números, solicitándolos al usuario

### Código PSeint

```python
Algoritmo Calculadora_suma
	Escribir '================================'
	Escribir 'Calculadora que suma 2 números'
	Escribir '================================'
	Escribir 'Dar un valor'
	Leer valor1
	Escribir 'Dar otro valor'
	Leer valor2
	Escribir  'Dar otro valor'
	Leer valor3
	suma <- valor1+valor2 + valor3
	Escribir 'El resultado de la suma es: ',suma
	multiplicacion = valor1 * valor2 * valor3
	Escribir 'El resultado de la multip es: ',multiplicacion
FinAlgoritmo

```
### Diagrama de flujo

![saludo](assets/Calculadora_suma.png)

## Calculadora de perímetro rectángulo    

un programa para calcular el perímetro del rectángulo, solicitándole al usuario sus lados  e imprimir el resultado, con el siguiente  formato (ejemplo) "El perímetro del rectángulo es 13.4 unidades", después que entregue el área 

### Código PSeint

```python
Algoritmo calculadora_rectangulo
	Escribir "Calculadora del rectangulo"
	Escribir  "Dar el valor de la base"
	Leer base
	Escribir  "Dar el valor de la altura"
	Leer altura
	perimetro = (2*base) + (2*altura)
	area = base * altura
	Escribir  "El perimetro es ", perimetro, " unidades"
	Escribir "El area es ", area, " unidades cuadradas" 
FinAlgoritmo
```
### Diagrama de flujo

![saludo](assets/calculadora_rectangulo.png)

## Mascotas

Realizar un programa que le solicite al usuario, cuantas mascotas tiene, en caso que tenga 3 o mas le darás el mensaje "Eres amantes de los animales", sino le dirás "necesitas un gatito"

### Código PSeint

```python
Algoritmo Mascotas_
	
	Escribir 'Dar la cantidad de mascotas'
	Leer mascotas
	
	Si mascotas >= 3 Entonces
		Escribir 'Eres amantes de los animales'
	SiNo
		Escribir 'necesitas un gatito'
	FinSi
	
FinAlgoritmo

```
### Diagrama de flujo

![saludo](assets/mascotas.png)

## Calculadora Área/Perímetro Cuadrado  

Realizar un programa que calcule el area o perímetro del cuadrado, dependiendo de la respuesta solicitar los datos e imprimir el resultado

### Código PSeint

```python
Algoritmo calculadora_perimetro_area_cuadrado
	lado = 0 //la variable que usare para guardar la información
	Escribir "Calculadora del Cuadrado"
	Escribir "1) Perimetro"
	Escribir "2) Area"
	Leer opcion
	
	Escribir "Dar el valor del lado"
	Leer lado
	
	Si opcion == 1 Entonces
		perimetro = lado *4
		Escribir "El perimetro es: ", perimetro
	SiNo
		area = lado * lado
		Escribir "El area es: ", area
	FinSi
FinAlgoritmo
```
### Diagrama de flujo

![saludo](assets/calculadora_perimetro_area_cuadrado.png)

## Calculadora Cuadrado con opción de salir y mensaje de error

### Código PSeint

```python
Algoritmo Calculadora_Cuadrado
	Escribir 'Calculadora Cuadrado'
	Escribir '1) Area'
	Escribir '2) Perímetro'
	Escribir '3) Salir'
	Leer opcion
	Si opcion==1 Entonces
		Escribir 'Dar lado'
		Leer lado
		Escribir 'El Area es: ',(lado*lado)
	SiNo
		Si opcion==2 Entonces
			Escribir 'Dar lado'
			Leer lado
			Escribir 'El Perímetro es: ',(lado*4)
		SiNo
			Si opcion==3 Entonces
				Escribir 'Hasta la proxima inge'
			SiNo
				Escribir 'La opcion no existe'
			FinSi
		FinSi
	FinSi
FinAlgoritmo
```
### Diagrama de flujo

![saludo](assets/Calculadora_Cuadrado_opcion_salir.png)

## Mensaje con base a calificación (operador lógico)

### Código PSeint

```python
Algoritmo operador_logico
	
	Escribir "Da tu calificacion"
	Leer calificacion
	
	Si calificacion<= 10 Y calificacion >=6 Entonces
		Escribir "Pasaste"
	SiNo
		Si calificacion <6 Y calificacion >=0 Entonces
			Escribir "Te veo en recursa"
			
		SiNo
			Escribir "Calificacion no valida"
		FinSi
	FinSi
FinAlgoritmo
```
### Diagrama de flujo

![saludo](assets/calificacion_logico.png)

