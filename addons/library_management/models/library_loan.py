from odoo import models, fields


class LibraryLoan(models.Model):
    _name = "library.loan"
    _description = "Library Loan"
    _order = "loan_date desc"

    name = fields.Char(string="Reference", readonly=True, copy=False)
    book_id = fields.Many2one("library.book", string="Book", required=True, ondelete="cascade")
    member_id = fields.Many2one("library.member", string="Member", required=True, ondelete="cascade")
    loan_date = fields.Date(string="Loan Date", default=fields.Date.context_today, required=True)
    expected_return = fields.Date(string="Expected Return")
    return_date = fields.Date(string="Return Date")
    state = fields.Selection(
        [
            ("ongoing", "Ongoing"),
            ("returned", "Returned"),
            ("late", "Late"),
        ],
        string="Status",
        default="ongoing",
    )
    notes = fields.Text(string="Notes")
