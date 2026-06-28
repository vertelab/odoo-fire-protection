# Copyright (C) 2025 Vertel AB (<https://vertel.se>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64
import io
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

try:
    import qrcode
except ImportError:
    _logger.warning("qrcode not installed. QR code generation disabled.")
    qrcode = None


class FireProtectionObject(models.Model):
    _name = "fire.protection.object"
    _description = "Fire Protection Object"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "location_id, object_type, name"
    _rec_name = "display_name"

    name = fields.Char(required=True, translate=True)
    display_name = fields.Char(compute="_compute_display_name", store=True)
    unique_id = fields.Char(
        string="Unique ID",
        required=True,
        copy=False,
        default=lambda self: self._generate_unique_id(),
        help="QR code / barcode identifier",
    )
    object_type = fields.Selection(
        [
            ("extinguisher", "Brandsläckare"),
            ("alarm", "Brandlarm"),
            ("door", "Branddörr"),
            ("sprinkler", "Sprinkler"),
            ("lighting", "Nödbelysning"),
            ("sign", "Skylt / Utrymningsväg"),
            ("hose", "Brandpost / Slangvinda"),
            ("blanket", "Brandfilt"),
            ("gas", "Gasdetektor"),
            ("other", "Övrigt"),
        ],
        string="Object Type",
        required=True,
        default="extinguisher",
    )
    location_id = fields.Many2one(
        "fsm.location",
        string="Location",
        required=True,
        index=True,
        ondelete="cascade",
    )
    floorplan_id = fields.Many2one(
        "fire.protection.floorplan",
        string="Floor Plan",
    )
    hotspot_x = fields.Float(string="X Position (%)")
    hotspot_y = fields.Float(string="Y Position (%)")

    # Lifecycle fields
    manufacture_date = fields.Date(string="Manufacture Date")
    install_date = fields.Date(string="Install Date")
    last_service_date = fields.Date(string="Last Service")
    next_service_date = fields.Date(string="Next Service Due")
    next_replacement_date = fields.Date(string="Next Replacement Due")
    service_interval_months = fields.Integer(
        string="Service Interval (months)",
        default=12,
    )
    replacement_5year_date = fields.Date(
        string="5-Year Overhaul Due",
        compute="_compute_lifecycle_dates",
        store=True,
    )
    replacement_10year_date = fields.Date(
        string="10-Year Reload/Replace Due",
        compute="_compute_lifecycle_dates",
        store=True,
    )
    replacement_20year_date = fields.Date(
        string="20-Year Scrap Date",
        compute="_compute_lifecycle_dates",
        store=True,
    )
    lifecycle_stage = fields.Selection(
        [
            ("active", "Active"),
            ("due_service", "Service Due"),
            ("due_overhaul", "Overhaul Due"),
            ("due_replacement", "Replacement Due"),
            ("overdue", "Overdue"),
            ("retired", "Retired"),
        ],
        string="Lifecycle Stage",
        compute="_compute_lifecycle_stage",
        store=True,
    )
    status = fields.Selection(
        [
            ("ok", "OK"),
            ("deficient", "Deficient"),
            ("critical", "Critical"),
            ("unknown", "Unknown"),
        ],
        string="Status",
        default="unknown",
        tracking=True,
    )

    # QR Code
    qr_code = fields.Binary(
        string="QR Code",
        compute="_compute_qr_code",
        store=True,
        attachment=True,
    )
    qr_code_filename = fields.Char(default="qr_code.png")

    # Relations
    maintenance_equipment_id = fields.Many2one(
        "maintenance.equipment",
        string="Maintenance Equipment",
        help="Linked Odoo maintenance equipment",
    )
    product_id = fields.Many2one(
        "product.product",
        string="Product",
    )
    company_id = fields.Many2one(
        "res.company",
        default=lambda self: self.env.company,
        required=True,
    )
    active = fields.Boolean(default=True)

    _sql_constraints = [
        (
            "unique_id_uniq",
            "unique(unique_id)",
            "Unique ID must be unique!",
        ),
    ]

    @api.depends("name", "unique_id", "object_type")
    def _compute_display_name(self):
        for rec in self:
            type_label = dict(self._fields["object_type"].selection).get(
                rec.object_type, rec.object_type
            )
            rec.display_name = f"[{rec.unique_id}] {type_label} — {rec.name}"

    @api.depends("manufacture_date")
    def _compute_lifecycle_dates(self):
        for rec in self:
            if rec.manufacture_date:
                mfg = rec.manufacture_date
                rec.replacement_5year_date = mfg.replace(year=mfg.year + 5)
                rec.replacement_10year_date = mfg.replace(year=mfg.year + 10)
                rec.replacement_20year_date = mfg.replace(year=mfg.year + 20)
            else:
                rec.replacement_5year_date = False
                rec.replacement_10year_date = False
                rec.replacement_20year_date = False

    @api.depends(
        "next_service_date",
        "replacement_5year_date",
        "replacement_10year_date",
        "status",
        "active",
    )
    def _compute_lifecycle_stage(self):
        today = fields.Date.today()
        for rec in self:
            if not rec.active:
                rec.lifecycle_stage = "retired"
            elif rec.status == "critical":
                rec.lifecycle_stage = "overdue"
            elif rec.next_replacement_date and rec.next_replacement_date <= today:
                rec.lifecycle_stage = "due_replacement"
            elif rec.replacement_5year_date and rec.replacement_5year_date <= today:
                rec.lifecycle_stage = "due_overhaul"
            elif rec.next_service_date and rec.next_service_date <= today:
                rec.lifecycle_stage = "due_service"
            elif rec.next_service_date and (rec.next_service_date - today).days <= 30:
                rec.lifecycle_stage = "due_service"
            else:
                rec.lifecycle_stage = "active"

    @api.depends("unique_id")
    def _compute_qr_code(self):
        if qrcode is None:
            return
        for rec in self:
            if rec.unique_id:
                qr = qrcode.QRCode(version=1, box_size=10, border=4)
                qr.add_data(rec.unique_id)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                buf = io.BytesIO()
                img.save(buf, format="PNG")
                rec.qr_code = base64.b64encode(buf.getvalue())
            else:
                rec.qr_code = False

    def _generate_unique_id(self):
        """Generate a unique ID for new objects."""
        seq = self.env["ir.sequence"].next_by_code("fire.protection.object")
        if not seq:
            seq = self.env["ir.sequence"].sudo().create({
                "name": "Fire Protection Object",
                "code": "fire.protection.object",
                "prefix": "FP-",
                "padding": 6,
            }).next_by_id()
        return seq

    def action_service_done(self):
        """Mark service as completed, set next service date."""
        self.ensure_one()
        today = fields.Date.today()
        from dateutil.relativedelta import relativedelta
        next_date = today + relativedelta(months=self.service_interval_months)
        self.write({
            "last_service_date": today,
            "next_service_date": next_date,
            "status": "ok",
        })

    def action_report_deficiency(self):
        """Mark object as deficient."""
        self.write({"status": "deficient"})

    def action_mark_critical(self):
        self.write({"status": "critical"})

    def action_retire(self):
        self.write({"active": False, "lifecycle_stage": "retired"})

    @api.model
    def cron_check_lifecycle(self):
        """Cron: check all objects and flag overdue ones."""
        objects = self.search([
            ("active", "=", True),
            ("lifecycle_stage", "in", ("due_service", "due_overhaul", "due_replacement")),
        ])
        for obj in objects:
            if obj.status != "critical":
                obj.message_post(
                    body=f"Service/overhaul due for {obj.display_name}",
                    message_type="notification",
                )
