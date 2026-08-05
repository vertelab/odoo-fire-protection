# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection Portal — Kundportal för SBA',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': 'White label kundportal för brandskydd — kunder ser sina fastigheter, ritningar och status',
    'category': 'Fire Protection',
    'depends': ['fire_protection_base', 'fire_protection_floorplan', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/portal_templates.xml',
    ],
    'application': False,
    'installable': True,
}
