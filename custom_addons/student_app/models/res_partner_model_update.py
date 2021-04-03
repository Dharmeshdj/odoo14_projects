from odoo import models, fields
import datetime
from odoo import api


class ResPartnerUpdate(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean()
    is_data = fields.Boolean()
    conutry = fields.Selection(
        [('india', 'India'), ('uk', 'Uk')])
    student_id = fields.Many2one('student.data')
    # dob = fields.Date(related='student_id.dates')
    # age = fields.Integer(compute='compute_age',store=False)
    
    age = fields.Integer()

    @api.depends('student_id.country_code')
    def compute_age(self):
        print("\n\n\n\ncalling\n\n\n\n")
        # self.age = 20
        for rec in self:
            rec.age = 0
            if rec.student_id.dates:
                val1 = rec.student_id.dates
                # print(f"\n\n\n\nhi dharmesh your age{val1}\n\n\n\n")
                val2 = datetime.date.today()
                # print(f"\n\n\n\nhi dharmesh your ageval2{val2}\n\n\n\n")
                rec.age = abs(((val2 - val1).days)//365)
