# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'website': 'https://vertel.se/apps/odoo-fire-protection/fire_protection_route',
    'name': 'Fire Protection Route — Ruttoptimering för brandtekniker',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': "Adds evacuation routes to fire protection plans.",
    'description': '''
Fire Protection Route — Ruttoptimering för brandtekniker
========================================================

    Adds evacuation routes to fire protection plans.

    Features:

        - UI Integration: Extends 2 view(s) in the Odoo interface.
        - Extends Odoo: Builds on fsm.order.
    ''',
    'category': 'Fire Protection',
    'depends': ['fire_protection_base', 'fieldservice', 'web_map_ce'],
    'data': [
        'security/ir.model.access.csv',
        'views/fire_protection_route_views.xml',
        'views/fire_protection_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'fire_protection_route/static/src/**/*',
        ],
    },
    'application': False,
    'installable': True,
}
