from operator import index
from odoo import api
from odoo.tools.misc import unique
# from odoo.api import model, onchange
from random import choices
from odoo import models, fields
from odoo.exceptions import UserError, ValidationError
import datetime


bd_group = [
    ('a+', 'A+'),
    ('b+', 'B+'),
    ('o', 'O'),
    ('a-', 'A-'),
    ('b-', 'B-'),
    ('ab+', 'AB+'),
    ('ab-', 'AB-'),
]


class student_data(models.Model):
    _name = 'student.data'
    _rec_name = 'first_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    first_name = fields.Char(string='firstname', max_length=30)
    last_name = fields.Char(string='lastname', max_length=30)
    address = fields.Text(max_length=50)
    email = fields.Char(string='your_email', max_length=20)
    gender = fields.Selection(

        [('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    blood_group = fields.Selection(bd_group)
    age = fields.Integer(string="your age")
    country_code = fields.Integer(max_length=3)
    mobile = fields.Integer(max_length=10)
    register = fields.Boolean(default=False)
    dates = fields.Date(string="Date of Birth")
    # rdate = fields.Date.today()
    profestion = fields.Selection(
        [('other', 'Other'), ('professor', 'Professor')])
    email_data = fields.Html('Data of student')
    skill_list = fields.Many2many(
        'student.skill', 'student_hobby_relf', 'studenthobby_idd', 'hobby_idd')
    handle = fields.Integer()
    # res_id = fields.Many2one(
    #     'res.partner', string="Student")
    photo_id = fields.Image()
    student_line_ids = fields.One2many('student.data.lines', 'stu_id')
    state = fields.Selection(
        [('pending', 'Pending'), ('confirm', 'Confirm'),
         ('paid', 'Paid'), ('cancel', 'Cancel')], )
    course_count = fields.Integer(compute="course_select_count")

    _sql_constraints = [
        ('unique_phone_cons', 
        'unique(email)', 
        'phone must be unique'),

        # ('check age must be greater 18',
        # (),
        # CHECK(Age >= 18 AND City='Sandnes')),

    ]

    # security = fields.Text(groups='base.group_system')
    @api.constrains('last_name')
    def last_name_email_compulsory(self):
        print(f'\n\n\n\n{self.last_name}\n\n\n\n\n')
        for rec in self:
            if not rec.last_name:
                raise ValidationError("last name must be enter..")

    

    def name_get(self):
        result = []
        for field in self:
            # print(f'\n\ncheck forloop dharmesh  {self} \n\n')\
            # check forloop dharmesh  student.data(1,)
            result.append((field.id, "{} {}".format
                           (field.first_name, field.last_name)))
            # print(f'\n\ncheck forloop dharmesh  {result} \n\n')
            # check forloop dharmesh  [(1, 'sivam khachiya')]
        return result

    @api.onchange('student_line_ids')
    def onchange_add_course(self):
        print("\n\n selfffff =>", self)
        for student in self:
            print("\n\n line ==>", student.student_line_ids)
            if len(student.student_line_ids) > 0:
                student.write({'state': 'pending'})
            else:
                student.write({'state': ''})

    @api.onchange('dates')
    def onchange_dob(self):
        for rec in self:
            if rec.dates:
                val1 = rec.dates
                # print(f"\n\n\n\nhi dharmesh your age{val1}\n\n\n\n")
                val2 = datetime.date.today()
                # print(f"\n\n\n\nhi dharmesh your ageval2{val2}\n\n\n\n")
                rec.age = abs(((val2 - val1).days)//365)

    def action_confirm(self):
        for rec in self:
            if rec.student_line_ids.course_id:
                # print(f"\n\n\n\n\nhi confirm{rec}\n\n\n\n\n\n")
                # rec.state = "confirm"     # also direct store dasta to field
                rec.write({'state': 'confirm'})

    def action_paid(self):
        for rec in self:
            if rec.student_line_ids.course_id:
                # print(f"\n\n\n\n\nhi paid{rec}\n\n\n\n\n\n")
                rec.write({'state': 'paid'})

    def action_cancel(self):
        for rec in self:
            if rec.student_line_ids.course_id:
                rec.write({'state': 'cancel'})

    @api.model
    def create(self, vals):
        print(f"\n\n\n\n\nhi paid dhamaa create method\n\n\n\n\n\n")
        print(vals)

        readdata = self.env["student.data"].search_count(
            [("first_name", '=', vals["first_name"])])  # dict data access from val
        print(f'\n\n\n\n\n{readdata}')
        # readdata = self.env["student.data"].sudo().search_count(
        #     [("first_name", '=', vals["first_name"])])
        # readdata = self.env["courses.data"].search(
        #     [('course_names', '=', 'python')])
        # readdata=self.env["courses.data"].search([])
        # print(f"\n\n\n\n{readdata}\n\n")
        data_record = super(student_data, self).create(vals)
        print(data_record, "check bhai")

        if readdata:
            raise ValidationError("name must be unique..")
        else:
            return data_record

    # method call at time of update

    def write(self, vals):
        print(vals)
        for rec in self:
            readdata = self.env["courses.data"].search([])
            if readdata:
                # print(f"\n\n\n\n{readdata[0].course_names}\n\n")
                # print(f"\n\n\n\n\nhi dhamesh write method\n\n\n\n\n\n")
                # print(super().write(vals))
                # from multiple record acess perticular record
                # self.env["student.data"].create({"first_name": "manthanbhai"}) cmd
                print(readdata)
        return super(student_data, self).write(vals)

    def unlink(self):
        for rec in self:
            print("record set delete", self)
            rtn = super(student_data, self).unlink()
            print("return value", rtn)
        return rtn

    def stu_course_view(self):
        for rec in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'course form student',
                'view_mode': 'tree,form',
                'res_model': 'student.data.lines',
                'domain': [('stu_id', '=', rec.id)],

            }

    def course_select_count(self):
        for rec in self:
            # rec.course_count=10
            rec.course_count = self.env["student.data.lines"].search_count(
                [('stu_id', '=', self.id)])


class student_data_lines(models.Model):
    _name = "student.data.lines"

    profe = [
        ('kalam', 'Kalam'),
        ('navin', 'Navin'),
        ('sirg', 'Sirg'),

    ]
    course_id = fields.Many2one('courses.data', ondelete="set default")
    stu_id = fields.Many2one('student.data')

    professor_name = fields.Selection(profe)
    course_name = fields.Char(related='course_id.course_names')
    course_lengths = fields.Integer(
        related='course_id.course_length')
    course_amount = fields.Integer()
    # sale_id = fields.Many2one('sale.order',)
    # sales_field = fields.Float(related="sale_id.currency_rate")

    @api.onchange('course_id')
    def onchange_amount(self):
        for rec in self:

            if rec.course_id:
                rec.stu_id.state = 'pending'
                self.course_amount = rec.course_id.course_amount
        print(f"\n\n\n\n {self.course_amount, rec.course_amount,rec.id} \n\n\n\n"
              )
