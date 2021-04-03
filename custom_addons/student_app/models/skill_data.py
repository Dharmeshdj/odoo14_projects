from odoo import models, fields


class HobbySkills(models.Model):
    _name = "student.skill"

    name = fields.Char(string="Hobby")
    award = fields.Char(string="award")
    colors = fields.Integer()
    # def name_get(self):
    #     result = []
    #     print("check")
    #     for field in self:

    #         result.append((field.id, " %s %s " %
    #                        (field.course_id.course_length, field.professor_name)))
    #     print(f'\n\ncheck forloop dharmesh  {result} \n\n')
    #     return result
