# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FsmOrder(models.Model):
    _inherit = "fsm.order"

    partner_id = fields.Many2one(
        "res.partner",
        string="Partner",
        related="location_id.partner_id",
        store=True,
        help="Customer associated with this order's location. Used for map geolocation.",
    )
    routing_sequence = fields.Integer(
        string="Route Stop #",
        default=0,
        help="Sequence number for route planning. 0 = not yet sequenced.",
    )
    estimated_arrival = fields.Datetime(
        string="ETA",
        help="Estimated time of arrival at this stop",
    )
    travel_time_minutes = fields.Integer(
        string="Travel Time (min)",
        help="Estimated travel time from previous stop",
    )
