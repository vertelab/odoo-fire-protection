# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection AI — Risk Analysis',
    'version': '18.0.1.0.0',
    'summary': 'AI-driven riskanalys och prediktivt underhåll för brandskydd',
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
