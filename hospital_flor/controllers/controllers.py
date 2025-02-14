# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalFlor(http.Controller):
#     @http.route('/hospital_flor/hospital_flor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_flor/hospital_flor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_flor.listing', {
#             'root': '/hospital_flor/hospital_flor',
#             'objects': http.request.env['hospital_flor.hospital_flor'].search([]),
#         })

#     @http.route('/hospital_flor/hospital_flor/objects/<model("hospital_flor.hospital_flor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_flor.object', {
#             'object': obj
#         })

