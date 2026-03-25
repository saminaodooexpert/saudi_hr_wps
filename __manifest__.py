{
    'name': 'Saudi Payroll WPS Expert - Al-Rajhi & SNB',
    'version': '17.0.1.0.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Generate Saudi WPS Excel files for Al-Rajhi and SNB Banks with 1-click.',
    'description': """
        Expert solution for KSA companies. Generate Wage Protection System (WPS) 
        compliant Excel files directly from Odoo. 
        Features: 
        - Separate Basic & Housing Allowance.
        - Iqama/ID validation.
        - Bank-ready Excel format.
    """,
    'author': 'Shameena Moin Qaisar',
    'depends': ['hr', 'hr_payroll'],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'price': 69.00,
    'currency': 'USD',
    'license': 'OPL-1',
}
