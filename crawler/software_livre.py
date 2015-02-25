# -*- coding: utf-8 -*-

import re
from evento_handler import EventoHandler

class SoftwareLivre(EventoHandler):

    def get_painel_eventos(self, page_content):
        painel = re.findall("class=\"article-body(.*?)<!-- end class=\"article", page_content, re.DOTALL | re.IGNORECASE)
        return painel[0] if painel else ''

    def get_eventos_box(self, painel_eventos):
        eventos_box = re.findall("(<p>.*?</p>)", painel_eventos, re.DOTALL | re.IGNORECASE)
        return eventos_box

    def get_evento_box_nome(self, evento_box):
        nome = re.findall("<strong>([\w\d].+?)</strong><br />", evento_box, re.DOTALL | re.IGNORECASE)
        return nome[0] if nome else ""

    def get_evento_box_data(self, evento_box):
        data = re.findall(">(\d+ .+?\d\d\d\d)<", evento_box, re.DOTALL | re.IGNORECASE)
        return data[0] if data else ""

    def get_evento_box_local(self, evento_box):
        local = re.findall("<br />(\w.+?)<br />", evento_box, re.DOTALL | re.IGNORECASE)
        return local[0] if local else ""

    def get_evento_box_endereco(self, evento_box):
        return ""

    def get_evento_box_site(self, evento_box):
        site = re.findall(u"href=\"(.+?)\"", evento_box, re.DOTALL | re.IGNORECASE)
        return site[0] if site else ""