# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class FireProtectionInspection(models.Model):
    _name = "fire.protection.inspection"
    _description = "SBA Inspection Round"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "date desc, name"

    name = fields.Char(required=True)
    date = fields.Date(required=True, default=fields.Date.context_today)
    inspector_id = fields.Many2one(
        "res.users",
        string="Inspector",
        default=lambda self: self.env.user,
    )
    location_id = fields.Many2one(
        "fsm.location",
        string="Location",
        required=True,
    )
    inspection_type = fields.Selection(
        [
            ("monthly", "Monthly Round"),
            ("quarterly", "Quarterly Round"),
            ("annual", "Annual Full Inspection"),
            ("special", "Special Inspection"),
        ],
        string="Inspection Type",
        default="monthly",
    )
    checklist_ids = fields.One2many(
        "fire.protection.checklist.item",
        "inspection_id",
        string="Checklist",
    )
    deficiencies_found = fields.Integer(
        string="Deficiencies Found",
        compute="_compute_deficiencies",
        store=True,
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        tracking=True,
    )
    notes = fields.Html(string="Notes")
    report = fields.Binary(string="Inspection Report (PDF)")
    report_filename = fields.Char()
    company_id = fields.Many2one(
        "res.company",
        related="location_id.company_id",
        store=True,
    )

    @api.depends("checklist_ids.is_deficient")
    def _compute_deficiencies(self):
        for rec in self:
            rec.deficiencies_found = len(
                rec.checklist_ids.filtered(lambda c: c.is_deficient)
            )

    def action_start(self):
        self.write({"state": "in_progress"})

    def action_complete(self):
        self.write({"state": "completed"})

    def action_cancel(self):
        self.write({"state": "cancelled"})

    def action_draft(self):
        self.write({"state": "draft"})

    def action_generate_checklist(self):
        """Generate checklist items from all objects at this location."""
        self.ensure_one()
        objects = self.env["fire.protection.object"].search([
            ("location_id", "=", self.location_id.id),
            ("active", "=", True),
        ])
        for obj in objects:
            self.env["fire.protection.checklist.item"].create({
                "inspection_id": self.id,
                "object_id": obj.id,
                "expected_status": "ok",
            })

    def action_generate_report(self):
        """Placeholder for PDF report generation."""
        self.ensure_one()
        pass
