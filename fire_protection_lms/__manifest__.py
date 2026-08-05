# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection LMS — SBA-utbildningar med diagnostiska prov',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': 'Brandskyddsutbildningar via website_slides — SBA, brandskyddskontroll, HLR, Heta Arbeten',
    'category': 'Fire Protection',
    'depends': ['fire_protection_base', 'website_slides'],
    'data': [
        'security/ir.model.access.csv',
        'data/slide_channel_data.xml',
        'data/slide_quiz_data.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
