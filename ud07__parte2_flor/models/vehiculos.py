# -*- coding: utf-8 -*-
from odoo import models, fields

class Vehiculo(models.Model):
    _name = 'empresa.vehiculo'
    _description = 'Vehículo'
    _rec_name = 'matricula'  # Usar la matrícula como identificador

    tipo = fields.Selection([
        ('bicicleta', 'Bicicleta'),
        ('ciclomotor', 'Ciclomotor'),
        ('furgoneta', 'Furgoneta'),
    ], string="Tipo", required=True)
    matricula = fields.Char(string="Matrícula")
    descripcion = fields.Text(string="Descripción")
    foto = fields.Binary(string="Foto")
