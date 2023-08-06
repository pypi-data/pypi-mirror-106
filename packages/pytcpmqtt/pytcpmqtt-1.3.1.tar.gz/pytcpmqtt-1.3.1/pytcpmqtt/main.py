import socket
import threading
import sys
import time
import json
import getpass
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import ssl
import base64
import random, string
import math
import datetime
from queue import Queue # queue pour partager les données entre 2 thread

class Socket_Thread (threading.Thread):
    def __init__(self, host, port, Queue):      # arguments du de la classe
        threading.Thread.__init__(self)  # ne pas oublier cette ligne
        # (appel au constructeur de la classe mère)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.sock.settimeout(10.0)# nécessaire pour relancer la connexion si pas de reception après 10.00 secondes
        self.connected = False
        self.queue = Queue

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(10.0)# nécessaire pour relancer la connexion
            self.sock.connect((self.host, self.port))
            mess = "{\"connexion\":\"0K\"}\n" # n'importe quel message pour initier la connexion au serveur TCP
            self.sock.sendall(str.encode(mess))# pour initialiser la connexion
            print("connexion effectuée sur le serveur : "+self.host)
            self.connected = True
            #print(str(self.data.decode("utf-8")))
            with self.queue.mutex:# vide le contenu de la queue en préservant le Thread (MUtual EXclusion) 
                self.queue.queue.clear()
        except:
            print("Pas de connexion avec le serveur TCP ... tentative de reconnexion ... ")
            #input("Press enter to quit")
            self.connected = False
            time.sleep(2)
            #sys.exit(0)
    
    def run(self):
        while not self.connected:
            self.connect()
            time.sleep(2)
        i = 0 # pour tester la fermeture de la connexion
        while True:
            if (self.connected):
                try:
                    data = self.sock.recv(1024)
                    #print("data : {0}".format(data))
                    dataStr = str(data.decode("utf-8").strip('\r\n'))
                    if dataStr != "":
                        i = 0
                        #print(str(data.decode("utf-8").strip('\r\n')))
                        self.queue.put(dataStr) # sauvegarde des données dans un queue partagée entre 2 thread
                        #print("queue non vide")
                    else :
                        i+=1
                        #print("i : {0}".format(i))
                    if (i> 20):# si > 20 on a perdu la connexion a été fermée, on se reconnecte....
                        self.connected = False
                    #self.queue.put(dataStr)
                    #print("ok")
                except socket.timeout:
                    self.connected = False
                    print( "connexion perdue .... essai de reconnexion " )
                    self.connect()
                    #time.sleep(5)
            else :
                #print("La connexion avec le serveur TCP est perdue....")
                #print(" ... essai de reconnexion ...")
                self.connect()
                time.sleep(2)
                
                    # while not self.connected:  
                        # # attempt to reconnect, otherwise sleep for 2 seconds  
                        # try:
                            # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            # self.sock.settimeout(10.0)#ne pas oublier !!!
                            # self.sock.connect((self.host,self.port))  
                            # self.sock.sendall(str.encode(mess))# pour initialiser la connexion
                            # #self.queue = Queue
                            # print("connexion initialisée !!")
                            # #data = self.sock.recv(1024)
                            # self.connected = True
                            # #print( "re-connection successful" )  
                        # except socket.error:
                            # print("erreur de connexion !!")
                            # print("... reconnexion....")
                            # self.connected = False;
                            # time.sleep(2)
                            #except :
                            #    print("erreur 3")
                #except :
                #    print("erreur 2")

# Opening JSON file 
try:
    file = open('tcp_mqtt_data.json',"r") 
except OSError:
    print('Le fichier de configuration \'tcp_mqtt_data.json\' n\'est pas présent dans votre répertoire !')
    exit()

# returns JSON object as a dictionary 
jsonconf = json.load(file) 

host = jsonconf["tcp_host"]
port = jsonconf["tcp_port"] 
urlMqtt = jsonconf["broker_url"]  # url mqtt
portMqtt = jsonconf["broker_port"]   # port mqtt

salle = jsonconf["salle"]
KEY = jsonconf["KEY"]
broker_protocol = jsonconf["broker_protocol_mqtt_mqtts_ws_wss"]

