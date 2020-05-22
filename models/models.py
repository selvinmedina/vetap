# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vetapp_animal(models.Model):
    _name = 'vetapp.animal'

    name = fields.Char("Animal Name")
    species_id = fields.Many2one("vetapp.species")
    breed_id = fields.Many2one("vetapp.breed")
    owner_id = fields.Many2one('res.partner')
    spoyorneuter = fields.Boolean("Spayed or Neutered")
    birthdate = fields.Date("Birth Date")
    diagnosis_ids = fields.Many2many('vetapp.diagnosis')
    notes = fields.Text()

class vetapp_species(models.Model):
    _name = "vetapp.species"
    name = fields.Char("Species")
    animal_ids = fields.One2many("vetapp.animal", "species_id")
    notes = fields.Text()

class vetapp_breed(models.Model):
    _name = "vetapp.breed"
    name = fields.Text()
    animal_ids = fields.One2many("vetapp.animal", "breed_id")

class vetapp_partner(models.Model):
    _inherit = 'res.partner'
    orientation_completed = fields.Boolean("Orientation Completed")
    orientation_staff_id = fields.Many2one("res.users")
    animal_ids = fields.One2many('vetapp.animal', 'owner_id', 'Pets')

class vetapp_diagnosis(models.Model):
    _name = 'vetapp.diagnosis'
    name = fields.Char()
    code = fields.Char('Diagnostic Code')
    symptom_ids = fields.Many2many('vetapp.symptom')
    treatment_ids = fields.Many2many('vetapp.treatment')
    notes = fields.Text()

class vetapp_symptom(models.Model):
    _name = 'vetapp.symptom'
    name = fields.Char()
    code = fields.Char('Symptom Code')
    diagnosis_ids = fields.Many2many('vetapp.diagnosis')
    notes = fields.Text()

class vetapp_treatment(models.Model):
    _name = 'vetapp.treatment'
    name = fields.Char()
    code = fields.Char('Treatment Code')
    notes = fields.Text()
    product_ids = fields.Many2many("product.template")
    diagnosis_ids = fields.Many2many('vetapp.diagnosis')

class vetapp_products(models.Model):
    _inherit = 'product.template'
    treatment_ids = fields.Many2many('vetapp.treatment')
