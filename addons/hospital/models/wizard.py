# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'hospital.wizard'
    _description = "Wizard: Quick Appointment"

    def _default_patient(self):
        return self.patient_id.name

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True, default=_default_patient)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    datetime = fields.Date(default=fields.Date.today, required=True)

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'doctor_id': self.doctor_id.id,
            'datetime': self.datetime,
        }
        self.env['hospital.appointment'].create(vals)