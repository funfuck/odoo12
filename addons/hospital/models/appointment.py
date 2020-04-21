# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class appointment(models.Model):
    _name = 'hospital.appointment'
    _description = "Hospital Appointments"

    patient_id = fields.Many2one('hospital.patient',
        ondelete='set null', string="Patient", required=True)

    doctor_id = fields.Many2one('hospital.doctor',
        ondelete='set null', string="Doctor", required=True)

    datetime = fields.Date(default=fields.Date.today, required=True)

    patient_code_name = fields.Char(string="Patient", compute='_patient_code_name')
    doctor_code_name = fields.Char(string="Doctor", compute='_doctor_code_name')

    @api.depends('patient_id')
    def _patient_code_name(self):
        for r in self:
            r.patient_code_name =  '%s: %s' % (r.patient_id.patient_code, r.patient_id.name)

    @api.depends('doctor_id')
    def _doctor_code_name(self):
        for r in self:
            r.doctor_code_name =  '%s: %s' % (r.doctor_id.doctor_code, r.doctor_id.name)
