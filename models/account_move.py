from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    origin_id = fields.Many2one(
        comodel_name="sale.order",
        compute="_get_sale_order_origin",
        store=True,
    )
    po = fields.Char(
        related="origin_id.po",
        store=True,
    )

    @api.depends("invoice_origin")
    def _get_sale_order_origin(self):
        for r in self:
            origin_sale_order = self.env["sale.order"].search(
                [("name", "=", r.invoice_origin)], limit=1
            )
            r.origin_id = origin_sale_order.id
