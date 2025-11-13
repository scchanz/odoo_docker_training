{
    "name": "Library Management",
    "version": "1.0",
    "summary": "Manage books and members",
    "description": "A simple library management module for Odoo training",
    "category": "Tools",
    "author": "Zunn",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/library_book_views.xml",
    ],
    "installable": True,
    "application": True,
}
