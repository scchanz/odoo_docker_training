from odoo import models, fields


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"

    GENRE_SELECTION = [
        ("general", "General"),
        ("fiction", "Fiction"),
        ("non_fiction", "Non Fiction"),
        ("science", "Science"),
        ("technology", "Technology"),
        ("history", "History"),
        ("biography", "Biography"),
    ]

    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author")
    isbn = fields.Char(string="ISBN")
    genre = fields.Selection(GENRE_SELECTION, string="Genre", default="general")
    publication_date = fields.Date(string="Publication Date")
    pages = fields.Integer(string="Pages")
    available = fields.Boolean(string="Available", default=True)
    description = fields.Text(string="Description")
