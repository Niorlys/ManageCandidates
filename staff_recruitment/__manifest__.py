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

    'category': 'Human Resources/Recruitment Development',
    'version': '0.1',

    'license':'LGPL-3',

    'depends': ['base'],

    "application": True,

    'data': [
        'security/staff_recruitment_security.xml',
        'security/ir.model.access.csv',
        'views/recruitment_convocatory_views.xml',
        'views/skill_views.xml',
        'views/candidate_views.xml',
        'views/job_views.xml',
        'views/experience_views.xml',
        'report/report_templates.xml',
        'report/report_views.xml',
        'views/report_model_views.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
