from odoo import models, fields


class Courses(models.Model):
    _name = "courses.data"
    _rec_name = "course_names"

    course_names = fields.Char(string="Course Name")
    course_length = fields.Integer(
        max_length=2)
    course_amount = fields.Integer()
    course_active = fields.Boolean()

    def unlink(self):
        print('\n\n\n\n\n\n-----------------------LLamada a unlink address')
        print(self)
        print(self.course_names)

        # course_remove = self.env["student.data"].search(
        #     [("student_line_ids.course_id.course_names", "=", self.course_names)])
        # for rec in course_remove:
        #     rec.student_line_ids.unlink()

        return super(Courses, self).unlink()
