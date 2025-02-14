# hospital_flor/models/pacientes.py

from odoo import models, fields

class HospitalFlorPacientes(models.Model):
    _name = 'hospital_flor.pacientes'
    _description = 'Hospital Flor Pacientes'

    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellidos', required=True)
    sintomas = fields.Text(string='Síntomas')