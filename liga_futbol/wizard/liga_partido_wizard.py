from odoo import models, fields

class LigaPartidoWizard(models.TransientModel):
    _name = 'liga.partido.wizard'

    # Campos del modelo que usaremos en el Wizard
    nombre = fields.Char()
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)

    # Relacionar con el modelo 'liga.equipo' (o el que uses para equipos)
    equipo_casa = fields.Many2one('liga.equipo', string="Equipo Casa")
    goles_casa = fields.Integer(string="Goles Casa")
    equipo_fuera = fields.Many2one('liga.equipo', string="Equipo Fuera")
    goles_fuera = fields.Integer(string="Goles Fuera")

    def add_liga_partido(self):
        ligaPartidoModel = self.env['liga.partido']
        for wiz in self:
            ligaPartidoModel.create({
                'nombre': wiz.nombre,
                'descripcion': wiz.descripcion,
                'equipo_casa': wiz.equipo_casa.id,
                'goles_casa': wiz.goles_casa,
                'equipo_fuera': wiz.equipo_fuera.id,
                'goles_fuera': wiz.goles_fuera,
            })
