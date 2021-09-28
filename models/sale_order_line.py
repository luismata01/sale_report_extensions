from odoo import fields, models

class SaleOrderLine(models.Model):
     _inherit = "sale.order.line"
     #_brand_id = fields.Char('X Field')
     
     #brand_id = fields.Many2one(
     #    'product.brand',string='Brand')
     
     _brand_id = fields.Many2one(
        'product.brand',
        string='Marca', related='product_template_id.brand_id',
        readonly=True)

# wdb.set_trace()