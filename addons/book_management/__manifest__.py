{
    'name': "Book Management",
    'version': "1.0",
    'summary': "Book management",
    'description': "Module to manage books",
    'author': "Mirgor",
    'category': '',
    'website': '',
    "installable": True,
    "application": True,
    'depends': [
        'base', "contacts"
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/book_management_view.xml',
        'views/res_partner_view.xml',
    ],
    'demo':""
}
