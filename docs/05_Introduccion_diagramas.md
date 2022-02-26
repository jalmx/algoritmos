# Introducción a creación de Diagramas de flujo

Aquí comenzaremos a construir diagramas de flujo básicos. Construidos parte por parte.

!!! example "Ejemplo"
    **1. Se debe realizar un diagrama de flujo que sume 2 números enteros, estos números deben estar almacenados en memoria; es decir, en variables. El resultado enviarlo a la pantalla.**

Con base a las instrucciones, entendemos que los valores pueden ser cuales quiera, deben estar almacenados en el programa.

Primero debemos comenzar con el símbolo de *INICIO*

![part1](./img/e1_p0.png)

Tomando las instrucciones nos dice que debemos tomar definir un valor, el que nosotros querramos, en memoria para sumarlo con otro, por lo tanto, aplicamos un proceso declarando la primera variable `variable1` y le asignamos un valor; en esta caso le asignamos el valor de `10`. El símbolo de `Proceso` (Rectángulo) se usa para realizar una operación matemática, asignación de valor a una variable o declaración de una variable.

*Se utiliza el signo de igual (=) para asignación de un valor a una variable.*

![part1](./img/e1_p1.png)

Ahora debemos declarar otro variable, en este caso la llamaremos `valor2`, recordemos que el nombre de la variable es el que escojamos. *En una sección previa se indican las reglas para declaración de variables*.
A nuestra variable `variable2` le asignamos el valor de `5`. Como estamos realizando una asignación de un valor a una variable, utilizamos el símbolo de `Proceso` (Rectángulo).

![part1](./img/e1_p2.png)

Acto seguido es realizar la operación aritmética de suma. Para ello esto lo realizamos en un `Proceso` y lo guardamos en una variable llamada `suma`.

![suma](./img/e1_p3.png)

Ya que tenemos el resultado guardado en la variable `suma`, lo mandaremos a la pantalla (Display).

![resultado](./img/e1_p4.png)

Hemos terminado de realizar lo solicitado, por lo tanto, debemos terminar nuestro diagrama de flujo, con el símbolo de `FIN`

![resultado](./img/e1_p5.png)

!!! example "Ejemplo"
    **2. Realizar la suma de dos números enteros, solicitándolos al usuario y al final imprimir por pantalla el resultado.**

Con base a las instrucciones debemos solicitar al usuario los números, pero primero le tenemos que indicar que debe hacer, y debemos guardar este valor en una variable cada uno para poder realizar la operación correspondiente.

Como todo diagrama de flujo comenzamos con el símbolo de *INICIO*

![inicio](./img/e2_p1.png)

Tenemos que indicarle al usuario qué debe realizar, para realizar esto debemos utilizar el símbolo para enviar mensajes a la pantalla con el mensaje. *Los textos que queremos que se muestre debe ir entre dobles comillas `" "`*. El mensaje que mostraremos es `"Dar el primer numero entero"`

![inicio](./img/e2_p2.png)

Ahora debemos recibir el dato que el usuario quiere ingresar, este numero lo debemos guardar en algún lado, por lo tanto, declaramos una variable dentro del símbolo que es para ingresar datos. La variable la llamamos `variable1`

![inicio](./img/e2_p3.png)

Ya que tenemos el primer valor, debemos solicitar al segundo valor, para ello debemos mandar el segundo mensaje indicándole al usuario qué debe realizar, el mensaje será `"Dar el segundo numero entero"` dentro del símbolo de `Display`

![inicio](./img/e2_p4.png)

Debemos recibir el siguiente valor y almacenarlo en otra variable, la llamaremos `valor2`, para poder ingresar el valor a esta variable tenemos que ocupar el símbolo de entrada de datos.

![inicio](./img/e2_p5.png)

Contamos con los valores que ingreso el usuario en las variables `valor1` y `valor2`, ahora debemos realizar la operación y la guardaremos en la variable `suma`.

![inicio](./img/e2_p6.png)

El resultado de la operación esta almacenada en la variable `suma`, la debemos envíar a la pantalla, tenemos que usar el símbolo de `Display`, la variable

![inicio](./img/e2_p7.png)

Hemos terminado lo que nos fue solicitado, por lo tanto, solo nos queda finalizar el diagrama de flujo con *FIN*

![inicio](./img/e2_p8.png)

