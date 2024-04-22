{
    'name': "Book Management",
    'version': "1.0",
    'summary': "Book Management",
    'description': "Module to manage books",
    'author': "Mirgor",
    'category': '',
    'website': '',
    "installable": True,
    "application": True,
    'depends': [
       'base', 'mail', "contacts", "web",
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/book_management_view.xml',
        'views/book_copy_view.xml',
        'reports/book_copy_complete_report.xml',
        'reports/book_copy_summary_report.xml',
        'views/author_management_view.xml',
        'views/res_partner_view.xml',
        'views/book_category_view.xml',
        'views/book_copy_wizard_view.xml',
        'data/email_template.xml',
    ],
    'images': [
        'static/description/icon.png',
               ],
        
    'demo':""
}
