# -*- coding: utf-8 -*-
{
    'name': 'Hospital management',
    'author': 'deepak',
    'version': '1.1',
    'summary': 'Hospital app',
    'sequence': 30,
    'description': """
application
    """,
    'category': 'Managing',
    'depends': ['base'],
    'data': ['view/hospital_info_view.xml',
             'view/hospital_floor_view.xml',
             'view/hospital_facility_view.xml'],
    'installable': True,
    'application': False,
    'auto_install': False,
}