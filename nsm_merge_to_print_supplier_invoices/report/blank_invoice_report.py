# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2015 Odoo Experts
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from report import report_sxw


class blank_invoice_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context=None):
        super(blank_invoice_report, self).__init__(cr, uid, name,
                                                   context=context)
        self.localcontext.update({'time': time})
        self.context = context


report_sxw.report_sxw('report.blank.invoice.report',
                      'account.invoice',
                      'addons/nsm_merge_to_print_supplier_invoices/report/blank_invoice_report.rml',
                      parser=blank_invoice_report, header=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
