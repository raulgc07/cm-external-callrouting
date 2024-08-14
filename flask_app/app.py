# Aplicacion para callmanager external call control. Se usa librerias xml.sax para parse los datos xml


from flask import Flask, Response, request, render_template
from saxXacmlHandler import *
from conectar_mysql import *






# Definición de resuestas 

continueResponse = '<?xml encoding="UTF-8" version="1.0"?><Response><Result><Decision>Permit</Decision><Status></Status><Obligations><Obligation FulfillOn="Permit" ObligationId="urn:cisco:xacml:policy-attribute"><AttributeAssignment AttributeId="Policy:simplecontinue"><AttributeValue DataType="http://www.w3.org/2001/XMLSchema#string">&lt;cixml ver="1.0"&gt;&lt;continue&gt;&lt;/continue&gt; &lt;/cixml&gt;</AttributeValue></AttributeAssignment></Obligation></Obligations></Result></Response>'

# this is the same as the above response, yet the cixml is not encoded
continueResponseUnencodedCixml = '<?xml encoding="UTF-8" version="1.0"?><Response><Result><Decision>Permit</Decision><Status></Status><Obligations><Obligation FulfillOn="Permit" ObligationId="urn:cisco:xacml:policy-attribute"><AttributeAssignment AttributeId="Policy:simplecontinue"><AttributeValue DataType="http://www.w3.org/2001/XMLSchema#string"><cixml ver="1.0"><continue></continue></cixml></AttributeValue></AttributeAssignment></Obligation></Obligations></Result></Response>'

continueWithAnnouncementResponse = '<?xml encoding="UTF-8" version="1.0"?><Response><Result><Decision>Permit</Decision><Status></Status><Obligations><Obligation FulfillOn="Permit" ObligationId="urn:cisco:xacml:policy-attribute"><AttributeAssignment AttributeId="Policy:simplecontinue"><AttributeValue DataType="http://www.w3.org/2001/XMLSchema#string">&lt;cixml ver="1.0"&gt;&lt;continue&gt;&lt;greeting identification="custom_05011"/&gt;&lt;/continue&gt; &lt;/cixml&gt;</AttributeValue></AttributeAssignment></Obligation></Obligations></Result></Response>'

continueWithModifyIngEdResponse = '<?xml encoding="UTF-8" version="1.0"?><Response><Result><Decision>Permit</Decision><Status></Status><Obligations><Obligation FulfillOn="Permit" ObligationId="urn:cisco:xacml:policy-attribute"><AttributeAssignment AttributeId="Policy:simplecontinue"><AttributeValue DataType="http://www.w3.org/2001/XMLSchema#string">&lt;cixml ver="1.0"&gt;&lt;continue&gt;&lt;modify callingnumber="1000" callednumber="61002"/&gt;&lt;/continue&gt; &lt;/cixml&gt;</AttributeValue></AttributeAssignment></Obligation></Obligations></Result></Response>'

denyResponse = '<?xml encoding="UTF-8" version="1.0"?><Response><Result><Decision>Deny</Decision><Status></Status><Obligations><Obligation FulfillOn="Deny" ObligationId="urn:cisco:xacml:response-qualifier"><AttributeAssignment AttributeId="urn:cisco:xacml:is-resource"><AttributeValue DataType="http://www.w3.org/2001/XMLSchema#string">resource</AttributeValue></AttributeAssignment></Obligation></Obligations></Result></Response>'

divertResponse = '<?xml encoding="UTF-8" version="1.0"?> <Response><Result><Decision>Permit</Decision><Obligations><Obligation FulfillOn="Permit" ObligationId="continue.simple"><AttributeAssignment AttributeId="Policy:continue.simple"><AttributeValue DataType="http://www.w3.org/2001/XMLSchema#string">&lt;cixml ver="1.0"&gt;&lt;divert&gt;&lt;destination&gt;12378&lt;/destination&gt;&lt;/divert&gt;&lt;reason&gt;chaperone&lt;/reason&gt;&lt;/cixml&gt;</AttributeValue></AttributeAssignment></Obligation></Obligations></Result></Response>'

# this is the same as above, except that the cixml is not encoded
divertResponseUnencodedCixml = '<?xml encoding="UTF-8" version="1.0"?> <Response><Result><Decision>Permit</Decision><Obligations><Obligation FulfillOn="Permit" ObligationId="continue.simple"><AttributeAssignment AttributeId="Policy:continue.simple"><AttributeValue DataType="http://www.w3.org/2001/XMLSchema#string"><cixml ver="1.0"><divert><destination>12378</destination></divert><reason>chaperone</reason></cixml></AttributeValue></AttributeAssignment></Obligation></Obligations></Result></Response>'

