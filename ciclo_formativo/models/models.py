# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ciclo_formativo(models.Model):
#     _name = 'ciclo_formativo.ciclo_formativo'
#     _description = 'ciclo_formativo.ciclo_formativo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

