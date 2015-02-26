# -*- coding: utf-8 -*-

from software_livre import SoftwareLivre
from pymongo import MongoClient


#saia_de_casa = EventoHandler('https://saiadecasa.github.io/')

#print saia_de_casa.get_eventos()

software_livre = SoftwareLivre('http://softwarelivre.org/portal/eventos', ('nome', 'data', 'site', 'local'))

mongo_client = MongoClient()
mongo_db = mongo_client.test
mongo_eventos = mongo_db.eventos

def registra_eventos(eventos):
    for evento in eventos:
        if not mongo_eventos.find({'nome': evento['nome']}).count():
            mongo_eventos.insert(evento)

registra_eventos(software_livre.get_eventos())

for e in mongo_eventos.find():
    print e
