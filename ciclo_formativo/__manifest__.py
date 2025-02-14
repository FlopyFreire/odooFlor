# -*- coding: utf-8 -*-
{
    'name': "CICLO FORMATIVO",

    'summary': "Gestión de ciclos formativos, módulos, alumnado y profesores",

    'description': """
Gestión educativa
    """,

    'application': True,
    'author': "Flor",
    'website': "odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'education',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/groups.xml',  
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/modulo_views.xml',
        'views/alumno_views.xml',
        'views/profesor_views.xml',
        'views/ciclo_formativo_views.xml',
        

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

