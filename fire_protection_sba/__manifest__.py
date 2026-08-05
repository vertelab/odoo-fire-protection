# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection SBA — Systematiskt Brandskyddsarbete',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': 'Ronderingsmallar, checklistor, egenkontroll för brandskydd',
    'category': 'Fire Protection',
    'depends': ['fire_protection_base', 'fire_protection_floorplan'],
    'data': [
        'security/ir.model.access.csv',
        'views/fire_protection_inspection_views.xml',
        'views/fire_protection_checklist_views.xml',
        'views/fire_protection_menu.xml',
    ],
    'application': False,
    'installable': True,
}
