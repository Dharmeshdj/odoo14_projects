from odoo import models, fields
from datetime import date


class StudentWizard(models.TransientModel):
    _name = "student.wizard"
    _description = "this is student wizard model"

    reason = fields.Char(max_length=30)

    def submit_wizard(self):
        print(f'\n\n\n\n submit wizard \n\n\n\n')
        for rec in self:
            if self.reason:
                dt = self.env["student.data.lines"].browse(
                    self._context.get("active_id"))
                print(
                    f'\n\n\n\n{dt.course_name}\n\n\n\n')
                dt.write(
                    {'cancel_reason': self.reason})

                # self.student_line_ids.cancel_reason = self.reason

                # rec.student_line_ids.cancel_reason = rec.reason
