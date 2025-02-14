# -*- coding: utf-8 -*-
# from odoo import http


# class BiblioComics(http.Controller):
#     @http.route('/biblio_comics/biblio_comics', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/biblio_comics/biblio_comics/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('biblio_comics.listing', {
#             'root': '/biblio_comics/biblio_comics',
#             'objects': http.request.env['biblio_comics.biblio_comics'].search([]),
#         })

#     @http.route('/biblio_comics/biblio_comics/objects/<model("biblio_comics.biblio_comics"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('biblio_comics.object', {
#             'object': obj
#         })

