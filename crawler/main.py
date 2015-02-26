# -*- coding: utf-8 -*-

import re
from software_livre import SoftwareLivre
from pymongo import MongoClient


def main():

    def registra_eventos(eventos):
        for evento in eventos:
            if not mongo_eventos.find({'nome': re.compile(evento['nome'], re.IGNORECASE)}).count():
                print mongo_eventos.insert(evento)

    saia_de_casa = EventoHandler('https://saiadecasa.github.io/')
    software_livre = SoftwareLivre('http://softwarelivre.org/portal/eventos', ('nome', 'data', 'site', 'local'))

    mongo_client = MongoClient()
    mongo_db = mongo_client.test
    mongo_eventos = mongo_db.eventos

    registra_eventos(software_livre.get_eventos())
    registra_eventos(saia_de_casa.get_eventos())

if __name__ == "__main__":
    main()