# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_disclaimer = fields.Html(
        string='Invoice Disclaimer',
        compute='_compute_invoice_disclaimer',
        store=False,
        help="Disclaimer text from customer configuration"
    )

    @api.depends('partner_id', 'partner_id.invoice_disclaimer_id')
    def _compute_invoice_disclaimer(self):
        """Compute disclaimer based on customer's disclaimer setting"""
        for move in self:
            disclaimer = ''
            if (move.partner_id and 
                move.partner_id.invoice_disclaimer_id and 
                move.partner_id.invoice_disclaimer_id.active):
                disclaimer = move.partner_id.invoice_disclaimer_id.content
            move.invoice_disclaimer = disclaimer

    def _get_invoice_disclaimer(self):
        """Helper method to get disclaimer for use in reports"""
        return self.invoice_disclaimer or ''
