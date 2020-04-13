# -*- coding: utf-8 -*-

from odoo import models, fields, api

class patient(models.Model):
    _name = 'hospital.patient'
    _description = "Hospital Patients"

    name = fields.Char(required=True)
    age = fields.Integer(required=True)
    gender = fields.Char(required=True)
    note = fields.Text()

    age_group = fields.Char(string="Age Group", compute='_age_group')

    @api.depends('age')
    def _age_group(self):
        for r in self:
            if r.age > 20:
                r.age_group = 'Major'
            else:
                r.age_group = 'Minor'


class patient(models.Model):
    _inherit = 'hospital.patient'

    gender = fields.Selection([ ('M', 'Male'),('F', 'Female'),], '', default='M', required=False)
