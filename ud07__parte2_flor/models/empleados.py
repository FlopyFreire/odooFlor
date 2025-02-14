# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Empleado(models.Model):
    _name = 'empresa.empleado'
    _description = 'Empleado'
    _rec_name = 'complete_name' # Usar el nombre completo como identificador

    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    dni = fields.Char(string="DNI", required=True)
    telefono = fields.Char(string="Teléfono", required=True)
    tiene_licencia_moto = fields.Boolean(string="Licencia de Moto")
    tiene_licencia_furgoneta = fields.Boolean(string="Licencia de Furgoneta")
    foto = fields.Binary(string="Foto")

    complete_name = fields.Char(string="Nombre Completo", compute="_compute_complete_name", store=True)

    def _compute_complete_name(self):
        for record in self:
            record.complete_name = f"{record.nombre} {record.apellido}".strip()

    repartos_ids = fields.One2many('empresa.reparto', 'empleado_id', string="Repartos")
