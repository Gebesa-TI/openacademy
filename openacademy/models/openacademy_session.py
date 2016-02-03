# -*- coding: utf-8 -*-
# © <2016> <Cesar Barron>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class OpenacademySession(models.Model):
    _name = 'openacademy.session'
    _description = 'Sesiones de Openacademy'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner',
                                    string="Instructor")
    course_id = fields.Many2one('openacademy.curse',
                                ondelete='cascade',
                                string="Curse",
                                required=True)
    attendee_ids = fields.Many2many('res.partner', string="Asistentes")


