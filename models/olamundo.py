from odoo import models , fields , api

class olamundo(models.Model):
    _name='odoo_olamundo.olamundo'
    _description = 'Exemplo olamundo'

    name = fields.Char(String="Ola Mundo:")
