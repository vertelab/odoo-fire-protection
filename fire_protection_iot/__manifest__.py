# Copyright (C) 2025 Vertel Sverige AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'website': 'https://vertel.se/apps/odoo-fire-protection/fire_protection_iot',
    'name': 'Fire Protection IoT — Sensorbrygga',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': "Connects IoT sensors to fire protection monitoring.",
    'description': '''
Fire Protection IoT — Sensorbrygga
==================================

    Connects IoT sensors to fire protection monitoring.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
    ''',
    'category': 'Fire Protection',
    'depends': ['fire_protection_base'],
    'data': [
        'security/ir.model.access.csv',
        'views/fire_protection_iot_views.xml',
    ],
    'application': False,
    'installable': True,
}
