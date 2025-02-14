# ciclo_formativo/models/modulo.py

from odoo import models, fields, api

class Modulo(models.Model):
    _name='ciclo_formativo.modulo'
    _description = 'Modulos del ciclo formativo'

    name = fields.Char(string = 'Nombre módulo', required=True)
    id_ciclo = fields.Many2one('ciclo_formativo.ciclo_formativo', string='Ciclo formativo', required=True)
    id_profesor = fields.Many2one('ciclo_formativo.profesor', string='Profesor', unique=True)
    id_alumno = fields.Many2many('ciclo_formativo.alumno', string='Alumnos matriculados')

