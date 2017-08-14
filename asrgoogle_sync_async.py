#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Andrés de Barros - adebaros@expand.com.uy
Script para ejecutar transcripicones ASR utilizando los servicios de Speech Google cloud plataform
'''
import argparse
import base64
import json
import requests
import time
from pprint import pprint

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials
import ivr
import os
os.system("export GOOGLE_APPLICATION_CREDENTIALS=file.json")
key = ""
asterisk = ivr.IVR(debuglevel=4)

DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')

def get_speech_service():
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    return discovery.build(
        'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)

def transcribe_gcs(gs):
    service = get_speech_service()
    service_request = service.speech().asyncrecognize(
        body={
            'config': {
                'encoding': 'LINEAR16',
                'sampleRate': 8000,
                'languageCode': 'es-UY',
            },
            'audio': {
                "uri":gs
                }
            })
    response = service_request.execute()
    data = json.dumps(response)
    json_input = data
    try:
        decoded = json.loads(json_input)
        texto_reconocido = decoded['name']
    except (ValueError, KeyError, TypeError):
        print('Exception occoured: %s' % (e))
    url = "https://speech.googleapis.com/v1beta1/operations/" + str(texto_reconocido) + "?key=" + key
    content_response = requests.get(url)
    content_json = content_response.json() 
    data1 = json.dumps(content_json)
    decoded = json.loads(data1)
    inicio = 0
    while inicio == 0:
        try:
      	    decoded['done']
            inicio = 1
	    range = len(decoded['response']['results'])
	    for alternatives in xrange(range):
	     	print alternatives
	        speech = decoded['response']['results'][alternatives]['alternatives'][0]
	        print speech['transcript']
        except: 
	    content_response = requests.get(url)
            content_json = content_response.json()
            data1 = json.dumps(content_json)
            decoded = json.loads(data1)
            print ("Procesando speech id async: " + decoded['name'])
            time.sleep(5)

def transcribe_file(speech_file):
    with open(speech_file, 'rb') as speech:
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                'encoding': 'LINEAR16',
                'sampleRate': 8000, 
                'languageCode': 'es-UY',
            },
            'audio': {
		 'content': speech_content
                }
            })
    response = service_request.execute()
    data = json.dumps(response)
    json_input = data
    try:
        decoded = json.loads(json_input)
        texto_reconocido = decoded['results'][0]['alternatives'][0]['transcript']
    except (ValueError, KeyError, TypeError):
        print('Exception occoured: %s' % (e))
    return texto_reconocido

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path', help='Debe indicar un archivo de audio en disco o un audio con patg GCS')
    args = parser.parse_args()
    if args.path.startswith('gs://'):
        transcribe_gcs(args.path)
    else:
        print transcribe_file(args.path)
