# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InvoiceDisclaimer(models.Model):
    _name = 'invoice.disclaimer'
    _description = 'Invoice Disclaimer'
    _order = 'name'

    name = fields.Char(
        string='Disclaimer Name',
        required=True,
        help="Name to identify this disclaimer"
    )
    
    content = fields.Html(
        string='Disclaimer Content',
        required=True,
        help="The disclaimer text that will appear on invoices"
    )
    
    active = fields.Boolean(
        string='Active',
        default=True,
        help="Uncheck to hide this disclaimer from selection"
    )
    
    partner_ids = fields.One2many(
        'res.partner',
        'invoice_disclaimer_id',
        string='Customers',
        help="Customers using this disclaimer"
    )
    
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        help="Company this disclaimer belongs to"
    )

    # Computed fields for partner display
    partner_count = fields.Integer(
        string='Customer Count',
        compute='_compute_partner_count',
        help="Number of customers using this disclaimer"
    )

    @api.depends('partner_ids')
    def _compute_partner_count(self):
        """Compute the number of customers using this disclaimer"""
        for record in self:
            record.partner_count = len(record.partner_ids)

    @api.model
    def create(self, vals):
        """Override create to ensure company_id is set"""
        if not vals.get('company_id'):
            vals['company_id'] = self.env.company.id
        return super(InvoiceDisclaimer, self).create(vals)

    def name_get(self):
        """Custom name_get to show disclaimer name only"""
        result = []
        for record in self:
            result.append((record.id, record.name))
        return result
