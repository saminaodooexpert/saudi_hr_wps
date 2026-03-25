from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    x_iqama_id = fields.Char(string='Iqama/ID Number', help="Saudi National ID or Iqama Number")
    x_bank_iban = fields.Char(string='Bank IBAN', help="Full KSA IBAN starting with SA")
