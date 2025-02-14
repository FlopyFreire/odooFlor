# biblio_comics/models/socios.py
from odoo import models, fields

class BiblioComicsSocios(models.Model):
    _name = 'biblio_comics.socios'
    _description = 'Biblio Comics Socios'

    name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    identifier = fields.Char(string='Identifier', required=True)
