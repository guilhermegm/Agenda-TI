
# -*- coding: utf-8 -*-

import re
from ocrawler import CrawlerHandler
from format_things import FormatThings

class EventoHandler(CrawlerHandler, FormatThings):
    evento_required_fields = ('nome', 'data', 'endereco', 'local')

    def __init__(self, base_url, evento_required_fields=None):
        self.base_url = base_url

        if evento_required_fields:
            self.evento_required_fields = evento_required_fields

    def get_painel_eventos(self, page_content):
        painel = re.findall("<section id='main_content'>(.*?)</section>", page_content, re.DOTALL | re.IGNORECASE)
        return painel[0] if painel else ''

    def get_eventos_box(self, painel_eventos):
        eventos_box = re.findall("(<h4>.*?</ul>)", painel_eventos, re.DOTALL | re.IGNORECASE)
        return eventos_box

    def evento_to_json(self, nome, data, local, endereco, site):
        return {'nome': nome, 'data': data, 'local': local, 'endereco': endereco, 'site': site}

    def get_evento_box_nome(self, evento_box):
        nome = re.findall("<h4>(.*?)</h4>", evento_box, re.DOTALL | re.IGNORECASE)
        return nome[0] if nome else ""

    def get_evento_box_data(self, evento_box):
        data = re.findall("Data:</b>(.*?)<", evento_box, re.DOTALL | re.IGNORECASE)
        return data[0] if data else ""

    def get_evento_box_local(self, evento_box):
        local = re.findall("Local:</b>(.*?)<", evento_box, re.DOTALL | re.IGNORECASE)
        return local[0] if local else ""

    def get_evento_box_endereco(self, evento_box):
        endereco = re.findall(u"Endereço:</b>(.*?)<", evento_box, re.DOTALL | re.IGNORECASE)
        return endereco[0] if endereco else ""

    def get_evento_box_site(self, evento_box):
        site = re.findall(u"Site:</b>(.*?)<", evento_box, re.DOTALL | re.IGNORECASE)
        return site[0] if site else ""

    def parse_eventos_box(self, eventos_box):
        eventos_box_parsed = []

        for evento_box in eventos_box:
            nome = self.get_evento_box_nome(evento_box)
            data = self.get_evento_box_data(evento_box)
            local = self.get_evento_box_local(evento_box)
            endereco = self.get_evento_box_endereco(evento_box)
            site = self.get_evento_box_site(evento_box)

            eventos_box_parsed.append( self.evento_to_json( nome, data, local, endereco, site ) )

        return eventos_box_parsed

    def format_eventos_box(self, eventos_box_parsed):
        for evento in eventos_box_parsed:
            evento['nome'] = self.format_nome( evento['nome'] )
            evento['data'] = self.format_data( evento['data'] )
            evento['local'] = self.format_local( evento['local'] )
            evento['endereco'] = self.format_endereco( evento['endereco'] )
            evento['site'] = self.format_site( evento['site'] )

    def is_evento_valid(self, evento):
        for field in self.evento_required_fields:
            if not (field in evento and evento[field]):
                return False
        return True

    def remove_invalid_eventos(self, eventos_box_formatted):
        i = 0
        while i < len(eventos_box_formatted):
            if self.is_evento_valid( eventos_box_formatted[i] ):
                i += 1
            else:
                eventos_box_formatted.pop(i)

    def parse_page_content(self):
        page_content = self.get_page_content()

        painel_eventos = self.get_painel_eventos(page_content)
        eventos_box = self.get_eventos_box(painel_eventos)
        eventos_box_parsed = self.parse_eventos_box(eventos_box)

        self.format_eventos_box(eventos_box_parsed)
        self.remove_invalid_eventos(eventos_box_parsed)

        return eventos_box_parsed

    def get_eventos(self):
        return self.parse_page_content()