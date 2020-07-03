# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'AWS SMS Sale',
    'version': '10.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'sale', 'aws_sms', 'phone_code'],
    'data': [        
        'views/sale_order_view.xml',        
    ],
    'installable': True,
    'auto_install': False,    
}