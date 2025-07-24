# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    invoice_disclaimer_id = fields.Many2one(
        'invoice.disclaimer',
        string='Invoice Disclaimer',
        help="Disclaimer to display on invoices for this customer",
        domain="[('active', '=', True), ('company_id', 'in', [company_id, False])]"
    )

    @api.onchange('company_id')
    def _onchange_company_id(self):
        """Clear disclaimer if company changes and disclaimer doesn't belong to new company"""
        if self.invoice_disclaimer_id and self.company_id:
            if (self.invoice_disclaimer_id.company_id and 
                self.invoice_disclaimer_id.company_id != self.company_id):
                self.invoice_disclaimer_id = False
