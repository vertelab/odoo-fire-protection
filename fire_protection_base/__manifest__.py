# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection Base',
    'version': '18.0.1.0.0',
    'summary': 'Brandskydd — objektregister, livscykel, QR-koder.',
    'category': 'Fire Protection',
    'description': '''
Fire Protection Base
====================

    Core module for fire protection management in Odoo.

Implements:

    - Fire protection objects (extinguishers, alarms, fire doors, etc.)
    - Life cycle management with service intervals (5-year review, etc.)
    - Inspection and service history.
    ''',
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-fire-protection/fire_protection_base',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'mail',
        'fieldservice',
        'maintenance',
        'product',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/fire_protection_object_views.xml',
        'views/fire_protection_location_views.xml',
        'views/fire_protection_menu.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
}
