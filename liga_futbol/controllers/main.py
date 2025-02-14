# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)

# Clase del controlador web
class Main(http.Controller):
    @http.route('/ligafutbol/equipo/json', type='http', auth='none')
    def obtenerDatosEquiposJSON(self):
        equipos = request.env['liga.equipo'].sudo().search([])
        listaDatosEquipos = []
        for equipo in equipos:
            listaDatosEquipos.append([equipo.nombre, str(equipo.fecha_fundacion), equipo.jugados, equipo.puntos, equipo.victorias, equipo.empates, equipo.derrotas])
        json_result = json.dumps(listaDatosEquipos)
        return json_result

    @http.route('/eliminarempates', type='http', auth='public', methods=['GET'], csrf=False)
    def eliminar_empates(self):
        _logger.info("Iniciando eliminación de partidos empatados")
        try:
            # Buscar todos los partidos
            partidos = request.env['liga.partido'].sudo().search([])
            
            # Filtrar los partidos donde los goles sean iguales
            partidos_empates = partidos.filtered(lambda p: p.goles_casa == p.goles_fuera)
            
            num_eliminados = len(partidos_empates)
            _logger.info("Número de partidos empatados encontrados: %d", num_eliminados)
            
            # Eliminar los partidos empatados
            if num_eliminados > 0:
                partidos_empates.unlink()
                _logger.info("Eliminación completada")
            
            return "Número de partidos eliminados: %d" % num_eliminados
        except Exception as e:
            _logger.error("Error eliminando partidos empatados: %s", str(e))
            return "Error eliminando partidos empatados: %s" % str(e)


