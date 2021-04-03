# -*- coding: utf-8 -*-
# from odoo import http


# class StudentApp(http.Controller):
#     @http.route('/student_app/student_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_app/student_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_app.listing', {
#             'root': '/student_app/student_app',
#             'objects': http.request.env['student_app.student_app'].search([]),
#         })

#     @http.route('/student_app/student_app/objects/<model("student_app.student_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_app.object', {
#             'object': obj
#         })
