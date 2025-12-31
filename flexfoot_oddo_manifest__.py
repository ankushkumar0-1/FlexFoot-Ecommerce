{
    'name': 'FlexFoot Ecommerce',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Online Shoe Store using Odoo',
    'description': 'An e-commerce website for selling shoes online.',
    'author': 'Ankush Kumar',
    'depends': ['website', 'website_sale'],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'flexfoot_odoo_module/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': True,
}
