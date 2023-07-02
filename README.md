# Rest2Graph

Rest2Graph es una herramienta con la que podrás obtener el código fuente del servidor de una API Graphql a partir de una especificación OAS de una API Rest. La herramienta se encuentra tanto desplegada con una [interfaz web](http://vicato.pythonanywhere.com/), como por medio de una interfaz de comandos.

Para poder ejecutar el proyecto solo necesitaremos de Python 3.8 o superior y tener instaladas todas las librerías de Python que se encuentran en el requirement.txt .

## ¿Cómo usar la herramineta por interfaz de comandos?

Para utilizar la interfaz de comandos deberemos de situarnos dentro de la carpeta 'python' y ejecutar el siguiente comando:

```(python)
python main.py --oas-path [ruta-oas] --destination-path [ruta-destino] (--config-file)
```
Las opciones del comando:

* --oas-path: obligatorio, indica la ruta de la especificación OAS.
* --destination-path: obligatorio, indica la ruta destino del código fuente resultante.
* --config-file: opcional, con esta opción indicamos sui queremos o no generar el fichero de configuración.

## ¿Cómo usar la herramienta por interfaz gráfica en local?

Para utilizar la interfaz de comandos deberemos de situarnos dentro de la carpeta 'webapp/r2graph' y ejecutar el siguiente comando:

```(python)
python main.py
```
o

```(python)
python flask --app main run
```

Y la tendriamos disponeble en http://localhost:5000.

## ¿Cómo lanzar el servidor Apollo?

Una vez tengamos el fichero zip extraeremos la carpeta ’sourceCode’ que se encuentra dentro del fichero. Y dentro de esa carpete ejecutaremos dos comados:

* ‘npm install‘: para instalar todas las dependencias necesarias de Node.js.
* ‘npm start‘: para lanzar el servidor Apollo en con la ruta ’http://localhost:4000’
