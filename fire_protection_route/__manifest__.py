# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection Route — Ruttoptimering för brandtekniker',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': 'Optimerad ruttplanering för brandtekniker baserat på geografisk position och SLA',
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
