# -*- coding: utf-8 -*-


from odoo import models,fields,api


class ProductBrand(models.Model):
	_inherit = 'product.template'

	brand_id = fields.Many2one('product.brand',string='Brand')


class BrandProduct(models.Model):
	_name = 'product.brand'


	name= fields.Char(String="Name")
	name_arabic = fields.Char(String="Arabic Name")
	brand_image = fields.Binary()
	member_ids = fields.One2many('product.template', 'brand_id')
	product_count = fields.Char(String='Product Count', compute='get_count_products', store=True)
	bg_color_code = fields.Char(string="Bg Color Code")
	text_color = fields.Selection([('text-dark', 'text-dark'),('text-white','text-white')],"Text Color Code")
	top_brand = fields.Boolean()

	@api.depends('member_ids')
	def get_count_products(self):
		for rec in self:
			rec.product_count = len(rec.member_ids)


class BrandReportStock(models.Model):
	_inherit = 'stock.quant'

	brand_id  = fields.Many2one(related='product_id.brand_id',
		string='Brand', store=True, readonly=True)


