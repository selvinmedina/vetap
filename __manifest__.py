# -*- coding: utf-8 -*-
{
    'name': "vetapp",

    'summary': """
        Aprendienod ODOO 12 y 13 en un Master en ODOO 13 - Proyecto Vet Clinic """,

    'description': """
        Modulo de veterinaria
    """,

    'author': "Selvin Medina",
    'website': "http://www.github.com/selvinmedina",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}