from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    x_iqama_id = fields.Char(string='Iqama/ID Number', help="Enter Saudi Iqama or National ID")
    x_bank_iban = fields.Char(string='Bank IBAN (KSA)', help="Enter full IBAN starting with SA")
