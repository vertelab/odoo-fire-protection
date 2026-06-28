# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class FireProtectionChecklistItem(models.Model):
    _name = "fire.protection.checklist.item"
    _description = "Inspection Checklist Item"
    _order = "inspection_id, object_id"

    inspection_id = fields.Many2one(
        "fire.protection.inspection",
        string="Inspection",
        required=True,
        ondelete="cascade",
    )
    object_id = fields.Many2one(
        "fire.protection.object",
        string="Fire Object",
        required=True,
    )
    expected_status = fields.Selection(
        [
            ("ok", "OK"),
            ("deficient", "Deficient"),
        ],
        string="Expected",
        default="ok",
    )
    actual_status = fields.Selection(
        [
            ("ok", "OK"),
            ("deficient", "Deficient"),
            ("critical", "Critical"),
            ("not_found", "Not Found"),
            ("skipped", "Skipped"),
        ],
        string="Actual",
        default="ok",
    )
    photo = fields.Binary(string="Photo")
    photo_filename = fields.Char()
    comment = fields.Text(string="Comment")
    is_deficient = fields.Boolean(
        string="Is Deficient?",
        compute="_compute_is_deficient",
        store=True,
    )
    company_id = fields.Many2one(
        "res.company",
        related="inspection_id.company_id",
        store=True,
    )

    @api.depends("actual_status")
    def _compute_is_deficient(self):
        for item in self:
            item.is_deficient = item.actual_status in ("deficient", "critical", "not_found")

    def action_mark_ok(self):
        self.write({"actual_status": "ok"})

    def action_mark_deficient(self):
        self.write({"actual_status": "deficient"})

    def action_mark_critical(self):
        self.write({"actual_status": "critical"})

    def action_mark_not_found(self):
        self.write({"actual_status": "not_found"})

    def action_create_deficiency(self):
        """Create a nonconformity from this checklist deficiency."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "mgmtsystem.nonconformity",
            "view_mode": "form",
            "context": {
                "default_name": f"Brandskyddsbrist: {self.object_id.display_name}",
                "default_description": self.comment or f"Brist hittad vid SBA-rondering {self.inspection_id.name}",
                "default_origin": f"fire.protection.checklist.item,{self.id}",
            },
            "target": "current",
        }
