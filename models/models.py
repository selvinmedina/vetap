# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vetapp_animal(models.Model):
    _name = 'vetapp.animal'

    name = fields.Char("Animal Name")
    species = fields.Char("Species")
    spoyorneuter = fields.Boolean("Spayed or Neutered")
    birthdate = fields.Date("Birth Date")
    notes = fields.Text()



    # las propiedades computadas son con una funcion
    # breed = fields.Float(compute="_value_pc", store=True)

#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100