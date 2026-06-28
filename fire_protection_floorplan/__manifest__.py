# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection Floor Plan',
    'version': '18.0.1.0.0',
    'summary': 'Digitala ritningar med klickbara hotspots för brandskydd',
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
