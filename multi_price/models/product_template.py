from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    list_price = fields.Float(company_dependent = True)