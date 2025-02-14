# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Empresa(http.Controller):
    @http.route('/empresa/reparto/estado', type='http', auth='public', methods=['GET'], csrf=False)
    def estado_reparto(self, codigo_reparto, **kwargs):
        reparto = request.env['empresa.reparto'].sudo().search([('codigo', '=', codigo_reparto)], limit=1)
        if reparto:
            return str(reparto.estado)
        return "Reparto no encontrado"
