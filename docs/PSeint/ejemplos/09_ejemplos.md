# Ejemplos

## Calculadora suma de 2 números

```python
Algoritmo Calculadora_suma
	Escribir '================================'
	Escribir 'Calculadora que suma 2 numeros'
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

## Calculo factorial

```python
Algoritmo calcula_factorial
	Escribir 'Dar un número entero para calcular el factorial'
	Leer numero
	Si numero==0 O numero==1 Entonces
		Escribir 'El factorial es ',numero
	SiNo
		factorial <- 1
		contador <- numero
		Repetir
			factorial <- factorial*contador
			contador <- contador-1
		Hasta Que contador==1
		Escribir 'El factorial de ',numero,' es ',factorial
	FinSi
FinAlgoritmo

```

## Calculadora cuadrado

```python
Algoritmo Calculadora_Cuadrado
	Escribir 'Calculadora Cuadrado'
	Escribir '1) Area'
	Escribir '2) Perimetro'
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
			Escribir 'El Perimetro es: ',(lado*4)
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

## Calculadora con opcion de salir

```python
Algoritmo calculadora_infinita
	opcion <- 0
	Repetir
		Escribir '============================================================='
		Escribir 'Calculadora de suma o resta'
		Escribir '1) Sumar'
		Escribir '2) Restar'
		Escribir '3) Salir'
		Leer opcion
		Si opcion==3 Entonces
			Escribir 'Adiosito'
		SiNo
			Si opcion==1 Entonces
				Escribir 'Dar el primer numero'
				Leer a
				Escribir 'Dar el segundo numero'
				Leer b
				Escribir 'La suma es ',(a+b)
			SiNo
				Si opcion==2 Entonces
					Escribir 'Dar el primer numero'
					Leer a
					Escribir 'Dar el segundo numero'
					Leer b
					Escribir 'La resta es ',(a-b)
				SiNo
					Escribir 'La opcion no existe'
				FinSi
			FinSi
		FinSi
	Hasta Que opcion==3
FinAlgoritmo

```

## Calculadora perímetro y area del cuadrado

```python
Algoritmo calculadora_perimetro_area_cuadrado
	lado = 0 //la variable que usare para guardar la informacion
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

## Calculadora de perímetro y area del cuadrado

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

## Mensaje calificación - operador lógico  

```python
Algoritmo calificacion_op_logico
	Escribir "Dar la calificacion"
	Leer calificacion
	
	Si calificacion >= 6 Y calificacion <=10 Entonces
		Escribir "Pasaste"
	SiNo
		Si calificacion >=0 Y calificacion < 6 Entonces
			Escribir "Tronado"
		SiNo
			Escribir "No valido"
		FinSi
	FinSi
FinAlgoritmo
```


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

## Contador del 1 al 10

```python
Algoritmo contador_10	
	contador = 1
	Repetir
		Escribir contador
		contador = contador+1
	Hasta Que contador > 10
FinAlgoritmo
```

## Mensaje - ciclo

```python
Algoritmo Hola
	contador = 0
	Repetir
		//sección va todo lo que se va a Repetir
		Escribir " HOLA"
		contador = contador+1
	Hasta Que contador == 10 //comparación y si es falso se repite
	
FinAlgoritmo
```

## Mascotas

```python
Algoritmo Mascotas_
	
	Escribir 'Dar la cantidad de mascotas'
	Leer mascotas
	
	Si mascotas >= 3 Entonces
		Escribir 'Eres amantes de los animales'
	SiNo
		Escribir 'te  mas mascotas'
	FinSi
	
FinAlgoritmo

```

## Nadar o correr - Operador lógico

```python
Algoritmo nadar_correr_op_logico
	Escribir "Te gusta correr 1)Si 2)No"
	Leer a
	Escribir "Te gusta nadar 1)Si 2)No"
	Leer b
	
	Si a == 1 Y b == 1 Entonces
		Escribir  "Eres superman"
	SiNo
		Si a == 1 O b == 1 Entonces
			Escribir "Te falta mas punch"
		SiNo
			Escribir "Taz chobby"
		FinSi
	FinSi
FinAlgoritmo

```

## Calculo de promedio (ciclo)

```python
Algoritmo promedio_ciclo
	// Obtener el promedio de una materia,  
	// solicitando cada parcial (3)  imprimir el resultado (CON CICLOS)
	suma <- 0
	cal <- 1
	Repetir
		Escribir 'Dar la calificacion ',cal
		Leer parcial
		suma <- parcial+suma
		cal <- cal+1
	Hasta Que cal>3
	promedio <- suma/3
	
	Escribir 'Tu promedio es ',promedio
	
	Si promedio >= 6 Entonces
		Escribir "Pasaste"
	SiNo
		Escribir "Tronado"
	FinSi
FinAlgoritmo

```

## Tabla del 3

```python
Algoritmo tabla_3
	tabla = 3
	contador = 1
	Repetir 
		resultado = tabla * contador
		Escribir tabla " X " contador , " = ", resultado
		contador= contador+1
	Hasta Que contador > 10	
FinAlgoritmo

```

## Calculo de resistencia serie (infinito)

```python
Algoritmo resistencia_serie_infinita
	//Realizar una calculadora de para resistencia en seria, 
	//la cantidad de resistencias es ilimitada, el usuario decide 
	//cuando debe parar la solicitud de valores, es decir, para detener 
	//el programa se debe dar el valor de -1.
	resitenciaTotal = 0
	contador = 1
	Repetir
		Escribir "Dar la resistencia ", contador, ", para salir escribe -1"
		Leer resistencia
		
		Si resistencia <> -1 Entonces
			resitenciaTotal = resitenciaTotal + resistencia
			contador = contador +1
		FinSi
		
	Hasta Que resistencia == -1
	
	Escribir "La resistencia total de ", contador," en serie: ", resitenciaTotal ," ohms"
FinAlgoritmo

```

