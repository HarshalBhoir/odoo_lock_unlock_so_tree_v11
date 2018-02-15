# -*- coding: utf-8 -*-
# Copyright 2018 Vignesh @ Annadurai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Lock Unlock SO from tree",

    'summary': """
        Lock / unlock SO from Tree itself, Only works for version 11
      """,
    'author': " Vignesh ",
    'website': "viki2.odoo.com",
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'category': 'Sale',
    'version': '11.0.0.1',
    'depends': ['base', 'sale',
                ],
     'images': ['images/main_screenshot.png'],
    'data': [
        'views/sale_views.xml',
    ],
    'demo': [
    ],
}
