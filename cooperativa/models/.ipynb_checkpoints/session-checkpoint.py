# -*- coding utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta

class Session(models.Model):
    _name = 'cooperativa.session'
    _description = 'Informacion de la sesion'
    
    cooperativa_id = fields.Many2one(comodel_name='tasks.tareas',
                                    string='Cooperativa',
                                    ondelete='cascade',
                                    required=True)
    
    name = fields.Char(string='Title', related='cooperativa_id.name')
    
    lider_id = fields.Many2one(comodel_name='res.partner', string='Lider')
    voluntario_id = fields.Many2many(comodel_name='res.partner', string='Voluntario')

    start_time = fields.Date(string = 'Tiempo Inicio',
                            default = fields.Date.today)
    
    duration = fields.Integer(string ='Duracion',
                            default=1)
    
    end_time = fields.Date(string='Tiempo Fin',
                             compute='_compute_end_date',
                             inverse='_inverse_end_date',
                             store=True)
    
    @api.depends('start_time','duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.start_time and record.duration):
                record.end_time = record.start_time
            else:
                duration = timedelta(days=record.duration)
                record.end_time = record.start_time + duration
                
    def _inverse_end_date(self):
        for record in self:
            if record.start_time and record.end_time:
                record.duration = (record.end_time - record.start_time).days +1
            else:
                continue