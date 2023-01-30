# -*- coding: utf-8 -*-
# from odoo import http


# class StaffRecruitment(http.Controller):
#     @http.route('/staff_recruitment/staff_recruitment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/staff_recruitment/staff_recruitment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('staff_recruitment.listing', {
#             'root': '/staff_recruitment/staff_recruitment',
#             'objects': http.request.env['staff_recruitment.staff_recruitment'].search([]),
#         })

#     @http.route('/staff_recruitment/staff_recruitment/objects/<model("staff_recruitment.staff_recruitment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('staff_recruitment.object', {
#             'object': obj
#         })
