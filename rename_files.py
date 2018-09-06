# -*- coding: cp1252 -*-
import os
def rename_files():
    #(1) get file names from folder

    #caracter r no inicio do caminho indica que nomes serao vistos como strings
    file_list = os.listdir(r"C:\Curso Python\mesage")
    #print (file_list)
    saved_path = os.getcwd()
    #get diretorio de trabalho atual ou corrente
    #desta forma, vemos qual é o diretorio atual em tempo de execução

    os.chdir(r"C:\Curso Python\mesage")
    #aqui modificamos o diretorio atual para alterar os nomes dos arquivos
    
    
    #(2) for each file, rename file name
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"1234567890"))
        
        
    os.chdir(saved_path)



rename_files()
    
