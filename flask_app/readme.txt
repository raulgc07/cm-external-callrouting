Para poner en funcionamiento la aplicción seguir los siguientes pasos:
1.- General imagenes y contenedores.
    Vamos a generar todo de golpe usando docker compose. Para ello ejecutar el siguiente comando
        docker compose up -d
    Esto deber de generar tres imagenes:
        - app-flask-external-router_cm   
        - nginx-for-flask                
        - mysql_for_flask_router_cm
    y tres contenedores que además arrancarará:
        - base_datos_mysql
        - app_nginx
        - app-flask


3.- Verificar funcionamiento
    3.-1 Verficar que se han generado los contenedores y que están ejecutandose, para ello ejecutar
        docker ps 
    
    3.2.- Desde un navegador acceder a la siguiente url:
            http://ip-maquina:8080/callmanager

          En el navegador debería responder method not allowed
    
        3.2.1.- Se podría probar con postman enviando una peticón post y en el body lapetición xacml de la api curri, y entonces veriamos la respuesta enviadda por la aplicación en postman
                si se deniega o permite la llamada

    3.-3.- Probarlo configurado el external call control profile y asinarlo al translation pattern

            
4.- Se han creado distintas url's para el funcionamiento de la aplicación:

    http://ip-maquina:8080/callmanager  --> Recibirá las peticions desde el callnaner y la aplicación responderá si se debe permitir o denegar la llamada.
    http://ip-maquina:8080/add          --> Añadir un teléfono a la lista negra para que se le deniege la llamada
    http://ip-maquina:8080/del          --> Eliminar un teléfono de la lista negra
    http://ip-maquina:8080/display      --> Ver los teléfonos que hay en la lista negra.

5.- Posibles mejoras
    Crear un fichero la url index y ensta que se sirva una pagina index conteniendo enlaces a las urls de add, del y display


6. Notas:

    -Los ficheros Dockerfile son llamados desde el docker-compose.yml para generar las imagenes y los contenedores.
    -El fichero nginx-for-app-flask/project.conf contiene la configuración del servidor nginx, que en este caso se le dice que escuhe por el puerto 80 y se le indica las
     url's de las cuales tiene que hacer proxy al servidor da aplicaicones gunicorn que a la vez lo reenvia a flask. Este fichero desde el Dockerfile se copia a 
     /etc/nginx/conf.d
    -El fichero initdb.sql Contiene la información para cuando se crea el contenedor que inicialize la base de datos creando la tabla telefonos, para ello este fichero en el Dockerfile-mysql se
     copia a /docker-entrypoint-initdb.d/initdb.sql , ya que todo lo que haya en esa ubicación se ejecuta cuando se crea el contenedor pudiendo asi inicializar una base de datos.
