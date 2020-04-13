# -*- coding: utf-8 -*-

from odoo import models, fields, api

class doctor(models.Model):
    _name = 'hospital.doctor'
    _description = "Hospital Doctors"

    name = fields.Char(required=True)
    age = fields.Integer(required=True)
    gender = fields.Char(required=True)

class doctor(models.Model):
    _inherit = 'hospital.doctor'

    gender = fields.Selection([ ('M', 'Male'),('F', 'Female'),], '', default='M', required=True)