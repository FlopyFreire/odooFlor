# hospital_flor/models/medicos.py
from odoo import models, fields

class HospitalFlorMedicos(models.Model):
    _name = 'hospital_flor.medicos'
    _description = 'Hospital Flor Medicos'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    id_colegiado = fields.Char(string='ID Colegiado', required=True)