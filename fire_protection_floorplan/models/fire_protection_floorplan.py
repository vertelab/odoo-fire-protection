# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FireProtectionFloorplan(models.Model):
    _name = "fire.protection.floorplan"
    _description = "Floor Plan with Hotspots"
    _order = "location_id, name"

    name = fields.Char(required=True)
    image = fields.Binary(
        string="Floor Plan Image",
        required=True,
        help="Upload a floor plan (PNG, JPG, or PDF)",
    )
    image_filename = fields.Char()
    location_id = fields.Many2one(
        "fsm.location",
        string="Location",
        required=True,
        index=True,
    )
    floor_number = fields.Char(string="Floor / Section")
    building_section = fields.Char(string="Building Section")

    hotspot_ids = fields.One2many(
        "fire.protection.hotspot",
        "floorplan_id",
        string="Hotspots",
    )
    hotspot_count = fields.Integer(
        compute="_compute_hotspot_count",
        string="Hotspot Count",
    )

    company_id = fields.Many2one(
        "res.company",
        related="location_id.company_id",
        store=True,
    )

    def _compute_hotspot_count(self):
        for rec in self:
            rec.hotspot_count = len(rec.hotspot_ids)


class FireProtectionHotspot(models.Model):
    _name = "fire.protection.hotspot"
    _description = "Clickable Hotspot on Floor Plan"
    _order = "floorplan_id, name"

    name = fields.Char(required=True)
    floorplan_id = fields.Many2one(
        "fire.protection.floorplan",
        string="Floor Plan",
        required=True,
        ondelete="cascade",
    )
    object_id = fields.Many2one(
        "fire.protection.object",
        string="Fire Object",
        help="Linked fire protection object",
    )
    x = fields.Float(
        string="X Position (%)",
        required=True,
        default=50.0,
        help="Horizontal position on the floor plan (0-100%)",
    )
    y = fields.Float(
        string="Y Position (%)",
        required=True,
        default=50.0,
        help="Vertical position on the floor plan (0-100%)",
    )
    width = fields.Integer(string="Width (px)", default=32)
    height = fields.Integer(string="Height (px)", default=32)
    status_color = fields.Selection(
        [
            ("green", "Green — OK"),
            ("yellow", "Yellow — Deficient"),
            ("red", "Red — Critical"),
            ("gray", "Gray — Unknown"),
        ],
        string="Status Color",
        compute="_compute_status_color",
    )
    last_checked_date = fields.Date(
        related="object_id.last_service_date",
        store=True,
    )

    company_id = fields.Many2one(
        "res.company",
        related="floorplan_id.company_id",
        store=True,
    )

    def _compute_status_color(self):
        for hotspot in self:
            if hotspot.object_id:
                if hotspot.object_id.status == "ok":
                    hotspot.status_color = "green"
                elif hotspot.object_id.status == "deficient":
                    hotspot.status_color = "yellow"
                elif hotspot.object_id.status == "critical":
                    hotspot.status_color = "red"
                else:
                    hotspot.status_color = "gray"
            else:
                hotspot.status_color = "gray"

    def action_open_object(self):
        """Open the linked fire protection object."""
        self.ensure_one()
        if self.object_id:
            return {
                "type": "ir.actions.act_window",
                "res_model": "fire.protection.object",
                "res_id": self.object_id.id,
                "view_mode": "form",
                "target": "current",
            }
