# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Recruitment_Convocatory(models.Model):
    _name = 'recruitment.convocatory'
    _description = 'Convocatory to start a recruitment process.'

    name = fields.Char(required=True)
    description = fields.Text()
    vacancies = fields.Integer(default=1)
    recruiter_id = fields.Many2one("res.users","Recruiter",default=lambda s: s.env.user)
    strategy = fields.Selection(string = 'Strategy', selection=[('T','Training'), ('O','From outside'), ('RS', 'Recruitment Sources')])
    state = fields.Selection(string="Status", selection=[('N', 'New'), ('T','Testing'), ('I','Interview'),('S','Selecting'),
                                    ('H', 'Hiring'),('OB', 'Onboarding'),('C','Canceled')],copy = False, default = "N")
    costs = fields.Monetary("Estimated costs", "currency_id")
    currency_id = fields.Many2one("res.currency")



class Job(models.Model):
    _name ="convocatory.job"
    _description = "Job Model"
    title = fields.Char(required=True)
    location = fields.Char()
    mode = fields.Selection(string="Mode", selection=[('R', 'Remote'), ('H','Hybrid'), ('P','In Person')],copy = False, default = "R")
    job_description = fields.Text()
    skill_ids = fields.One2many("convocatory.skill", "job_id")
    deadline = fields.Date()
    salary = fields.Monetary("Salary", "currency_id")
    currency_id = fields.Many2one("res.currency")
    convocatory_id = fields.Many2one("recruitment.convocatory")

class Skill(models.Model):
    _name="convocatory.skill"
    _description="Technology"
    name = fields.Char(required=True)
    experience = fields.Integer(string="Experience (years)")
    job_id = fields.Many2one("convocatory.job")