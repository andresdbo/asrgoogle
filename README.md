# asrgoogle
Script transcripción ASR de google colad plataforma
ASR Google cloud plataform - BETA

Pasos a seguir para habilitar el uso del la APIs Services, en este caso utilizamos Speech API.

•	Dar de alta una cuenta en Google cloud plataform
•	En APIs Services habilitar Speech services
•	Crear claves en credenciales, pueden ser de dos tipo, claves de APIs o claves de cuentas de servicio (ej tipo JSON) 
•	Crear la variable de sistema GOOGLE_APPLICATION_CREDENTIALS, ej.: export GOOGLE_APPLICATION_CREDENTIALS=file.json
•	Para la transcripción de audios menores a 60s se puede leer directamente desde disco, para audios mayores a 60s es necesario leer desde google Storage.

El script asrgoogle_sync_async.py recibe como parámetro la ubicación del audio en google storage de tipo gs o la ruta en disco.

Ej.:
Google storage:
python asrgoogle_sync_async.py gs://file.wav
Disco:
python asrgoogle_sync_async.py /file.wav
