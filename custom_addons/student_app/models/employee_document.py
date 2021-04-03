
from odoo import models, fields, api
import datetime
from odoo.exceptions import UserError, ValidationError


class EmployeeDcoument(models.Model):
    _name = "employee.document"

    status = [('draft', 'Draft'),
              ('approved', 'Approved'),
              ('expired', 'Expired'),
              ('refused', 'Refused')]

    name = fields.Char()
    file = fields.Binary()
    expiry_date = fields.Date(string="Expiry Date")
    employee_id = fields.Many2one("hr.employee")
    doc_filename = fields.Char(
        related="employee_id.name", string='Doc Filename')

    state = fields.Selection(status, default="draft")

    @api.onchange('expiry_date')
    def onchage_expiry(self):
        for rec in self:
            val1 = rec.expiry_date
            val2 = datetime.date.today()
            if val1 != False:
                if val1 >= val2:
                    rec.state = "expired"
                else:
                    rec.state = "draft"

    # @api.model
    # def create(self, vals):
    #     emp_id = vals["employee_id"]
    #     namess = self.env["hr.employee"].browse(
    #         [emp_id])
    #     print("\n\n\n\n\n\n", vals)
    #     vals["doc_filename"] = namess.name
    #     return super(EmployeeDcoument, self).create(vals)

    def approve_action(self):
        self.state = "approved"

    def refuse_action(self):
        self.state = "refused"


class HrDocumentUpdate(models.Model):
    _inherit = 'hr.employee'

    doc_counts = fields.Integer(string="total", compute="count_rec")

    def count_rec(self):
        print("\n\n\n\n\n\n\n")
        for rec in self:
            var = self.env["employee.document"].search_count(
                [('employee_id', '=', rec.id)])
            rec.doc_counts = var

    def Emp_Doc_View(self):
        self.ensure_one()
        for rec in self:
            return{
                'type': 'ir.actions.act_window',
                'name': 'employee document',
                'view_mode': 'tree,form',
                'res_model': 'employee.document',
                'domain': [('employee_id', '=', rec.id)],
            }
