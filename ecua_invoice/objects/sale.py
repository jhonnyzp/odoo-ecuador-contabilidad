# -*- encoding: utf-8 -*-
########################################################################
#
# @authors: Santiago Orozco, TRESCloud Cia Ltda.
# Copyright (C) 2013  TRESCloud Cia Ltda
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
# This module is GPLv3 or newer and incompatible
# with OpenERP SA "AGPL + Private Use License"!
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see http://www.gnu.org/licenses.
########################################################################

from osv import fields, osv
import time
from tools import config
from tools.translate import _

class sale_order(osv.osv):
    _inherit = 'sale.order'
    _name = 'sale.order'
        
    def _get_default_shop(self, cr, uid, context=None):
        '''
        Obtendremos la tienda asociada al usuario a traves del punto de impresion atado al usuario y a la 
        tienda asociada a dicho punto.
        La funcion base no nos sirve para este proposito ya que solo retorna la primera tienda de acuerdo 
        a la compania que esta atada al usuario.
        '''
        user_obj = self.pool.get('res.users')
        user = user_obj.browse(cr, uid, uid, context)
        if user.printer_id:
            if user.printer_id.shop_id:
                return user.printer_id.shop_id.id
        return super(sale_order, self)._get_default_shop(cr, uid, context)

    def _prepare_invoice(self, cr, uid, order, lines, context=None):
        """
        Prepares the invoice, but ensures the current date as default.
        """
        context = context or {}
        context.update({
            'date_invoice': time.strftime('%Y-%m-%d')
        })
        return super(sale_order, self)._prepare_invoice(cr, uid, order, lines, context)

    _defaults = {
        'shop_id': _get_default_shop,
    }
sale_order()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: