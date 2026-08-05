# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection Law — Brandskyddslagstiftning',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': 'Förladdad brandskyddslagstiftning via mgmtsystem_law — LSO, LBE, AFS, BBR, SBF',
    'category': 'Fire Protection',
    'depends': ['fire_protection_base', 'mgmtsystem_law', 'document_law'],
    'data': [
        'security/ir.model.access.csv',
        'data/fire_law_data.xml',
    ],
    'application': False,
    'installable': True,
}
