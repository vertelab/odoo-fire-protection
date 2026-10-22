# Copyright (C) 2025 Vertel Sverige AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MgmtsystemNonconformity(models.Model):
    _inherit = "mgmtsystem.nonconformity"

    fire_protection_object_id = fields.Many2one(
        "fire.protection.object",
        string="Fire Protection Object",
        index=True,
    )
    fsm_order_id = fields.Many2one(
        "fieldservice.order",
        string="Field Service Order",
        help="Linked FSM work order for the technician",
    )

    def action_create_fsm_order(self):
        """Create an FSM order from this nonconformity for a technician to fix."""
        self.ensure_one()
        partner = self.fire_protection_object_id.location_id
        order = self.env["fieldservice.order"].create({
            "name": f"Åtgärda brandskyddsbrist: {self.name}",
            "partner_id": partner.id,
            "description": self.description or "",
            "origin": f"mgmtsystem.nonconformity,{self.id}",
            "priority": "2" if self.severity == "critical" else "1",
        })
        self.fsm_order_id = order.id
        return {
            "type": "ir.actions.act_window",
            "res_model": "fieldservice.order",
            "res_id": order.id,
            "view_mode": "form",
            "target": "current",
        }


class FsmOrder(models.Model):
    _inherit = "fieldservice.order"

    fire_deficiency_id = fields.Many2one(
        "fire.protection.checklist.item",
        string="SBA Deficiency",
        help="Linked SBA checklist deficiency that triggered this order",
    )
    fire_protection_object_id = fields.Many2one(
        "fire.protection.object",
        string="Fire Object",
        help="Fire protection object to service",
    )
