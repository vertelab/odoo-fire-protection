# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'website': 'https://vertel.se/apps/odoo-fire-protection/fire_protection_ai',
    'name': 'Fire Protection AI — Risk Analysis',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': "Adds AI-assisted risk analysis for fire protection.",
    'description': '''
Fire Protection AI — Risk Analysis
==================================

    Adds AI-assisted risk analysis for fire protection.

    Features:

        - Automation: Scheduled jobs: Fire Protection: AI Risk Assessment (Nightly).
    ''',
    'category': 'Fire Protection',
    'depends': ['fire_protection_sba', 'ai_agent_core'],
    'data': [
        'security/ir.model.access.csv',
        'data/ai_coworker_data.xml',
        'data/cron.xml',
    ],
    'application': False,
    'installable': True,
}
