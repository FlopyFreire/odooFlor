# -*- coding: utf-8 -*-
# from odoo import http


# class Ud07Parte2Flor(http.Controller):
#     @http.route('/ud07__parte2_flor/ud07__parte2_flor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ud07__parte2_flor/ud07__parte2_flor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ud07__parte2_flor.listing', {
#             'root': '/ud07__parte2_flor/ud07__parte2_flor',
#             'objects': http.request.env['ud07__parte2_flor.ud07__parte2_flor'].search([]),
#         })

#     @http.route('/ud07__parte2_flor/ud07__parte2_flor/objects/<model("ud07__parte2_flor.ud07__parte2_flor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ud07__parte2_flor.object', {
#             'object': obj
#         })