notApplicableResponse = '<?xml encoding="UTF-8" version="1.0"?> <Response> <Result> <Decision>NotApplicable</Decision> <Status> <StatusCode Value="The PDP is not protecting the application requested for, please associate the application with the Entitlement Server in the PAP and retry"/> </Status> <Obligations> <Obligation ObligationId="PutInCache" FulfillOn="Deny"> <AttributeAssignment AttributeId="resource" DataType="http://www.w3.org/2001/XMLSchema#anyURI">CISCO:UC:VoiceOrVideoCall</AttributeAssignment> </Obligation>  </Obligations> </Result> </Response>'

indeterminateResponse = '<?xml encoding="UTF-8" version="1.0"?> :<Response><Result ResourceId=""><Decision>Indeterminate</Decision><Status><StatusCode Value="urn:cisco:xacml:status:missing-attribute"/><StatusMessage>Required subjectid,resourceid,actionid not present in the request</StatusMessage><StatusDetail>Request failed</StatusDetail></Status></Result></Response>'


def do_POST():
    # Metodo para cuando llegan peticiones POST, que serían las que manda el callmanager cuando manda un XACML call routing request. 
     
    """ parser = xml.sax.make_parser()
    handler = XacmlHandler()
    parser.setContentHandler(handler) """
    peticion=request.get_data()    # obtenemos los datos en bruto cuando llega la petición

    print ("peticion xml: ", peticion)
    handler2= XacmlHandler()       #Creamos el content handler
    xml.sax.parseString (peticion, handler2)  #creamos el parser (xmlreader) pero desde la propioa petición que viene del callmanager, y le pasamos el contenn handler para qeu maneje los eventos generados
    
    #parser.parse("sampleXacmlReq.xml")   esta linea sería si en vez de venir los datos xml en la petición html fuera en un fichero
    print (handler2.CallingNumber)
    
    if buscar_elemento(handler2.CallingNumber):
        resp=Response(denyResponse, 200, content_type= 'text/xml')    #Generamos unva variable tipo response con los datos que nos interesa. Las respuesta xml las tenemos definidas de antemano. en este caso es denegar
        return resp
        """
        if handler2.CallingNumber == elementos :    
        
            resp=Response(denyResponse, 200, content_type= 'text/xml')    #Generamos unva variable tipo response con los datos que nos interesa. Las respuesta xml las tenemos definidas de antemano. en este caso es denegar
            return resp
    
        else:      
            resp=Response(continueResponse, 200, content_type= 'text/xml')  #Generamos unva variable tipo response con los datos que nos interesa. Las respuesta xml las tenemos definidas de antemano. en este caso es continuar
            return resp
        """
    else:      
            resp=Response(continueResponse, 200, content_type= 'text/xml')  #Generamos unva variable tipo response con los datos que nos interesa. Las respuesta xml las tenemos definidas de antemano. en este caso es continuar
            return resp



app = Flask(__name__)


@app.route('/callmanager',methods = ['HEAD','POST'])
def callmanager():
    
    # peticion=request.get_data()  
    #encontrado=buscar_elemento("692808696")
    #if encontrado:
    #     print ("Hola funciona busar elemento")
    if request.method == 'HEAD':  #tratamos el method HEAD porque CURRI lo usa como keepalive y hay que responder con 200 OK
        return ('',200)
    
    elif request.method == 'POST': 
        resp=do_POST()
        return resp

@app.route('/add', methods = ['GET'])   
def add():
    return render_template("form_add.html", msg="Añadir teléfono")
    
@app.route('/insertar_telefono', methods = ['POST'])   
def insertar_telefono():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono= request.form['telefono']
        if insertar_elemento (nombre, telefono):
            return render_template("form_add.html", msg="¿Añadir otro teléfono?")  
        else:
            return (render_template("form_add.html", msg="El teléfono ya existe, intentenlo otra vez"))
    else:
        return ("Elemento no añadido", 200)
    

@app.route('/del', methods = ['GET'])   
def delete():
     return render_template("form_del.html", msg="Introduzca número de teléfono a eliminiar")

@app.route('/eliminar_telefono', methods = ['POST'])   
def eliminar_telefono():
    if request.method == 'POST':
        telefono= request.form['telefono']
        if eliminar_elemento (telefono):
            return (render_template("form_del.html", msg="¿Eliminar otro?"))
        else:
            return (render_template("form_del.html", msg="El teléfono no existe, intentalo otra vez"))
    else:
        return ("Elemento no eliminado", 200)
    
@app.route('/display', methods = ['GET'])   
def display():
    if request.method == 'GET':
        elementos=mostrar()   
        return render_template("tabla.html", datos=elementos)
    else:
        return ("Elemento no eliminado", 200)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
