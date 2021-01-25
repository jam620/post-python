#!/usr/local/bin/python3
# _*_ coding: utf8 _*_

import requests
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="Indica el archivo a subir")
parser = parser.parse_args()


def main():
    if parser.file:
        if path.exists(parser.file):
            archivo = open(parser.file, 'rb')
            headers = {'User-Agent': 'Firefox'}
            #Esto funciona pero como estoy cloudflare no permite la subida
            '''peticion = requests.post(url='https://seguridad.morenojose.com/demo2/upload.php',
                                     files={'fileToUpload': archivo}, headers=headers)'''
            '''peticion = requests.post(url='http://localhost:8888/python/upload.php',
                                     files={'fileToUpload': archivo}, headers=headers)'''
            peticion = requests.post(url='https://seguridad.morenojose.com/demo2/upload.php',
                                     files={'fileToUpload': archivo}, headers=headers)

            if parser.file in peticion.text:
                print(peticion.text)
                print("Archivo Subido con exito")
            else:
                print("Falló la subida del archivo")
        else:
            print("No existe el archivo")
    else:
        print("Necesito un archivo para subir")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")
