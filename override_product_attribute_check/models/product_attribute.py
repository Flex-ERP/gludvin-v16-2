from odoo import models, fields, api


class ProductTemplateAttributeLine(models.Model):
    _inherit = 'product.template.attribute.line'

    @api.constrains('active', 'value_ids', 'attribute_id')
    def _check_valid_values(self):
        return True
