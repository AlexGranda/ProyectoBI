

__author__ = 'elikary'

'''


 QUITO
==============
'''
import couchdb
import sys
import textblob
import os
import re
import json

from couchdb import view
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

URL = 'localhost'
db_name = 'tweetsbi'


'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')
try:
    print(db_name)
    db = server[db_name]
    print('success')

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()


train = [
    ('Bienvenidos albertitonovoa y djdiegocarvajal estamos esperando pa que nos escriban  Quito','pos'),
    ('Quien esta planeando ir a LollaAR desde Ecuador    ', 'neu'),
    ('Te hubieras ido antes   montanertwiter', 'neg'),
    ('Tanto que hacer y yo solo tengo sueno', 'neu'),
    ('Hermoso lugar Hotel Boutique Portal de Cantuna', 'pos'),
    ('Detesto cuando la gente quiere hacerme pasar por RADAR    angry', 'neg'),
    ('RB DiegoSans lindo muy lindo Saludos desde Quito-Ecuador', 'pos'),
    ('esta me da risa tu cara  AngeloValotta   RKARTISTA  50CosasSobreAVyRK ', 'pos'),
    ('La casa del rival, mas amarilla que nunca ', 'pos'),
    ('Asi o mas  gemelas wendycaviedes  Lov U    Quito, Ecuador ','pos'),
    ('lo mas bonito de esto es el porcentaje de la pila  AngeloValotta   RKARTISTA  50CosasSobreAVyRK ','pos'),
    ('No se dejen meter gato por liebre con este pajarito de Torres. Despues no vengan a decir que no se los dije ','neg'),
    ('Una inspiracion resumida en una sola.. palabra.Amor NsTe amo mi Chaparra.Te amo mi ','pos'),
    ('ANGELO ESTA GUAPOOOOOOOOO   RKARTISTA','pos'),
    ('No todo lo que brilla es oro','neg'),
    ('Atencion Ayacucho, Huancavelica, Pasco y Junin  Los invitamos a participar en el taller para emprendedores de la macrorregion centro.','neu'),
    ('PrendeteConFuego te informa la temperatura en Guayaquil: maxima 31C minima 26C marielaviteri','neu'),
    ('Farandula: Katherine Heigl y su esposo Josh Kelley reciben a su tercer hijo','pos'),
    ('azucenita BichitoFutbol muy amable','pos'),
    ('Ecuador: Se registra caida de ceniza en Napo','neg'),
    ('realmadrid hoy tenemos que gana con  goles','pos'),
    ('No puedes perder lo q nunca fue tuyo, ni retener a quien no quiere quedarse','neu'),
    ('Yo ya no se que prefiero.. que me odie de corazon o que me ame sin amor.','neg'),
    ('Mientras uno se hace mas viejo, menos gente tiene alrededor  Por que creen q la gente se casa ','neu'),
    ('Yo amo esa cancion, Soy yo  ','pos'),
    ('En este pais no se castiga la Corrupcion...se castiga la pobreza... Se gastaron 600MM para tanta injusticia.. ','neg'),
    ('Tienes que aprender a levantarte de la mesa cuando deja de servirse el amor','neg'),
    ('Solo yo confundo los dias en que me toca materias, me equivoco de deber, hago a ultima hora y me va excelente :D','pos'),
    ('Pequenito pedazo de mi corazon','pos'),
    ('PaolaElles Hermosa','pos'),
    ('Abigail21 21 NI MARIA DE LA TIENDA, SE SABE MI NOMBRE','neg'),
    ('Violentos hay en todos los equipos, esto es un tema cultural y de orden, las leyes para los violentos deben ser ejemplares NoMasViolencia','neg'),
    ('Despues de la tormenta, viene ti bendicion   Quito City, Ecuador','pos'),
    ('Nada mejor que una Cerveza....    ','pos'),
    ('TE SORPRENDi MIRANDO COMO UN BOBO MIENTRAS BAILABA SIN PAREJA Y SIN PARAR','neg'),
    ('Pontifex es te quedaste en blanco   ','neu'),
    ('EcuadorQuiereSuPrimeraCitaCNCO christophervele hermosos ojitos esperamos tenerlos de vuelta en tu pais CNCOmusic','pos'),
    ('Estoy destinada a estar atras de una pantalla siempre ahr.','neg'),
    ('Abigail21 21 lo mejorrrr, amarteeee','pos'),
    ('No quiero ver nada de eso blah,es tan aburrido o soy muy amargada ah.','neg'),
    ('Soy uno de los muertos de hambre, lo poco que tengo es por mi trabajo, no soy rico pues no he ocupado un cargo publico alguno como la M.V','neg'),
    ('alguien mas esta ansioso por el homenaje de manana a soycrismorena porque aca no damos mas de la emocion crecimos con ella y su magia','pos'),
    ('En un mundo de hipocritas, los sinceros somos los malos..','neg'),
    ('Quiero mas dias felices, por fa','pos'),
    ('Cortar cualquier vinculo que amargue mi vida.','pos'),
    ('Eli: Me encanta el apoyo que le das a Juanpa, te mereces todo con el','pos'),
    ('momentos locura club100  Quito - Sur 5 Esquinas ','pos'),
    ('laura PDC23 Y EL TUYOOOOO, OMGGGGG, ME ENCANTAAAA','pos'),
    ('geologia cascadalapiragua nanegal  Cascada La Piragua','neu'),
    ('HUBO UN TEMBLOR ACAAAAA','neg'),
    ('temblor en manabi','neg'),
    ('ME TRAUMA VER LAS REPLICAS SEGUIDA Y CERCA DE 5','neg'),
    ('Algo mas lindo que ser hincha es ser socio  HazteSocioBSC no lo dudes mas y asi apoyas a BarcelonaSCweb lg23','pos'),
    ('La musica en las venas se viene lo nuevo de El Chela esperalo elchela cumbialo music','pos'),
    ('betsabeeamaya  Ya es tu cumpleanooos, te deseo lo mejor del mundo  Vayase de rumba  Te quiero, bendiciones  Sebastian te felicitara ','pos'),
    ('te amo tanto JohannVera1 eres el mejor  ','pos'),
    ('San Martin y Esmeraldas  ECU911Reporta un accidente de transito, se coordina con ATMGuayaquil Salud CZ8','neg'),
    ('que asco que compartan articulos de ese senor progre xaflaginas enfermo de correismo','neg'),
    ('Un solo idolo tiene el Ecuador BarcelonaSC campeon.','pos'),
    ('AimeeMiranda25 hoy es mi cumpleanos','pos'),
    ('La verdad se corrompe tanto con la mentira como con el silencio.','neu'),
    ('Cuando alguien desea algo debe saber que corre riesgos y por eso la vida vale la pena.','neu'),
    ('Que lindo cuando las ideas fluyen.','pos'),
    ('Si veo una publicacion de el sobre la basura enserio que lo voy a borrar ojala que no','neg'),
    ('Las mujeres trabajan 39 dias mas al ano en promedio que los hombres, segun el Foro Economico Mundial ','neu'),
    ('Tomando energia para 48 horas de mucho trabajo.','neu'),
    ('Doy un paso adelante y me doy cuenta que los miedos corren mucho mas...','neu'),
    ('pocas personas son mis amigos, pero esas personas aunque solo las salude o ya no hable con ellos, son geniales, soy bendecida al tenerlos','pos'),
    ('Sismo se sintio fuerte en Manta segun nos informan los habitantes SismoEcuador','neg'),
    ('Porque me tienes, porque me puedes, porque me dueles como nadie me dolio...','neg'),
    ('JorgeGlas DeCaraAlFuturo ENTREVISTA','neu'),
    ('El insomnio no es tan pesado con buena musica....One (U2)','pos'),
    ('El invento del Cuy Enlatado...','neu'),
    ('No estoy de acuerdo con que vinculen a faustominoz en temas relacionados a su ex pareja, el debate debe ser serio y responder al problema','neg'),
    ('Un semestre mas... siete materias.... perdon pero donde me mato  ','neg'),
    ('En tus manos Dios ','pos'),
    ('Me preocupa que solo en mi refri haya ron con cola ','neg'),
    (' Como se puede robar la vida de un ser humano a cambio de comida, de una cama o de un auto  ','neu'),
    (' La mentira no hara pacto con quien anda en verdad  (Santa Teresa de Jesus)','neu'),
    ('Nunca voy a poder ser lo suficiente bueno para las personas.','neg'),
    ('TheTide enserio quieres que muera de emocion   , porque si es asi lo estas logrando ','pos'),
    ('Cuando los vemos asi es inevitable no llorar nos llenan el con sus canciones no creen','neg'),
    (' Para que quieres dos camaras en un telefono  Te lo explicamos con un iPhone 7 Plus, un LG G5 y...','neu'),
    ('Y acariciarte bajo la sombra de la enramada es como un sueno que a veces vive sobre mi almohada','neu'),
    ('Organizaciones sindicales marcharon en Quito para reclamar por recuperacion de derechos de los trabajadores','neu'),
    ('Paco Moncayo: A mi no me van a imponer el candidato a la Vicepresidencia, ni Jimmy Jairala, ni ninguno de ','neg'),
    ('FabryEstrellaP cual seria nuestro futuro     jajajaj practicando nuevas canciones para el repertorio Fabri  tqm  ','pos'),
    ('De quien es la musica de la Champions League  Y por que demonios creia que era de Queen ','neu'),
    ('Voy a ver un capitulo de cada serie que me recomiende Netflix cada vez que lo abro. Asi me atrevo a probar cosas nuevas.','neu'),
    ('CCoelloB RobertoRomanV Votar por la democracia via eluniversocom','neg'),
    ('nos da tanto orgullo laliespos canto hermoso LalienShowMatch la admiramos tanto','pos'),
    ('Seguimos recibiendo participantes MetallicaDC','neu'),
    ('Muy orgullosa de mi hermano rubenzavala70 eres un grande  Felicidades  MedialabUIO espacio de encuentro e innovac','pos'),
    ('Lo de menos son todos los secretos que intuyo huelo y toco y siempre te respeto','neu'),
    ('UN DiA A LA VEZ , UN DIA A LA VEZ Republica Del Salvador','neu'),
    ('rena MBI a quien quieres enganar renataa   a quien ','neg'),
    ('Vean y aprendan, las barras y la prensa acabaran por matar al futbol','neg'),
    ('lo de menos es que jamas me sobres que tu amor me enriquezca haciendome mas pobre','neg'),
    ('La que tiene conocimiento de todos mis pensamientos.','neu'),
    ('Lo triste y frustrante es que todavia hay muchos que siguen votando por PRI y siguen creyendo las mentiras del CORRUPTO de EP','neg'),
    ('Definitivamente mi universidad es unica la amo','pos')
]

