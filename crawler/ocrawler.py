# -*- coding: utf-8 -*-

import requests

class CrawlerHandler():

    base_url = ''
    request_page = None

    def __init__(self, base_url):
        self.base_url = base_url

    def get_request_page(self):
        self.request_page = requests.get(self.base_url)

    def get_page_content(self):
        if not self.request_page:
            self.get_request_page()
        return self.request_page.text