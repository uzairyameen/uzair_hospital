{
    'name': 'Hospital',
    'version': '17.0.1.1',
    'category': 'Uncategorized',
    'summary': 'A hospital management module',
    'description': 'Module for managing hospital operations',
    'author': 'Uzair',
    'depends': [
        'mail',  # Only keep if you're using the mail functionality
        'product',
        'account'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient_views.xml',
        'views/patient_readonly_views.xml',
        'views/appointment_views.xml',
        'views/appointment_lines_views.xml',
        'views/patient_tag_views.xml',
        'views/account_move_views.xml',
        'views/menu.xml',# Added the frontend template
    ],
    'installable': True,
    'application': True,
}






