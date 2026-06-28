# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Fire Protection Base',
    'version': '18.0.1.0.0',
    'summary': 'Brandskydd — objektregister, livscykel, QR-koder',
    'category': 'Fire Protection',
    'description': """
        Kärnmodul för brandskyddshantering i Odoo.

        Implementerar:
        - Brandskyddsobjekt (brandsläckare, brandlarm, branddörrar, etc.)
        - Livscykelhantering med serviceintervall (5-årsöversyn, 10-årsomlastning)
        - QR-koder för varje objekt
        - Utökning av fsm.location med brandskyddsfält
        - Koppling till OCA Field Service och Odoo Maintenance

        Bygger på OCA fieldservice och Odoo maintenance.
    """,
    'author': 'Vertel AB',
    'website': 'https://vertel.se',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'mail',
        'fieldservice',
        'maintenance',
        'product',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/fire_protection_object_views.xml',
        'views/fire_protection_location_views.xml',
        'views/fire_protection_menu.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
}
