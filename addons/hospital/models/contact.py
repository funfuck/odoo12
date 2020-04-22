# -*- coding: utf-8 -*-
from odoo import fields, models

class contact(models.Model):
    _inherit = 'res.partner'
    patient_id = fields.Many2one('hospital.patient', string="Patient")