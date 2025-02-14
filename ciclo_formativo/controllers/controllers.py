# -*- coding: utf-8 -*-
# from odoo import http


# class CicloFormativo(http.Controller):
#     @http.route('/ciclo_formativo/ciclo_formativo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ciclo_formativo/ciclo_formativo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ciclo_formativo.listing', {
#             'root': '/ciclo_formativo/ciclo_formativo',
#             'objects': http.request.env['ciclo_formativo.ciclo_formativo'].search([]),
#         })

#     @http.route('/ciclo_formativo/ciclo_formativo/objects/<model("ciclo_formativo.ciclo_formativo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ciclo_formativo.object', {
#             'object': obj
#         })

