# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class doctor(models.Model):
    _name = 'hospital.doctor'
    _description = "Hospital Doctors"

    name = fields.Char(required=True)
    age = fields.Integer(required=True)
    gender = fields.Selection([ ('M', 'Male'),('F', 'Female'),], '', default='M', required=True)
    doctor_code = fields.Char(string='Doctor Code', required=True, copy=False, readonly=True,
                   index=True, default=lambda self: _('drxxx'))

    user_ref = fields.Many2one('res.users',
        ondelete='set null', string="User", index=True)

    @api.model
    def create(self, vals):
        if vals.get('doctor_code', _('drxxx')) == _('drxxx'):
            vals['doctor_code'] = self.env['ir.sequence'].next_by_code('hospital.doctor.sequence') or _('drxxx')
        res = super(doctor, self).create(vals)
        return res