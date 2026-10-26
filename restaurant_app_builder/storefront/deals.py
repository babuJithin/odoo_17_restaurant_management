# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import itertools
from datetime import datetime, date, timedelta

from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class MobileDealelemt(models.Model):
    _name = 'deal.element'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name',required=True,default=lambda self: _('New'))

    color= fields.Char('Color',track_visibility='always')
    sequence = fields.Integer('Sequence',required=True,default=1)
    active = fields.Boolean(default=True)
    image = fields.Binary('Image', attachment=True,store=True)
    categ_ids = fields.Many2many('product.public.category',string="Category", track_visibility='always',limit=10)
    product_ids = fields.Many2many('product.template',string="Products", track_visibility='always',limit=10)


    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('deal.element') or _('New')
        return super(MobileDealelemt, self).create(vals)

    @api.onchange("product_ids")
    @api.depends("product_ids")
    def set_domain_for_categ_id(self):
        categ_ids=self.env["product.public.category"].search([('product_tmpl_ids', 'in', self.product_ids.ids)])
        self.categ_ids=categ_ids








