# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'website': 'https://vertel.se/apps/odoo-fire-protection/fire_protection_competence',
    'name': 'Fire Protection Competence — Brandtekniker-certifieringar',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': 'Förladdade brandtekniker-kompetenser i hr_skills — SBF, HLR, Heta Arbeten',
    'description': '''
Fire Protection Competence — Brandtekniker-certifieringar
=========================================================

    Förladdade brandtekniker-kompetenser i hr_skills — SBF, HLR, Heta Arbeten.

    Features:

        - Demo Data: Ships pre-configured demo data for the industry.
    ''',
    'category': 'Fire Protection',
    'depends': ['fire_protection_base', 'mgmtsystem_hr_skills'],
    'data': [
        'security/ir.model.access.csv',
        'data/fire_competence_data.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
