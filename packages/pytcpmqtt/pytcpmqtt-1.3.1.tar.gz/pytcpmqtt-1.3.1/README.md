#pytcpmqtt

Permet la connexion d'un microprocesseur fonctionnant en serveur TCP sur un réseau local vers un serveur MQTT.

Un fichier json de configuration "tcp_mqtt_data.json" doit être présent dans le répertoire :

Contenu du fichier "tcp_mqtt_data.json" :

{<br />
  "tcp_host":"192.168.1.26",<br />
  "tcp_port":92,<br />
  "broker_url":"url_de_votre_broker_mqtt",<br />
  "broker_protocol_mqtt_mqtts_ws_wss":"tcp",<br />
  "broker_port":8443,<br />
  "date_heure":true,<br />
  "salle":"maSalle",<br />
  "KEY":"bureau/lumiere1"<br />
}<br />

-----------

Le topic de réception sera : salle/KEY/out

Le topic d'envoi sera : salle/KEY/in

Si date_heure" : true alors ajoute de la date et l'heure dans le json , si non mettre à : false 

Les protocoles possibles sont "wss" websockets sécurisés avec login et mot de passe ( pas de certificat)
ou "tcp" pour ssl avec login et mot de passe ( pas de certificat client) 

Lancement du programme :

	py -m pytcpmqtt.main 
	(ou sur raspberry python3 -m pytcpmqtt.main)



