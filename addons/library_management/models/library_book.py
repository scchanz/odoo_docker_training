from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"

    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author")
    isbn = fields.Char(string="ISBN")
    publication_date = fields.Date(string="Publication Date")
    pages = fields.Integer(string="Pages")
    available = fields.Boolean(string="Available", default=True)
    description = fields.Text(string="Description")  # <-- Tambahkan ini
