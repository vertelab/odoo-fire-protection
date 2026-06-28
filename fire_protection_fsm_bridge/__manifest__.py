# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection — FSM Bridge',
    'version': '18.0.1.0.0',
    'summary': 'Koppling SBA-avvikelse → FSM-arbetsorder för brandtekniker',
    'category': 'Fire Protection',
    'depends': ['fire_protection_sba', 'mgmtsystem_nonconformity', 'fieldservice'],
    'data': [
        'security/ir.model.access.csv',
        'views/fire_protection_fsm_views.xml',
    ],
    'application': False,
    'installable': True,
}
