# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'empresa.cliente'
    _description = 'Cliente'
    _rec_name = 'complete_name2'  # Usar el nombre completo como identificador

    dni = fields.Char(string="DNI", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    telefono = fields.Char(string="Teléfono", required=True)

    complete_name2 = fields.Char(
        string="Nombre Completo", compute="_compute_complete_name2", store=True
    )

    @api.depends('nombre', 'apellidos')  # Se recalcula si cambian estos campos
    def _compute_complete_name2(self):
        for record in self:
            record.complete_name2 = f"{record.nombre or ''} {record.apellidos or ''}".strip() or "Sin Nombre"

