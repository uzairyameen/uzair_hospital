from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        string="Gender",
        tracking=True,
        required=True
    )

    tag_ids = fields.Many2many(
        'patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string='Tags'
    )
    is_minor = fields.Boolean(string="Minor")
    guardian = fields.Char(string="Guardian")

    def unlink(self):
        for rec in self:
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise UserError(
                    _("You cannot delete the patient '%s' because an appointment is present.") % rec.name
                )
        return super(HospitalPatient, self).unlink()


