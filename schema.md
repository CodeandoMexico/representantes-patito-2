# Actor
  ### (Diputado o Diputada) :
` Belongs to` **[Partido](#Partidos)**
` Belongs to` **[Legislatura](#Legislaturas)**
` Has many` **[Comisiones](#Comisiones)**
` Has and belongs to` **[Asistencias](#Asistencias)**  
` Has and belongs to` **[Iniciativas](#Iniciativas)**

  * cámara (a la que pertenece) [local, federal, senado] [ cadena ]
  * nombre [ cadena ]
  * apellido [ cadena ]
  * slug (nombre y apellido transliterado para búsquedas) [ cadena ]
  * distrito (`/^d[lf]-[1-3]{,1}\d-(\d{1,2}|rp|c[1-5])$/`) [ cadena ]
  * entidad [ numerico ]
  * género (0, 1 -- masculino/femenino) [ numerico ]
  * partido [ cadena ]
  * correo [ cadena ]
  * imagen [ cadena ] || pdf: { url: [ cadena ] }
  * suplente [ cadena ]
  * elección [mayoría relativa, primera minoría, representación proporcional] [ numerico ]
  * curul [ numerico ]
  * cabecera [ cadena ]
  * teléfonos [ cadena ]
  * links (redes sociales, páginas) [ cadena ]

# Legislaturas
` Has many ` **[Diputados](#Actor)**
` Has many ` **[Iniciativas](#Iniciativas)**
  * nombre
  * no_de_legislatura [ cadena ]
  * mo_en_romano [ cadena ]

# Periodos
` Belongs to ` **[Legislatura](#Legislaturas)**
  * Legislatura [ cadena ]
  * Legislatura Id [ numerico ]
  * Actual [ boolean ]

# Periodos
` Belongs to ` **[Legislatura](#Legislaturas)**
 * Legislatura [ numerico ]
 * Legislatura Id [ numerico ]
 * Actual [ boolean ]

# Partidos
` Has many ` **[Diputados](#Actor)**
` Belongs to ` **[Legislatura](#Legislaturas)**
` Has and Belongs to ` **[Iniciativas](#Iniciativa)**
 * nombre [ cadena ]
 * logo [ cadena ] || pdf: { url: [ cadena ] }
 * estatus [ boolean ]
 * url_web [ cadena ]
 * orden [ numerico ]
 * estatus [ numerico ]

# Asistencias
` Has and belongs to many ` **[Diputados](#Actor)**
` Has and belongs to many ` **[Asistencias Diputados](#Asistencias-diputados)**
` Belongs to ` **[Comision](#Comisiones)**
` Belongs to ` **[Legislatura](#Legislaturas)**
  * fecha [ datetime ]
  * comision [ numerico ]
  * legislatura [ numerico ]
  * periodo [ cadena ]

# Asistencias-diputados
` Belongs to ` **[Diputado](#Actor)**
` Belongs to ` **[Asistencia](#Asistencias)**
  * diputado_id [ numerico ]
  * asistencia_id [ numerico ]
  * tipo_de_asistencia [ numerico ]

# Dictamenes
` Has many ` **[Iniciativas](#Iniciativas)**
` Has many ` **[Votaciones](#Votaciones)**
` Belongs to ` **[Legislatura](#Legislaturas)**
  * titulo [ cadena ]
  * fecha_de_presentacion [ datetime ]
  * archivo [ cadena ] || pdf: { url: [ cadena ] }
  * numero_de_publicacion (Periodico oficial) [ cadena ]

# Revision:
  * creada (fecha)
  * aceptado (sí/no)
  * diff (hash)

# Puesto:
  * nombre (del puesto)
  * comisión (a la que pertenece)

# Link:
  * servicio (qué red social es)
  * url
  * actor (a la que pertenece)

# Inasistencia: (Revisar)
  * actor (a la que pertenece)
  * total
  * sesiones
  * periodos (hash)

# Votaciones:
` Belongs to ` **[Diputado](#Actor)**
` Belongs to ` **[Dictamen](#Dictamenes)**
  * actor (a la que pertenece)
  * total
  * a favor
  * en contra
  * abstención
  * ausente
  * periodos (hash)

# Comisiones:
` Has many ` **[Diputados](#Actor)**
` Has many ` **[Asistencias](#Asistencias)**
  * cámara
  * nombre
  * oficina
  * link
  * entidad (para cámaras locales)
  * teléfonos
  * integrates (actores que pertenecen)
    * cuáles son de presidencia
    * cuáles son de secretaría
    * cuáles son sólo integrantes

# Distrito:
  * tipo
  * entidad
  * secciones

# Sección:
  * entidad
  * municipio
  * (id) marco geográfico nacional
  * sección
  * tipo
  * coordenadas


# Teléfono:
  * número
  * extensión


# Cabilderos:
  * rfc [ cadena ]
  * razon_social [ cadena ]
  * domicilio [ cadena ]
  * telefono [ cadena ]
  * correo_electronico [ cadena ]
  * personas_autorizadas (tratar como array)
  * estatus_cabildero [ boolean ]
  * anexo_buno (tratar como text)
  * anexo_bdos (tratar como text)
  * numero_acreditacion [ cadena ]
  * persona_fisica [ cadena ]
  * numero_cabildero [ numerico ]
  * fecha_acreditacion [ datetime ]
  * organos_gobierno_comisiones
  * diputadas_diputados
  * diputados (arreglo con los datos de los diputados correspondientes)
  * comisiones
  * nombre
  * colonia

# Decretos
 ` Belongs to` **[Dictamen](#Dictamenes)**
 ` Belongs to` **[Iniciativa](#Iniciativas)**
 ` Belongs to` **[Legislatura](#Legislaturas)**
 ` Has many` **[Archivos](#Archivos)**
   * titulo [ cadena ]
   * archivo [ cadena ]
   * archivo_de_publicacion [ cadena ] || pdf: { url: [ cadena ] }
   * descripcion [ texto ]
   * fecha_publicacion [ datetime ]
   * no_publicacion [ cadena ] || pdf: { url: [ cadena ] }

# Detalle-orden
 ` Belongs to` **[Orden](#Ordenes)**
 ` Belongs to` **[Iniciativa](#Iniciativas)**
   * archivo
   * descripcion
   * numero_romano
   * colocacion(orden)

# Ordenes
  ### Ordenes del día
` Belongs to` **[Comision](#Comisiones)**
` Belongs to` **[Legislatura](#Legislaturas)**
  * fecha
  * ejercicio
  * archivo_pdf
  * tipo_de_orden (reunion, sesión solemne, diputación permanente, junta preparatoria, sesión extraordinaria)

# Listado de todas la Iniciativas:
  * id
  * fecha
  * descripcion
  * fondo
  * subfondo
  * seccion
  * clave
  * lugar
  * fecha_radicacion
  * iniciante
  * tipo_documento
  * asunto
  * comisiones
      * comision
          * nombre
# Ley:
` Belongs to` **[Legislatura](#Legislaturas)**
  * id [ numerico ]
  * categoria_id [ numerico ]
  * created_at [ datetime ]
  * updated_at [ datetime ]
  * titulo [ cadena ]
  * descripcion [ cadena ]
  * tipo [ numerico ]
  * variable_id [ numerico ]
  * epub_url [ cadena ] || epub: { url: [ cadena ] }
  * word_url [ cadena ] || alt: word: { url: [ cadena ] }
  * pdf_url [ cadena ] || pdf: { url: [ cadena ] }
  * publicacion_url [ cadena ]  || publicacion: { url: [ cadena ] }
  * publicacion_info [ cadena ]  
  * orden [ numerico ]

# Código

  * id [ numerico ]
  * titulo [ cadena ]
  * descripcion [ cadena ]
  * pdf_url [ cadena ] || pdf: { url: [ cadena ] }
  * word_url [ cadena ] || word: { url: [ cadena ] }
  * publicacion_url [ cadena ] || publicacion: { url: [ cadena ] }
  * publicacion_info [ cadena ]
