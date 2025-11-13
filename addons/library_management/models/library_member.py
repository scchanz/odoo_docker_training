from odoo import models, fields


class LibraryMember(models.Model):
    _name = "library.member"
    _description = "Library Member"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    address = fields.Text(string="Address")
    join_date = fields.Date(string="Join Date", default=fields.Date.context_today)
    active = fields.Boolean(string="Active", default=True)
