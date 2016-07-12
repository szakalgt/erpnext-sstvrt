# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def execute():
	frappe.reload_doc('projects', 'doctype','time_sheet')
	frappe.reload_doc('projects', 'doctype', 'time_sheet_detail')
	frappe.reload_doc('accounts', 'doctype', 'sales_invoice_timesheet')
	
	make_property_setter('Time Sheet', "naming_series", "options", 'TS-', "Text")
	make_property_setter('Time Sheet', "naming_series", "default", 'TS-', "Text")