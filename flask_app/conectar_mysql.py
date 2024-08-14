import mysql.connector
#from mysql.connector import *
from mysql.connector import errorcode



def conectar_bd ():
    try:
        #conexion = mysql.connector.connect(user='root', password='password', host='nombre o ip base datos')
        conexion = mysql.connector.connect(user='root', password='password', host='base_datos_mysql', database='lista_negra')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print ("error de ultimo esfuerzo")
            print(err)
    else:
        print ("conectado a la base de datos")
        return (conexion)
        

def crear_bd (cursor):
    print ("creando base de datos")
    cursor.execute("create database lista_negra")
    print ("saliendo de crear base de datos")

def crear_tabla (cursor):
    print ("creando tabla")
    cursor.execute("CREATE TABLE telefonos (id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,nombre varchar(60),telefono varchar(20))")
    print ("saliendo de crear tabla")

def buscar_elemento (telefono):
    conexion = conectar_bd()
    mycursor = conexion.cursor()
    sql_statement = "select * from telefonos where telefono='"+telefono+"'"
    print ("La cadena SQL es: ", sql_statement)
    mycursor.execute(sql_statement)
    elementos= mycursor.fetchone()
    if elementos != None:
        print (elementos[2])
        mycursor.close()
        conexion.close()    
        return True 
    else:
        print ("Numero no esta en la base de datos") 
        mycursor.close()
        conexion.close()
        return False
              



def insertar_elemento(nombre, telefono):
    print (nombre)
    print (telefono)
    conexion=conectar_bd()
    mycursor = conexion.cursor()
    sql_statement= ("insert into telefonos (nombre, telefono) values (%s, %s)" )
    dato_telefono = (nombre , telefono)
    print ("La sentencia sql es: ", sql_statement)
    try:
        mycursor.execute(sql_statement, dato_telefono)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DUP_ENTRY:
            print ("registro duplicado")
            return False
    else:      
        print ("registro añadido" ,nombre, telefono)
        conexion.commit()
        mycursor.close()
        conexion.close()
        return True

def eliminar_elemento(telefono):
    print ("telefono")
    if buscar_elemento(telefono):

        conexion=conectar_bd()
        mycursor = conexion.cursor()
        sql_statement= ("delete from telefonos where telefono='"+telefono+"'")
        try:
            mycursor.execute(sql_statement)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print ("error")
                return False
        else:      
            print ("registro eliminado" , telefono)
            conexion.commit()
            mycursor.close()
            conexion.close()
            return True
    else:
        return False    

def mostrar():
    conexion=conectar_bd()
    mycursor = conexion.cursor()
    sql_statement= ("select * from telefonos")
    try:
        mycursor.execute(sql_statement)
    except mysql.connector.Error as err:
        #if err.errno == errorcode.ER_DUP_ENTRY:
        print ("error")
        return False
    else:      
        print ("mostrando datos")
        elementos= mycursor.fetchall()
        mycursor.close()
        conexion.close()
        return elementos

    


            

if __name__ == "__main__":

    conectar_bd()
  

