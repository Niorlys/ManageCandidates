# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class Candidate(models.Model):
    _inherit = "res.partner"
    _order="id desc"

    plus_ids = fields.Many2many("plus.techs")
    skill_ids = fields.One2many("convocatory.skill", "candidate_id")
    convocatory_id = fields.Many2one("recruitment.convocatory")
    candidate = fields.Boolean(default = False)
    age = fields.Integer(string='Age')
    ci = fields.Char(string="DNI")

    _sql_constraints = [('check_ci', 'UNIQUE(ci)',f'There is a candidate with the same CI')]

    @api.constrains('age')
    def _check_age(self):
        if not (17 < self.age < 45):
            raise UserError("Candidate's age must be in range 18-45.")



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
    costs = fields.Monetary("Estimated costs", "currency_id", copy=False)
    currency_id = fields.Many2one("res.currency")
    candidate_ids = fields.One2many("res.partner", 'convocatory_id')
    job_id = fields.Many2many("convocatory.job")
    color = fields.Integer()

    def cancel_convocatory(self):
        self.state="C"
        return True



class Job(models.Model):
    _name ="convocatory.job"
    _description = "Job Model"
    title = fields.Char(required=True)
    location = fields.Char()
    mode = fields.Selection(string="Mode", selection=[('R', 'Remote'), ('H','Hybrid'), ('P','In Person')],copy = False, default = "R")
    job_description = fields.Html()
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
    candidate_id = fields.Many2one("res.partner")

class PlusTechs(models.Model):
    _name="plus.techs"
    _description="Development enviroment tools"

    name = fields.Char()
    color = fields.Integer()

