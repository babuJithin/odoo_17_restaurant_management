# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import itertools
from datetime import datetime, date, timedelta
import time
import random
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)
import uuid
import re




class CustomGuestSession(models.Model):
    _name = 'guest.session'
    _description = 'Guest Session'

    session_id = fields.Char(string="Session ID")

class ResPartner(models.Model):
    _inherit= 'res.partner'

    company_name_ecom = fields.Char(string="Company Name")
    gst_vat = fields.Char(string="Gst vat")
    guest_user_id = fields.Integer(String="Guest USER id")


class ResUsers(models.Model):
    _inherit = 'res.users'



    @api.model
    def get_res_user_public(self):
        public_user = self.env.ref('base.public_user')
        if public_user:
            return public_user
        else:
            return False



    def create_temp_res_user(self):

        chrs = 'ABCDEFHIJITYDSNCJSUJDBSIBDSJSNOAHaskjdssoibdiusbabcdef0123456789'  # Change your required characters here
        n = 12  # Change your word length here
        random_key = (''.join(random.choices(chrs, k=15)))
        name= random_key or ''
        email = random_key+"@gmail.com" or ''
        phone = random_key or ''
        portal = self.env['res.users'].sudo().create(
         {'login': email, 'name': name,'is_guest_user':True,
          'login_mobile': phone,
          'sel_groups_1_9_10': 9})
        return portal



