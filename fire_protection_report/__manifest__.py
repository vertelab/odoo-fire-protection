# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection Report — Tillsynsredo',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': 'Exportera kompletta tillsynsunderlag för Räddningstjänsten',
    'category': 'Fire Protection',
    'depends': ['fire_protection_sba', 'mgmtsystem_nonconformity'],
    'data': [
        'security/ir.model.access.csv',
        'data/report_templates.xml',
    ],
    'application': False,
    'installable': True,
}
