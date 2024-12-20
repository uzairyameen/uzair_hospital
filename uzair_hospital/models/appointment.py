from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'  # Use `patient_id` as the display name

    reference = fields.Char(string='Reference', default="New")
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=False, ondelete='cascade')
    date_appointment = fields.Date(string="Date of Appointment")
    note = fields.Text(string="Note")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='draft', tracking=True)
    appointment_line_ids = fields.One2many(
        'hospital.appointment.line', 'appointment_id', string="Appointment Lines"
    )
    total_qty = fields.Float(compute='_compute_total_qty', string="Total Quantity", store=True)
    date_of_birth = fields.Date(string="DOB", related='patient_id.date_of_birth')

    @api.depends('appointment_line_ids.qty')  # Trigger computation when related lines change
    def _compute_total_qty(self):
        for rec in self:
            rec.total_qty = sum(rec.appointment_line_ids.mapped('qty'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)

    def action_ongoing(self):
        self.write({'state': 'ongoing'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_confirm(self):
         self.write({'state': 'confirmed'})
    
    def action_ongoing(self):
        self.write({'state': 'ongoing'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})


class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = 'Hospital Appointment Line'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment', required=True)
    product_id = fields.Many2one('product.product', string="Product", required=True)
    qty = fields.Float(string="Quantity", required=True)
