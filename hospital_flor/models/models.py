# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class hospital_flor(models.Model):
#     _name = 'hospital_flor.hospital_flor'
#     _description = 'hospital_flor.hospital_flor'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

