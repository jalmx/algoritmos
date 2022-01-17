# Variables

## Que es una variable?

Una variable desde el punto de vista computacional es un espacio en memoria. 
Desde el punto de vista matematico es un referencia o un nombre para un valor que desconocemos y puede tomar cualquier valor.
Entonces, que es al final, es una combinacion de ambas definiciones, es un espacio en memoria que puede almacenar un dato o datos, dependiento del tipo de variable o el tamaño de la variable.

## Qué es declarar una variable?

**La declaración de una variable es reservar un espacio en memoria de la computadora**.
La computadora tiene cierta cantandidad de memoria, la cual es repartida entre todos los programas y los propios procesos para ejecutar el sistema operativo. Cuando ejecutamos un programa, éste comienza reservar memoria para poder trabajar.
Entonces, al declarar variables estamos consumiendo memoria, la cual vamos a utilizar en algun momento, si estamos reservando el espacio significa que en algun otro momento necesitamos recuperar lo que hemos guardado para realizar otra operación, de lo contrario no necesitamos reservar memoria si el valor solo será utilizado una unica vez.

## Cómo nombrar una variable?

Dentro de la programación existen **buenas practicas** para declarar variables. Estas reglas se definen a lo largo del tiempo que ha evolucionado. Estas son las reglas genericas para (casi) todos lenguajes. 

- Deben comenzar en minúscula
- Se escriben en minúsculas, las variantes se dan cuando son más de dos palabras.
- Solo puede contener numeros al final.
- Sensibles a minúsculas y mayúsculas; es decir, si declaro una variable llamada `variable1` y otra llamada `Variable1`, para la computadora son variables o espacios de memoria distintos, aun que suenen igual, con el solo hecho de cambiar una letra, ya estamos hablando de una variable distinta.
- No pueden contener espacios entre letras o palabras
- No puede comenzar con números o símbolos
- No puede contener carácteres especiales, todos son caracteres especiales menos el abecedario ingles. Ejemplo: `!"·%&-+/()=?¿...`, los unicos simbolos permitidos son `$` y `_`.
- **El nombre debe ser descriptivo**; es decir, con solo leerlo podemos deducir qué hace o para qué fue declarada
- *(Regla especial):* Todo de escribe en ingles.
- *(Regla especial)*: Si se desea escribir una variable combinando dos palabras o más, se separarán con un guíon bajo, se aplica la convencion CamelCase, es decir, en lugar de usar el espacio la palbra debe continuar con letra mayuscula.
- Ejemplos:
    - `valor`
    - `valor1`
    - `valorUno`
    - `variableNueva`

Las convenciones de Camel Case y Snake Case no las menciona por el momento, porque aplican en función de un lenguale enconcreto, hasta el momento esto aplicará para diagramas de flujo, lo cual es algo generico y base.
