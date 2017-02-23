#ESCUELA POLITÉCNICA NACIONAL
#FACULTAD DE INGENIERÍA DE SISTEMAS
#INTELIGENCIA DE NEGOCIOS


##INTEGRANTES:
* Dávila David
* Granda Alexandra
* Unapanta Luis

##TEMA
Diseño e Implementación de un sistema clasificador de sentimientos para Política

## PROPÓSITO
El propósito del presente proyecto es la investigación e implementación del funcionamiento de un clasificador de sentimientos utilizando los algoritmos de aprendizaje vistos en la materia de Inteligencia de Negocios y los datos recolectados de Twitter desde octubre del 2016 para identificar tendencias de opinión sobre los candidatos presidenciales en el Ecuador.

## HERRAMIENTAS

* [Python 2.7](https://www.python.org/) - Lenguaje utilizado.
* [ElasticSearch](https://www.elastic.co/) - Herramienta de Map - Reduce.
* [Kibana](https://www.elastic.co/products/kibana) - Presentación de Gráficos.

## FASES DEL PROYECT0
* Adquisicion de Datos
* Pre-procesamiento de Datos
* Procesamiento de Datos
* Análisis de Datos
* Presentación de Datos

### Adquisición de Datos
Para la primera fase del proyecto se recolectó datos utilizando un cosechador de tweets entregado al inicio del curso a través del aula virtual. Para poder extraer tweets se establecieron las coordenadas correspondientes a la ciudad de Quito.
Las herramientas utilizadas para esta fase corresponden a un script codificado en Python, una base de datos noSQL como CouchDb y los utilitarios de Twitter para Python.

* [Harverster] (https://github.com/Rainini1/ProyectoBI/blob/master/harvester_uio%20(2).py) - Recolector de Tweets

### Pre-procesamiento de Datos

Antes de comenzar se debe tomar en cuenta que tendremos dos vistas, para el procesamiento de los tweets creamos una vista donde solo seleccionaremos los tweets de Ecuador, puesto que se identificó previamente que los tweets recolectados tienen información proveniente de otros países como Perú. Para esta vista solo utilizaremos dos campos:
   + Id: Identificador para ubicar los campos de la base principal.
   + Text: Texto del tweet para limpiar y clasificar.


Para la otra vista la utilizaremos para enviar la información de la base en CouchDB hacia ElasticSearch esta vista contendrá los siguientes campos:
   + Id: Identificador de tweet.
   + Created_at: Fecha y hora exacta de la creación del tweet.
   + Follower_count: Número de seguidores del usuario que realiazo el tweet.
   + Text: Información del tweet.
   + Sreen_name: Del campo User se extrae el nombre del usuario
   
   
* [Vistas] (https://github.com/Rainini1/ProyectoBI/blob/master/vistas.js) - Creación de vistas para CouchDB


### Procesamiento de Datos

Con la vista pre-procesada y con tweets únicamente de Ecuador, lugar de donde se realizará el análisis de los datos, se debe procesar el campo Text para poder analizar la opinión pública desde su contexto original. El procesamiento de los datos involucra la eliminación de links, emoticones y tags, en el caso de los tags no deben borrarse completamente, por el contrario, solo eliminar el carácter “#”. La siguiente parte del procesamiento es la clasificación de los tweets según su contexto donde puede ser positivo, negativo, y neutro.

* [Limpiador de Datos](https://github.com/Rainini1/ProyectoBI/blob/master/limpiador.py) - Archivo auxiliar para eliminar hashtags, URL's y numerales
#### Limpieza de Datos
Para limpiar el texto del tweet se utilizó un código en Python, ya que cuando manejamos texto en Python, una de las operaciones más comunes es la búsqueda de una subcadena; ya sea para obtener su posición en el texto o simplemente para comprobar si está presente. Por lo que para la busqueda de tags, emoticones, y links, para su posterior eliminación es necesario recurrir a las Expresiones Regulares, también conocidas como Patrones.
Para utilizar Expresiones Regulares, Python provee el módulo re. Importando este módulo podemos crear objetos de tipo patrón y generar objetos tipo matcher, que son los que contienen la información de la coincidencia del patrón en la cadena.
  
#### Clasificación de Datos
Para la clasificación de los tweets utilizamos una librería en Python

Utilizamos un clasificador Naive Bayes con 100 tweets totalmente limpios para el entrenamiento la cual clasifica el campo Text según los datos de entrenamiento en positivos, negativos y neutros. Ver figura 2. Esta clasificación le agregamos como un nuevo campo en nuestra base principal como Sentiment.

### Análisis de Datos
Para el análisis sobre el text de los tweets, para conocer la opción de los usuarios, la herramienta Elasticsearch nos permitirá realizar búsquedas sobre el texto del tweet. Elasticsearch es la herramienta que permite indexar y analizar en tiempo real grandes cantidades de datos. Realiza la búsqueda por texto gracias a un DSL y un Api para búsquedas más complicadas. ElasticSearch organiza la información en colecciones de documentos o Índices (index) y Tipos de Documentos (Type).
Elasticsearch a diferencia de otros sistemas, no necesita declarar un esquema de la información que añadimos, pero para sacar mayor partido a la información tendremos que añadir los llamados mappings que funcionan como un schema. Para nuestro caso crearemos un índice y su respectivo mapping con siguientes campos respetivos de la base de datos principal de tweets.

* [ElasticSearch](http://localhost:9200) - Local
* [Mapping](https://github.com/Rainini1/ProyectoBI/blob/master/mappings.txt) - Crear Indice

Luego de la creación del índice podemos visualizar el índice creado “tweets” especificando todos los campos creados, los tipos de datos deben coincidir con la base principal de los tweets.
Debemos pasar la vista con los respectivos campos especificados anteriormente de la Base en CouchDB hacia ElasticSearch donde se realizará la búsqueda y la presentación de los datos, para el paso de los datos usamos un comando curl.
Luego actualizamos el índice y observaremos toda la información de los tweets listos para la presentación.

### Presentación de Datos
Luego del análisis de los tweets necesitamos observar la tendencia de opinión de los candidatos/partidos por lo que usamos Kibana, que consiste en una interfaz de ElasticSearch muy sencilla. Dado que ElasticSearch dispone de una API ReST, Kibana consiste en una aplicación web dinámica en JavaScript que nos permite crear dashboards o realizar búsquedas de una forma muy amigable y permite generar gráficos según el análisis deseado. 
Por lo que contaremos con visualizaciones que permitan concluir lo siguiente: 
+	Impacto de las redes sociales (Twitter)
+	Impacto negativo y positivo en Twitter.
De las ventajas más llamativas de Kibana podemos destacar la integración con ElasticSearch o Logstash y la fácil utilización de la interfaz. 

Para poder acceder a Kibana, se ingresa a:
* [Kibana](http://localhost:9200) - Presentación de Gráficos.

Al tener creado el Index dentro de Kibana, en la pestaña Visualización creamos una nueva (Estilo Pastel o Barras), al seleccionar la fuente de datos escogemos una nueva: Tweets. Aquí definimos los parámetros de la consulta o se filtran los datos por algún termino o campo en particular.
