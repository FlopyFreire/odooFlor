# -*- coding: utf-8 -*-
from odoo import models, api

class ReporteEmpleadoReparto(models.AbstractModel):
    _name = 'report.empresa.reporte_empleado_reparto'
    _description = 'Reporte de Repartos Pendientes por Empleado'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['empresa.empleado'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'empresa.empleado',
            'docs': docs,
            'repartos': self.env['empresa.reparto'].search([('empleado_id', 'in', docids), ('estado', '=', 'no_ha_salido')])
        }
