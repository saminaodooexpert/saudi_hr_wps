from odoo import models, fields, api
import base64
import io

class SaudiWPSWizard(os.TransientModel):
    _name = 'saudi.wps.wizard'
    _description = 'Saudi WPS Generator'

    file_data = fields.Binary('WPS File', readonly=True)
    file_name = fields.Char('File Name', readonly=True)

    def action_generate_wps(self):
        # Yeh code Excel file ka dhancha banayega
        output = io.BytesIO()
        # Hum filhaal simple CSV/Excel logic ka rasta de rahe hain
        content = "Employee ID,Bank IBAN,Salary,Housing,Net Salary\n"
        employees = self.env['hr.employee'].search([('x_iqama_id', '!=', False)])
        
        for emp in employees:
            content += f"{emp.x_iqama_id},{emp.x_bank_iban or ''},0,0,0\n"
            
        self.write({
            'file_data': base64.b64encode(content.encode()),
            'file_name': 'Saudi_WPS_Report.csv'
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'saudi.wps.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }
