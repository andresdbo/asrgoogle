# Synopsis

La idea fue generar ejemplo en python para acceder a los servicios de Speech de Google, audios menores a 60 segundos y acceso asincrónico con audios mayores a 60 segundos, es un ejemplo experimental en face de testing.

# Instalación
## Requerimientos
$ pip install --upgrade gcloud

$ pip install --upgrade google-api-python-client

En la plataforma de google cloud, ir a proyectos y crear un nuevo proyecto, luego ir a credenciales y crear una credencial tipo key y otra tipo json.
En storage, crear un nuevo storage y subir un archivo de audio que sean mayores de 60s

# Ejemplos
### Ejecución de audio a texto de forma asincrónica con un audio mayor a 60s
`python asrgoogle_sync_async.py gs://storage-google-file.wav`
### Ejecución sincrónica con un audio en disco local
`python asrgoogle_sync_async.py gs://file.wav`

# Motivación
Poder conocer las nuevas tecnologías disponibles para la utilización de reconocimientos de voz.
