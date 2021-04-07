from odoo import models, fields
from datetime import date


class StudentWizard(models.TransientModel):
    _name = "student.wizard"
    _description = "this is student wizard model"

    reason = fields.Char(max_length=30)

    def submit_wizard(self):
        print(f'\n\n submit wizard \n\n')
        for rec in self:

            if self.reason:
                dt = self.env["student.data.lines"].browse(
                    self._context.get("active_id"))  # access current cancel record
                print(f'\n\n\asdhjgashjdgasdhjghjasdn\n{dt.stu_id}\n\n\n')

                dt.write(
                    {'cancel_reason': self.reason,
                     'course_cancel': False,
                     })
                select_courses = self.env["student.data.lines"].search_count(
                    [('course_cancel', '=', True), ('stu_id', '=', dt.stu_id.id)])
                print(
                    f'\n\n\n\nselected course  ={select_courses}\n\n\n')

                if select_courses <= 0:
                    print(f'\n\n\n\n{dt.stu_id.state}\n\n\n')
                    dt.stu_id.state = 'cancel'

                # if self.reason:
                #     dt = self.env["student.data.lines"].browse(
                #         self._context.get("active_id"))  # access current cancel record
                #     # print(
                #     #     f'\n\n\n\n{self._context.get("active_id")}\n{dt.course_name}\n\n\n')
                #     dt.write(
                #         {'cancel_reason': self.reason,
                #          'course_cancel': False,
                #          })

                #     # self.student_line_ids.cancel_reason = self.reason

                #     # rec.student_line_ids.cancel_reason = rec.reason
