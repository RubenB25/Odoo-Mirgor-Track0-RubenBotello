from odoo import models,fields, api

class BookManagement(models.Model):
    _name = "book.management"
    _description = "Book Management"
    _rec_name = "complete_name"
    
    author = fields.Char(string="Author",default="Algo")
    release_date = fields.Char(string="Date")
    summary = fields.Char(string="Summary")
    total_pages = fields.Integer(string="Pages",default=0)
    author_continues_writing_books = fields.Boolean(string="Still writing books?")
    complete_name = fields.Char(string="Nombre Completo", compute="_complete_name")
    res_partner_id = fields.Many2one('res.partner', string='Contacto')
    @api.depends('author','total_pages')
    def _complete_name(self):
        for rec in self:
            if rec.author and rec.total_pages:
                rec.complete_name = '%s - %s' % (rec.author, rec.total_pages)
            else:
                rec.complete_name = rec.author
            