# vérification du champ date
valeurDate = False # par defaut vapeur False
champ_date =  "date_heure" in jsonconf # si True la clé existe
if (champ_date):
    valeurDate = jsonconf["date_heure"]
    #valeurDate = bool(str_valeurDate == 'true')
    if (valeurDate):
        print("\"date_heure\": true  -> ajout de la date et l'heure dans le json.")
    #else :
        #print("sans date ")

#transport='websockets'    transport="tcp" pour ssl)
if (broker_protocol == "wss"):
    protocol = "websockets"
else :
    protocol = "tcp"

IdUser = True;# identification par login et mot de passe vrai par defaut
TLSV = True # TLS vrai par défaut

Username = input('Entrez votre identifiant MQTT : ') 
pwd = getpass.getpass('Entrez votre mot de passe MQTT :')

auth = {
    'username':Username,
    'password':pwd
}

# fonction qui retourne une chaine aléatoire
def randomword(length):
    lettresEtChiffres = string.ascii_letters + string.digits
    chaineAleatoire = ''.join((random.choice(lettresEtChiffres) for i in range(length)))
    return chaineAleatoire

tls = {
  #'ca_certs':"",
  'tls_version':ssl.PROTOCOL_TLSv1_2
}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  #print("Connected with result code "+str(rc))
  if (rc ==0):
      client.connected_flag=True #set flag
      print("connexion MQTT effectuée sur : "+urlMqtt +" port : "+str(portMqtt)+"\n")
      client.subscribe(salle+"/"+KEY+"/in")
  else :
      print("Problème de connexion, code : "+str(rc))
      client.connected_flag=False #set flag
      print("Programme terminé ! (tapez Ctrl-break ou Ctrl-C pour quitter")
      quit()
      #exit()
      #raise SystemExit
  #print("flags "+str(flags))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data = str(msg.payload.decode("utf-8"))
    print("réception : "+salle+"/"+KEY+"/in "+data)
    # envoi d'un message vers le serveur    
    mess = data+"\n"
    m.sock.sendall(str.encode(mess)) # réception des données de mqtt et envoi vers le serveur TCP 
    #print(data.encode())
    #"{\"led1\":255}\n"

# mqtt connexion
client = mqtt.Client(
  client_id= randomword(8),
  clean_session=True,
  protocol=mqtt.MQTTv311,
  transport=protocol)    # transport="tcp" pour ssl et "websockets" pour wss)
client.connected_flag=False
if IdUser:
    client.username_pw_set(username=auth["username"],password=auth["password"])
if TLSV:
    client.tls_set(tls_version=tls["tls_version"])
    #print("connexion TLSV")
    
client.on_connect = on_connect
client.on_message = on_message
client.reconnect_delay_set(min_delay=3, max_delay=120) # reconnection après 3 s puis si échec après 6 s jusqu'à 120 s
client.connect(urlMqtt, portMqtt, 60)

def envoiVersMqtt(in_q):
    while True:
        try:
            data = in_q.get() 
            # Process the datdata
            # python object to be appended
            if (valeurDate):
                datenow = datetime.datetime.now()
                date_time = datenow.strftime("%Y-%m-%d %H:%M:%S")
                jsondate = {"date":date_time}
                datajson = json.loads(data)
                # appending the data
                datajson.update(jsondate)
                data = json.dumps(datajson)  # takes Python Object as the parameter. It returns the JSON string. 
                
            if (client.connected_flag):
                print("envoi : "+salle+"/"+KEY+"/out/ "+data)
                client.publish(salle+"/"+KEY+"/out/",payload=data,qos=0)# envoi des données vers MQTT
        except: 
            print('problème d\'envoi vers mqtt !!!')
            #break

# Initializing a queue
q = Queue(maxsize = 10)# taille maximale de la queue FIFO 
#q = Queue()

#Création du thread de connexion au serveur TCP
m = Socket_Thread(host,port,q)        # crée le thread avec la queue de données
m.start()    
time.sleep(2)

# envoi d'un message 
#mess = "{\"led1\":255}\n"
#m.sock.sendall(str.encode(mess))

# création du thread pour envoyer les données vers MQTT
t = threading.Thread(target=envoiVersMqtt,args =(q, ))
t.start()

client.loop_forever()
print("FIN")