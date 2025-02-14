# -*- coding: utf-8 -*-
{
    'name': "UD07_Parte2Flor",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Flor Ibarra",
    'website': "https://www.odoo.com",
    'instalable': True,
    'aplicación': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/empleado_views.xml',
        'views/vehiculo_view.xml',
        'views/cliente_view.xml',
        'views/reparto_view.xml',
        'views/menu_views.xml',
        'wizard/wizard_reparto_view.xml',
        'reports/reporte_empleado_reparto_template.xml',
        'reports/report_empleado_reparto_action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

