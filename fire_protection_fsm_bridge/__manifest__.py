# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'website': 'https://vertel.se/apps/odoo-fire-protection/fire_protection_fsm_bridge',
    'name': 'Fire Protection — FSM Bridge',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'summary': 'Koppling SBA-avvikelse → FSM-arbetsorder för brandtekniker',
    'description': '''
Fire Protection — FSM Bridge
============================

    Koppling SBA-avvikelse → FSM-arbetsorder för brandtekniker.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
        - Extends Odoo: Builds on fsm.order, mgmtsystem.nonconformity.
    ''',
    'category': 'Fire Protection',
    'depends': ['fire_protection_sba', 'mgmtsystem_nonconformity', 'fieldservice'],
    'data': [
        'security/ir.model.access.csv',
        'views/fire_protection_fsm_views.xml',
    ],
    'application': False,
    'installable': True,
}
