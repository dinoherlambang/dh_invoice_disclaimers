{
    'name': 'Invoice Disclaimer Management',
    'version': '13.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Manage customer-specific disclaimers on invoices',
    'description': """
Invoice Disclaimer Management
=============================

This module allows you to:
* Assign specific disclaimers to customers
* Display disclaimers in invoice footers
* Manage disclaimers through a dedicated interface

Features:
---------
* Customer-specific disclaimer assignment
* Invoice footer disclaimer display
* Easy disclaimer management

Guidance & Usage:
-----------------
1. Go to Accounting > Configuration > Invoice Disclaimers > Invoice Disclaimers to create and manage disclaimers.
2. Assign a disclaimer to a customer by editing the customer record (Contacts > Customer > Invoice Settings tab > Invoice Disclaimer).
3. The selected disclaimer will automatically appear in the footer of that customer's invoices.

Tips:
- You can use HTML formatting in the disclaimer content.
- Disclaimers can be company-specific in multi-company environments.
- You can assign or change disclaimers for customers at any time.

For more details, see the README file included with this module.
    """,
    'author': 'Dino Herlambang',
    'depends': [
        'base',
        'account',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/disclaimer_views.xml',
        'views/res_partner_views.xml',
        'views/account_move_views.xml',
        'reports/invoice_report.xml',
        'data/disclaimer_data.xml',
    ],
    'demo': [
        'demo/disclaimer_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
