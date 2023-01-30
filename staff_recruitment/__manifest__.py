# -*- coding: utf-8 -*-
{
    'name': "StaffRecruitment",

    'summary': """
        Simple app to manage candidates in a recruitment process""",

    'description': """
        Staff Recruitment Management
        ============================

        This app allows to create a recruitment process through a easy plan development.
    """,

    'author': "Niorlys Ernesto Campos",

    'category': 'Human Resources/RecruitmentDevelopment',
    'version': '0.1',

    'license':'LGPL-3',

    'depends': ['base'],

    "application": True,

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
