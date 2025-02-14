# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lista_tareas(models.Model):
    _name = 'lista_tareas.lista_tareas'
    _description = 'Nueva tarea'
    _rec_name="tarea"
    
    
    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    fecha_inicio = fields.Datetime(string='Fecha Inicio')
    fecha_fin = fields.Datetime(string='Fecha Fin')
#
    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            if record.prioridad > 10:
                record.urgente = True
            else:
                record.urgente = False