# ciclo_formativo/models/profesor.py

from odoo import models, fields

class Profesor(models.Model):
    _name='ciclo_formativo.profesor'
    _description='Profesores que imparten módulos'

    name = fields.Char (string='Nombre', required=True)
    last_name = fields.Char (string='Apellidos', required=True)
    id_modulo = fields.Many2one('ciclo_formativo.modulo', string='Módulo que imparte', required=True, unique=True)
