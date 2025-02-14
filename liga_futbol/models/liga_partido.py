from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LigaPartido(models.Model):
    _name = 'liga.partido'
    _description = 'Un partido de la liga'

    nombre = fields.Char(string='Nombre del Partido')
    descripcion = fields.Text(string='Descripción')

    # Equipos participantes en el partido
    equipo_casa = fields.Many2one('liga.equipo', string='Equipo local')
    goles_casa = fields.Integer()
    equipo_fuera = fields.Many2one('liga.equipo', string='Equipo visitante')
    goles_fuera = fields.Integer()

    # Validaciones para evitar equipos repetidos
    @api.constrains('equipo_casa', 'equipo_fuera')
    def _check_equipos_diferentes(self):
        """ Valida que los equipos no sean el mismo. """
        for record in self:
            if not record.equipo_casa:
                raise ValidationError('Debe seleccionarse un equipo local.')
            if not record.equipo_fuera:
                raise ValidationError('Debe seleccionarse un equipo visitante.')
            if record.equipo_casa == record.equipo_fuera:
                raise ValidationError('Los equipos del partido deben ser diferentes.')

    def actualizoRegistrosEquipo(self):
        """
        Recalcula la clasificación de todos los equipos desde cero.
        Se eliminan valores anteriores y se recalculan en base a los partidos jugados.
        """
        # Reiniciamos las estadísticas de todos los equipos
        for recordEquipo in self.env['liga.equipo'].search([]):
            recordEquipo.victorias = 0
            recordEquipo.empates = 0
            recordEquipo.derrotas = 0
            recordEquipo.goles_a_favor = 0
            recordEquipo.goles_en_contra = 0
            recordEquipo.puntos = 0  # Ahora sí se inicializa correctamente

        # Recalculamos las estadísticas en base a los partidos jugados
        for recordPartido in self.env['liga.partido'].search([]):
            equipo_casa = recordPartido.equipo_casa
            equipo_fuera = recordPartido.equipo_fuera

            if not equipo_casa or not equipo_fuera:
                continue  # Si falta algún equipo, ignoramos este partido

            diferencia_goles = recordPartido.goles_casa - recordPartido.goles_fuera

            # Actualizamos goles a favor y en contra
            equipo_casa.goles_a_favor += recordPartido.goles_casa
            equipo_casa.goles_en_contra += recordPartido.goles_fuera
            equipo_fuera.goles_a_favor += recordPartido.goles_fuera
            equipo_fuera.goles_en_contra += recordPartido.goles_casa

            # Reglas para la asignación de puntos
            if diferencia_goles >= 4:
                # Si gana con 4 o más goles de diferencia
                equipo_casa.puntos += 4
                equipo_fuera.puntos -= 1 if equipo_fuera.puntos > 0 else 0  # Evitamos valores negativos
                equipo_casa.victorias += 1
                equipo_fuera.derrotas += 1
            elif diferencia_goles > 0:
                # Si gana con menos de 4 goles de diferencia
                equipo_casa.puntos += 3
                equipo_casa.victorias += 1
                equipo_fuera.derrotas += 1
            elif diferencia_goles == 0:
                # Si hay empate
                equipo_casa.puntos += 1
                equipo_fuera.puntos += 1
                equipo_casa.empates += 1
                equipo_fuera.empates += 1
            else:
                # Si el equipo visitante gana
                diferencia_goles = abs(diferencia_goles)  # Convertimos la diferencia en positiva
                if diferencia_goles >= 4:
                    equipo_fuera.puntos += 4
                    equipo_casa.puntos -= 1 if equipo_casa.puntos > 0 else 0  # Evitamos negativos
                    equipo_fuera.victorias += 1
                    equipo_casa.derrotas += 1
                else:
                    equipo_fuera.puntos += 3
                    equipo_fuera.victorias += 1
                    equipo_casa.derrotas += 1

    # API onchange para cuando se modifica un partido
    @api.onchange('equipo_casa', 'goles_casa', 'equipo_fuera', 'goles_fuera')
    def actualizar(self):
        self.actualizoRegistrosEquipo()

    # Sobrescribo el borrado (unlink)
    def unlink(self):
        # Borro el registro, que es lo que hace el metodo normalmente
        result = super(LigaPartido, self).unlink()
        # Añado que llame a actualizoRegistroEquipo()
        self.actualizoRegistrosEquipo()
        return result

    # Sobreescribo el metodo crear
    @api.model
    def create(self, values):
        # Hago lo normal del metodo create
        result = super().create(values)
        # Añado esto: llamo a la funcion que actualiza la clasificacion
        self.actualizoRegistrosEquipo()
        # Hago lo normal del metodo create
        return result

    # Añadir 2 goles al equipo de casa y actualizar la clasificación
    def sumar_goles_casa(self):
        self.goles_casa += 2
        self.actualizoRegistrosEquipo()

    def sumar_goles_fuera(self):
        self.goles_fuera += 2
        self.actualizoRegistrosEquipo()

    def reporte_partido(self):
        report_name = f"Reporte_Partido_{self.id}"  # Generamos el nombre dinámico aquí
        return self.env.ref('liga_futbol.reporte_partido').report_action(self, report_name=report_name)
