# ciclo_formativo/models/ciclo_formativo.py

from odoo import models, fields, api

class CicloFormativo(models.Model):
    _name = 'ciclo_formativo.ciclo_formativo'
    _description = 'Ciclos formativos'

    name = fields.Char(string="Nombre del ciclo", required=True)
    description= fields.Text(string="Descripción")
