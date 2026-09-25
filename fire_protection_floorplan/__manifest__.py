# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'website': 'https://vertel.se/apps/odoo-fire-protection/fire_protection_floorplan',
    'name': 'Fire Protection Floor Plan',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': "Adds floor plans with fire protection equipment markers.",
    'description': '''
Fire Protection Floor Plan
==========================

    Adds floor plans with fire protection equipment markers.

    Features:

        - UI Integration: Extends 2 view(s) in the Odoo interface.
        - Extends Odoo: Builds on fire.protection.floorplan, fire.protection.hotspot.
    ''',
    'category': 'Fire Protection',
    'depends': ['fire_protection_base'],
    'data': [
        'security/ir.model.access.csv',
        'views/fire_protection_floorplan_views.xml',
        'views/fire_protection_menu.xml',
    ],
    'application': False,
    'installable': True,
}
