# -*- coding: utf-8 -*-

from odoo import models, fields, api

class patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = "Hospital Patients"

    name = fields.Char(required=True, track_visibility='on_change')
    age = fields.Integer(required=True, track_visibility='on_change')
    gender = fields.Char(required=True)
    note = fields.Text(track_visibility='on_change')
    color = fields.Integer()

    age_group = fields.Char(string="Age Group", compute='_age_group')

    doctor_id = fields.Many2one('hospital.doctor',
        ondelete='set null', string="Doctor", required=True, group_expand='_read_group_stage_ids', track_visibility='on_change')

    @api.depends('age')
    def _age_group(self):
        for r in self:
            if r.age > 20:
                r.age_group = 'Major'
            else:
                r.age_group = 'Minor'
    
    @api.model
    def _read_group_stage_ids(self,stages,domain,order):
        stage_ids = self.env['hospital.doctor'].search([])
        return stage_ids


class patient(models.Model):
    _inherit = 'hospital.patient'

    gender = fields.Selection([ ('M', 'Male'),('F', 'Female'),], '', default='M', required=True, track_visibility='on_change')
