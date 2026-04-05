from odoo import models, fields ,api


class LibraryBook(models.Model):
    _name = 'library.book'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    title = fields.Char(required=1 , traking=True)
    name_author = fields.Char(required=1 , traking=True)
    total_copies = fields.Integer(required=1, tracking=True)
    degt_library = fields.Boolean()
    borrowed_copies = fields.Integer()
    available_copies = fields.Float(compute='_compute_available_copies', string='Total', store=True , tracking=True)

    state = fields.Selection(
        [
            ('available', 'Available'),
            ('borrowed', 'Borrowed'),
            ('lost', 'Lost'),
        ],
        default='available',
        required=True,
        tracking=True
    )



    @api.depends('available_copies','borrowed_copies','total_copies')
    def _compute_available_copies(self):
        for line in self:

            line.available_copies = line.total_copies - line.borrowed_copies




    def action_in_available(self):
        for rec in self:
            rec.state = 'available'

    def action_in_borrowed(self):
        for rec in self:
            rec.state = 'borrowed'

    def action_in_lost(self):
        for rec in self:
            rec.state = 'lost'
