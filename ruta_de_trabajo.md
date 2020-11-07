# Aterrizando la ruta de trabajo

- Terminemos el [schema.md](https://github.com/CodeandoMexico/representantes-patito-2/blob/master/schema.md)
- Empecemos el frontend

## Cómo finalizar el schema.md

**Definición:** 
El schema es el documento que detalla la estructura de las tablas en una base de datos y el formato de los datos que rellenarán esas tablas, así como las relaciones entre las mismas (Ej: Una bancada tiene a muchos diputados y un diputado pertenece a una bancada). Terminar el schema significa que terminaremos una propuesta de un estándar de datos, y le permitirá a los desarrolladores que hacen el API a diseñarla.

**Contexto de esta tarea:**
En [schema.md](https://github.com/CodeandoMexico/representantes-patito-2/blob/master/schema.md) se encuentra la propuesta inicial de Representantes Patito para modelar los datos. El Congreso del estado de Guanajuato tiene una propuesta más avanzada de software que maneja la actividad legislativa. Tenemos una lista de endpoints (ligas de consulta de la base de datos) que tiran la estructura pública de la base de datos en formato JSON. Podemos nutrir la propuesta original de schema con los datos del API de Congreso de Guanajuato.

**¿Cómo estructuramos esta tarea?:**

**Objetivo:** Actualizar el [schema.md](https://github.com/CodeandoMexico/representantes-patito-2/blob/master/schema.md) con las tablas de GTO

1. Tarea: Validar con GTO qué tablas faltan
2. Tarea: Llenar en Github cada tarea de validar las tablas de GTO y sus campos con el schema (una tarea por tabla)
3. Propuesta: Proponer una fecha y una dinámica de definición de tablas externa para que otros puedan participar - **pospuesto**
4. Propuesta: Proponer una fecha y dinámica de definición de tablas interna (al interior de la comunidad de Codeando) para que otros puedan participar


### Endpoints GTO

- [X] Listado de Leyes:
`GET http://www.congresogto.gob.mx/leyes.json`

- [X] Listado de Códigos:
`GET http://www.congresogto.gob.mx/codigos.json`

- [ ] Listado de Reglamentos:
`GET http://www.congresogto.gob.mx/reglamentos.json`

- [ ] Listado de Iniciativas a Consulta:
`GET http://www.congresogto.gob.mx/iniciativas/a_consulta.json`

- [ ] Listado de Iniciativas No Dictaminadas:
`GET http://www.congresogto.gob.mx/iniciativas/no_dictaminadas.json`

- [ ] Listado de Dictamenes en Pleno:
`GET http://www.congresogto.gob.mx/dictamenes/dictamenes_api.json`

- [ ] Listado de todas la Iniciativas (en revisión):
`GET http://www.congresogto.gob.mx/iniciativas/iniciativas_api.json`

- [ ] Listado de Ordenes (en revisión):
`GET http://www.congresogto.gob.mx/ordenes/ordenes_api.json`

- [ ] Detalle de la Orden/Reunion (en revisión):
`GET http://www.congresogto.gob.mx/ordenes/780/orden_api.json`

- [ ] Listado de Dictamenes en comisiones (en revisión):
`GET http://www.congresogto.gob.mx/dictamenes_comisiones/dictamenes_comisiones_api.json`

- [ ] Listado de Decretos:
`GET https://www.congresogto.gob.mx/decretos.json`

- [x] Listado de Comisiones de la Legislatura Actual:
`GET https://www.congresogto.gob.mx/comisiones/comisiones_api.json`

- [x] Cabilderos Personas Físicas:
`GET http://www.congresogto.gob.mx/cabildero_fisicas/personas_fisicas_api.json`

- [x] Cabilderos Personas Morales:
`GET http://www.congresogto.gob.mx/cabildero_morales/personas_morales_api.json`



## Frontend

**Contexto:**  
Como está descrito en el README, uno de los productos que salen de este proyecto es una forma de visualizar los datos. A esta parte le llamamos __Front-end__ es una página web que consume el API y despliega los datos de forma intuitiva.

**Problema:**
El fin de este proyecto es acercar el trabajo legislativo a la sociedad, por tanto, es crucial crear herramientas amigables que ayuden a buscar fácilmente la información requerida.
El Front-end debe cumplir con ser:
- Intuitivo (user-experience)
- Consistente (componentizable)
- Accesible (toma en cuenta las necesidades especiales del usuario)


- **Tarea:** Definir una dinámica para hacer un sprint de diseño de donde salgan todas las historias de usuario para esta aplicación.


## Scrapers

**Contexto:**
Para la obtención de la data de representantes perteneciente a cada entidad federativa, se desarrollarán web crawlers que ejecutan acciones encargadas de extraer de forma automática la información contenida en la estructura de los sitios web correspondientes. 

**Tareas:**
- Puedes desarrollar una web crawler para la entidad federativa de tu preferencia, basándote en el schema establecido. Para el desarrollo , puedes utilizar el lenguaje de tu preferencia, siempre y cuando puedas extraer la información y enviarla directamente al API del proyecto.
- Puedes desarrollar un pipeline general para agregar una araña y que ejecute el proceso completo de extraer y consumir el API para añadir información a la base de datos.
- Un buen punto de partida son los scrapers desarrollados por [unRob](https://github.com/unRob) en su repo original de [Representantes Pati.to](https://github.com/unRob/representantes.pati.to).


## API

**Contexto:**
Como motor del proyecto, hemos considerado el desarrollo de una API que sea capaz de conectar la funcionalidad del escribir en la base de datos (endpoint que se conecte con algún scraper), así como servir información al frontend.

Consideramos que una API se adecúa más a los requerimientos del proyecto, pues generaliza en una misma estructura el consumir el motor a través de sus endpoints para diferentes acciones internas con relación a la información que se trabaje.

**Tareas:**
- Puedes armar un CRUD básico con las tecnologías que se determinen a utilizar en el proyecto.
- Puedes crear la estructura de tablas determinada por el schema.
  - Puedes empezar con una o pocas tablas.
- Puedes crear endpoints base para las rutas asociadas a las vistas que se determinen en la sección de frontend.


## Preguntas en general

#### Contexto

En esta sección formularemos las preguntas e inquietudes generales en relación al proyecto; desde una perspectiva sobre los detalles de información legislativa a obtener y desplegar, hasta detalles técnicos sobre la estructura del proyecto y su desarrollo.

#### Q&A:

- **¿Los campos especificados a través del los endpoints del congreso de Gto. son suficientes?**
  No. Puede ser un primer saque pero necesitamos validaciones de otros estados y/o federal.
  
- **¿Quién será el usuario final de la aplicación?**
  X.
