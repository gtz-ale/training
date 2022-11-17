# -*- coding utf-8 -*-
from odoo import models, fields, api

class Session(models.Model):
    _name = 'cooperativa_session'
    _description = 'Informacion de la sesion'
    
    cooperativa_id = fields.Many2one(comodel_name='tasks.tareas',
                                    string='Cooperativa',
                                    ondelete='cascade',
                                    required=True)
    
    name = fields.Char(strins='Title', related='cooperativa_id.name')
    
    lider_id = fields.Many2one(comodel_name='res.parner', string='Lider')
    voluntario_ids = fields.Many2many(comodel_name='res.parner', string='Voluntario')
