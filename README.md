
Hi there!

Abordaje del ejercicio.

Primero me enfoqué en el algoritmo de asignación de tareas. Me pareció que se asemejaba al problema del set packing (a algún tipo de la familia de los set packing problems https://en.wikipedia.org/wiki/Set_packing).
Código: https://github.com/TomCastagnino/satellites/blob/main/ground_control/consumers/earth_utils.py

Lo que hice fue primero ordenar la lista de tareas según su peso (pay_off / número de  recursos usados). Para eso usé sorted(). Por lo tanto, la complejidad de mi función sort_task_list() es O(n log n).

Una vez que la lista de tareas está ordenada, uso distribute_task() para asignar la mayor cantidad de tareas posibles a cada satélite. Para eso chequeo que los conjuntos de recursos asignados del satélite y los recursos de la tarea sean disjuntos. Suponiendo que la cantidad de recursos totales es despreciable y puede realizarse en tiempo constante, la complejidad de la función sería O(n) en función de len(tareas).

(Nota: distribute_task() devuelve una lista nueva, no modifica la existente. Dentro de lo posible, intento que las funciones sean puras.)

El último paso es repetir distribute_task() por el número de satélites. Considerando que el objetivo de Satellogic es tener 300 satélitese para el 2025, supongo que este número puede tomarse como una constante.

Este algoritmo no es dependiente ni del número de recursos ni del número de satélites. Sí estoy asumiendo que todos los satélites cuentan con los mismos recursos.

Posible mejora: si conociera los recursos disponibles de casa satélite, podría hacer el algoritmo más eficiente al salir del loop cada vez que los recursos totales del satélite estén ocupados.

En cuanto a la arquitectura, decidí usar django-channels con Redis y docker. Nunca había usado ese stack. Otras opciones que evalué fueron usar Celery y RabbitMQ. También pensé en usar AWS.

Funcionamiento de la app:

Instalar Docker y correr: $ docker run -p 6379:6379 -d redis:5

Ir a localhost:8000/ground_control y seleccionar el número de satélites:

![alt text](0_satellogic.png)

Al ser redirigido a la siguiente pantalla, hay un ejemplo ya cargado. El ejemplo se puede modificar, siempre y cuando se respete la misma estructura del JSON y se mantengan las Keys.

![alt text](1_satellogic.png)

Apretar 'send'. Para borrar los registros, CTRL + F5

![alt text](2_satellogic.png)

Para el desarrollo, me basé en https://channels.readthedocs.io/en/stable/tutorial/part_1.html