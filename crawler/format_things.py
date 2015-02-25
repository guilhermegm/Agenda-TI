# -*- coding: utf-8 -*-

import re, locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, "pt_BR")

class FormatThings():
    meses_pt_br = dict([(datetime.strptime(str(i), '%m').strftime('%B').lower(), i) for i in range(1,13)] + [(datetime.strptime(str(i), '%m').strftime('%b').lower(), i) for i in range(1,13)])

    def get_month(self, month):
        if month.isnumeric():
            return int(month)
        else:
            return self.meses_pt_br[month.strip().lower()]

    def parse_data_pattern(self, data, pattern):
        data_pattern = re.findall(pattern, data, re.DOTALL | re.IGNORECASE)
        return data_pattern[0] if data_pattern else None

    def format_nome(self, nome):
        return nome.strip().title()

    def format_data(self, data):
        data_formatted = None
        data_patterns = (
            { 'pattern': '(\d+) e \d+ de (\w+?) de (\d+)', 'data_parts': {'day': 0, 'month': 1, 'year': 2} },
            { 'pattern': '(\d+) de (\w+?) de (\d+)', 'data_parts': {'day': 0, 'month': 1, 'year': 2} },
            { 'pattern': '(\d+) a (\d+) de (\w+)', 'data_parts': {'day': 0, 'month': 2} },
            { 'pattern': '(\d+) de (\w+)', 'data_parts': {'day': 0, 'month': 1} },
        )

        for data_pattern in data_patterns:
            data_parsed = self.parse_data_pattern(data, data_pattern['pattern'])

            if data_parsed:
                day = int(data_parsed[ data_pattern['data_parts']['day'] ])
                month = self.get_month(data_parsed[ data_pattern['data_parts']['month'] ])
                year = int(data_parsed[ data_pattern['data_parts']['year'] ]) if 'year' in data_pattern['data_parts'] else datetime.now().year
                datetime_params = {'day': day, 'month': month, 'year': year}

                data_formatted = datetime(**datetime_params)
                break

        return data_formatted

    def format_local(self, local):
        return local.strip().title()

    def format_endereco(self, endereco):
        return endereco.strip().title()

    def format_site(self, site):
        return site.strip().lower()