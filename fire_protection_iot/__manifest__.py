# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection IoT — Sensorbrygga',
    'version': '18.0.1.0.0',
    'summary': 'IoT-integration för brandlarmspaneler och sensorer',
    'category': 'Fire Protection',
    'depends': ['fire_protection_base'],
    'data': [
        'security/ir.model.access.csv',
        'views/fire_protection_iot_views.xml',
    ],
    'application': False,
    'installable': True,
}
