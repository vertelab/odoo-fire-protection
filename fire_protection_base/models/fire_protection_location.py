# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FsmLocation(models.Model):
    _inherit = "fsm.location"

    fire_safety_rating = fields.Selection(
        [
            ("A", "A — Excellent"),
            ("B", "B — Good"),
            ("C", "C — Needs Improvement"),
            ("D", "D — Critical"),
            ("unknown", "Unknown"),
        ],
        string="Fire Safety Rating",
        default="unknown",
    )
    fire_protection_object_ids = fields.One2many(
        "fire.protection.object",
        "location_id",
        string="Fire Protection Objects",
    )
    fire_object_count = fields.Integer(
        string="Object Count",
        compute="_compute_fire_object_count",
    )
    floorplan_ids = fields.One2many(
        "fire.protection.floorplan",
        "location_id",
        string="Floor Plans",
    )
    fire_last_inspection_date = fields.Date(string="Last Inspection")
    fire_next_inspection_date = fields.Date(string="Next Inspection Due")
    fire_responsible_person_id = fields.Many2one(
        "res.users",
        string="Fire Safety Responsible",
    )
    fire_deficiencies_count = fields.Integer(
        string="Open Deficiencies",
        compute="_compute_fire_deficiencies",
    )

    def _compute_fire_object_count(self):
        for loc in self:
            loc.fire_object_count = len(loc.fire_protection_object_ids)

    def _compute_fire_deficiencies(self):
        for loc in self:
            loc.fire_deficiencies_count = len(
                loc.fire_protection_object_ids.filtered(
                    lambda o: o.status in ("deficient", "critical")
                )
            )
