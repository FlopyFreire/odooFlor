# -*- coding: utf-8 -*-
{
    'name': "HOSPITAL",

    'summary': "Gestión de pacientes y médicos del hospital",

    'description': """
Gestión hospitalaria
================
    """,

    'application': True,
    'author': "Flor",
    'website': "odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Healthcare',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/pacientes_views.xml',
        'views/medicos_views.xml',
        'views/diagnostico_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

