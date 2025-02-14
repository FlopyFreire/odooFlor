# ciclo_formativo/models/alumno.py

from odoo import models, fields

class Alumnos(models.Model):
    _name = 'ciclo_formativo.alumno'
    _description = 'Alumnos matriculados'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    matricula = fields.Char(string='Matrícula', required=True)
    id_modulo = fields.Many2many('ciclo_formativo.modulo', string='Módulos matriculados', required=True)
    

