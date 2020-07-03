# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from odoo import api, models, fields
from odoo.exceptions import Warning

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.one
    def action_generate_sale_order_link_tracker(self):
        return super(SaleOrder, self).action_generate_sale_order_link_tracker()

    @api.one
    def action_send_sms_automatic(self, sms_template_id=False, need_check_date_order_send_sms=True):
        #action_generate_sale_order_link_tracker
        self.action_generate_sale_order_link_tracker()
        #action_send_sms_automatic
        return super(SaleOrder, self).action_send_sms_automatic(sms_template_id, need_check_date_order_send_sms)

    @api.multi
    def action_send_sms(self):
        #action_generate_sale_order_link_tracker
        for item in self:
            item.action_generate_sale_order_link_tracker()
        #action_send_sms
        return super(SaleOrder, self).action_send_sms()