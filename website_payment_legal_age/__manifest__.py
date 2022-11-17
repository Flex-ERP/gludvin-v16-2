# -*- coding: utf-8 -*-
{
    'name': "Website Payment Legal Age",

    'summary': """
    Add checkbox for agree that customer is over legal age.
    """,

    'description': """
    """,

    'author': "FlexERP Aps",
    'website': "https://www.flexerp.dk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/payment_footer.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_payment_legal_age/static/src/js/website_sale_payment.js'
        ]
    }
}