test = [
    ('  MatiNarvaezJ yo no soy mala','neg'),
    ('EN LOJA, VIVIMOS UN CLIMA MUY LINDO','pos'),
    ('Yo amo esa cancion, Soy yo ','pos'),
    ('  Lito Caluga Jajajaja eso no es para mi ajajjaja','pos'),
    ('  larepublica ec CYNTHIA NO, NO TU TIEMPO TODAVIA NO','neg')
]

cl = NaiveBayesClassifier(train)

view = "vistaEC/vistaEC"

LIMIT_OF_DOCUMENTS = 1000

url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
url2= '(www\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
patron2 = re.compile('#|@|'+url+'|'+url2)


while len(db.view(view, limit=LIMIT_OF_DOCUMENTS)) > 0:
    for data in db.view(view, limit=LIMIT_OF_DOCUMENTS):
        json_data = {}
        json_data = db.get(data['id'])
        text_es = data['value'][2]
        #print(text_es)
        #text_en = text_es.translate(to="en")
        #polarity_value = text_es.sentiment.polarity * 100.0
        #polarity = ""
        #if polarity_value == 0:
        #    polarity = 'neutral'
        #elif polarity_value < 0:
        #    polarity = 'negative'
        #else:
        #    polarity = 'positive'
        #subjectivity = text_es.sentiment.subjectivity
        
        text_es = patron2.sub('', text_es)
        clasificacion = cl.classify(text_es)
        json_data['sentiment'] = clasificacion
        #print(json_data)
        #print(text_es)
        #print(json_data)
        #nuevo_json = '{id:'+str(data['id'])+',created_at:'+str(data['value'][0])+',country_code:'+str(data['value'][1])+',text:'+text_es+',user_id:'+str(data['value'][3])+',followers:'+str(data['value'][4])+'}'
        #json_nuevo = json.dumps(nuevo_json)
        print(json_data)

        try:
            db.save(json_data)
        except:
            print("Data repeated...")

