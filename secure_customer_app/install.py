import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def after_install():
    create_domain_list()
    execute()

def create_domain_list():
    if not frappe.db.exists("Domain", "Dynamic"):
        dm1 = frappe.new_doc("Domain")
        dm1.domain = 'Dynamic'
        dm1.insert()

def execute():
    custom_field = {
        'fieldname': 'custom_token',
        'label': 'Custom Token',
        'fieldtype': 'Small Text',
        'insert_after': 'territory',
    }

    create_custom_field('Customer', custom_field)
