# biblio_comics/models/ejemplar_prestamo.py
from odoo import models, fields, api

class EjemplarPrestamo(models.Model):
    _name = 'ejemplar.prestamo'
    _description = 'Ejemplar de Comic para Prestamo'

    comic_id = fields.Many2one('biblioteca.comic', string='Comic', required=True)
    socio_id = fields.Many2one('biblio_comics.socios', string='Socio')
    fecha_inicio = fields.Date('Fecha de Inicio', required=True)
    fecha_fin = fields.Date('Fecha Prevista de Regreso', required=True)

    @api.constrains('fecha_inicio')
    def _check_fecha_inicio(self):
        for record in self:
            if record.fecha_inicio > fields.Date.today():
                raise models.ValidationError('La fecha de préstamo no puede ser posterior al día de hoy')

    @api.constrains('fecha_fin')
    def _check_fecha_fin(self):
        for record in self:
            if record.fecha_fin < fields.Date.today():
                raise models.ValidationError('La fecha prevista de regreso no puede ser anterior al día de hoy')

    def name_get(self):
        result = []
        for record in self:
            name = f"Préstamo - {record.comic_id.nombre}" if record.comic_id else "Nuevo préstamo"
            result.append((record.id, name))
        return result
