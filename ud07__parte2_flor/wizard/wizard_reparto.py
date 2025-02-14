# -*- coding: utf-8 -*-
from odoo import models, fields, api

class WizardReparto(models.TransientModel):
    _name = 'empresa.wizard_reparto'
    _description = 'Wizard para Crear Reparto'

    empleado_id = fields.Many2one('empresa.empleado', string="Repartidor", required=True)
    vehiculo_id = fields.Many2one('empresa.vehiculo', string="Vehículo", required=True)
    distancia_km = fields.Float(string="Kilómetros del Reparto", required=True)
    peso_kg = fields.Float(string="Peso del Paquete (kg)", required=True)
    volumen_m3 = fields.Float(string="Volumen del Paquete (m³)", required=True)
    observaciones = fields.Text(string="Observaciones")
    cliente_emisor_id = fields.Many2one('empresa.cliente', string="Cliente Emisor", required=True)
    nombre_receptor = fields.Char(string="Nombre del Receptor", required=True)
    apellidos_receptor = fields.Char(string="Apellidos del Receptor", required=True)
    urgencia = fields.Selection([
        ('organos', 'Órganos Humanos'),
        ('alimentos_refrigerados', 'Alimentos Refrigerados'),
        ('alimentos', 'Alimentos'),
        ('alta_prioridad', 'Alta Prioridad'),
        ('baja_prioridad', 'Baja Prioridad')
    ], string="Urgencia", required=True)

    def crear_reparto(self):
        self.ensure_one()
        reparto = self.env['empresa.reparto'].create({
            'fecha_hora_inicio': fields.Datetime.now(),
            'empleado_id': self.empleado_id.id,
            'vehiculo_id': self.vehiculo_id.id,
            'distancia_km': self.distancia_km,
            'peso_kg': self.peso_kg,
            'volumen_m3': self.volumen_m3,
            'observaciones': self.observaciones,
            'cliente_emisor_id': self.cliente_emisor_id.id,
            'nombre_receptor': self.nombre_receptor,
            'apellidos_receptor': self.apellidos_receptor,
            'urgencia': self.urgencia,
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'empresa.reparto',
            'view_mode': 'form',
            'res_id': reparto.id,
            'target': 'current',
        }
