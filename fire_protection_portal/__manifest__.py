# Copyright (C) 2025 Vertel Sverige AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'website': 'https://vertel.se/apps/odoo-fire-protection/fire_protection_portal',
    'name': 'Fire Protection Portal — Kundportal för SBA',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': "Customer portal for fire protection documentation (SBA).",
    'description': '''
Fire Protection Portal — Kundportal för SBA
===========================================

    Customer portal for fire protection documentation (SBA).

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
    ''',
    'category': 'Fire Protection',
    'depends': ['fire_protection_base', 'fire_protection_floorplan', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/portal_templates.xml',
    ],
    'application': False,
    'installable': True,
}
