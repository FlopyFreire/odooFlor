# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Definimos el modelo LigaEquipo, que almacena información de cada equipo
class LigaEquipo(models.Model):
    _name = 'liga.equipo'
    _description = 'Equipo de la liga'
    _order = 'nombre'
    _rec_name = 'nombre'  # Indicamos que se use el atributo "nombre" como identificador

    # Atributos del equipo
    nombre = fields.Char('Nombre equipo', required=True, index=True)
    escudo = fields.Image('Escudo equipo', max_width=50, max_height=50)
    fecha_fundacion = fields.Date('Fecha fundación')
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)

    # Estadísticas del equipo
    victorias = fields.Integer(default=0)
    empates = fields.Integer(default=0)
    derrotas = fields.Integer(default=0)
    
    # Campo calculado para el total de partidos jugados
    jugados = fields.Integer(compute="_compute_jugados", store=True)

    @api.depends('victorias', 'empates', 'derrotas')
    def _compute_jugados(self):
        """ Calcula el total de partidos jugados. """
        for record in self:
            record.jugados = record.victorias + record.empates + record.derrotas

    # ⚠️ Eliminamos el compute en 'puntos' para evitar conflictos
    puntos = fields.Integer(default=0)

    # Goles a favor y en contra
    goles_a_favor = fields.Integer()
    goles_en_contra = fields.Integer()

    # Restricción única en el nombre del equipo
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (nombre)', 'El nombre del equipo ya existe.')
    ]

    # Validación de la fecha de fundación
    @api.constrains('fecha_fundacion')
    def _check_release_date(self):
        """ Valida que la fecha de fundación no sea en el futuro. """
        for record in self:
            if record.fecha_fundacion and record.fecha_fundacion > fields.Date.today():
                raise ValidationError('La fecha de fundación del club debe ser anterior a la actual')
