from odoo import models, fields


class SaleOrderUpdate(models.Model):

    _inherit = 'sale.order'

    quatation_ready = fields.Boolean()
    is_sell = fields.Selection(
        [('sale', '💼'), ('panding', '🧑‍💼')])
