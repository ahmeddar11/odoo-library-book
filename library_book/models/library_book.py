from odoo import models, fields ,api


class LibraryBook(models.Model):
    _name = 'library.book'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    title = fields.Char(required=1 , traking=True)
    author = fields.Char(required=1 , traking=True)
    total_copies = fields.Integer(required=1, tracking=True)
    degt_library = fields.Boolean()
    borrowed_copies = fields.Integer()
    available_copies = fields.Float(compute='_compute_available_copies', string='Total', store=True , tracking=True)



    @api.depends('available_copies','borrowed_copies','total_copies')
    def _compute_available_copies(self):
        for line in self:

            line.available_copies = line.total_copies - line.borrowed_copies