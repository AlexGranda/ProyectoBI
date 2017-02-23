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

* [Python 2.7](https://www.python.org/) - Lenguaje utilziado.
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

* Harvers () - Recolector de Tweets

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

### Procesamiento de Datos

Con la vista pre-procesada y con tweets únicamente de Ecuador, lugar de donde se realizará el análisis de los datos, se debe procesar el campo Text para poder analizar la opinión pública desde su contexto original. El procesamiento de los datos involucra la eliminación de links, emoticones y tags, en el caso de los tags no deben borrarse completamente, por el contrario, solo eliminar el carácter “#”. La siguiente parte del procesamiento es la clasificación de los tweets según su contexto donde puede ser positivo, negativo, y neutro.
