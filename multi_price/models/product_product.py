from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    lst_price = fields.Float(company_dependent = True)