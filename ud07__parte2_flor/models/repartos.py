# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Reparto(models.Model):
    _name = 'empresa.reparto'
    _description = 'Reparto'
    _rec_name = 'codigo'
    _order = 'fecha_recepcion, urgencia'

    codigo = fields.Char(string="Código", required=True, copy=False, readonly=True, index=True, default=lambda self: 'Nuevo')
    fecha_hora_inicio = fields.Datetime(string="Fecha y Hora de Inicio", required=True)
    fecha_hora_retorno = fields.Datetime(string="Fecha y Hora de Retorno")
    fecha_recepcion = fields.Datetime(string="Fecha de Recepción", required=True)
    empleado_id = fields.Many2one('empresa.empleado', string="Repartidor", required=True)
    vehiculo_id = fields.Many2one('empresa.vehiculo', string="Vehículo", required=True)
    distancia_km = fields.Float(string="Kilómetros del Reparto", required=True)
    peso_kg = fields.Float(string="Peso del Paquete (kg)", required=True)
    volumen_m3 = fields.Float(string="Volumen del Paquete (m³)", required=True)
    observaciones = fields.Text(string="Observaciones")
    estado = fields.Selection([
        ('no_ha_salido', 'No ha salido'),
        ('de_camino', 'De camino'),
        ('entregada', 'Entregada')
    ], string="Estado de la Entrega", default='no_ha_salido')
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

    @api.model
    def create(self, vals):
        if vals.get('codigo', 'Nuevo') == 'Nuevo':
            vals['codigo'] = self.env['ir.sequence'].next_by_code('empresa.reparto') or 'Nuevo'
        result = super(Reparto, self).create(vals)
        return result

    @api.constrains('empleado_id', 'vehiculo_id', 'distancia_km')
    def _check_valid_delivery(self):
        for record in self:
            if record.vehiculo_id.tipo == 'ciclomotor' and not record.empleado_id.tiene_licencia_moto:
                raise ValidationError("El empleado no tiene carné de ciclomotor")
            if record.vehiculo_id.tipo == 'furgoneta' and not record.empleado_id.tiene_licencia_furgoneta:
                raise ValidationError("El empleado no tiene carné de furgoneta")

            viajes_activos = self.env['empresa.reparto'].search([
                ('empleado_id', '=', record.empleado_id.id),
                ('vehiculo_id', '=', record.vehiculo_id.id),
                ('estado', 'in', ['no_ha_salido', 'de_camino']),
                ('id', '!=', record.id)  # Ignorar el propio registro al validar
            ])
            if viajes_activos:
                raise ValidationError("El empleado o el vehículo ya están de viaje")

            if record.distancia_km > 10 and record.vehiculo_id.tipo == 'bicicleta':
                raise ValidationError("Los repartos de más de 10 km no se pueden realizar en bicicleta")
            if record.distancia_km < 1 and record.vehiculo_id.tipo == 'furgoneta':
                raise ValidationError("Los repartos de menos de 1 km no se pueden realizar en furgoneta")
