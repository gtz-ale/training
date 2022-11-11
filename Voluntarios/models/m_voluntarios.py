# -*- coding utf-8 -*-
from odoo import models, fields, api

class Voluntarios(models.Model):
    
    _name = 'tareas.m_voluntarios'
    _description = 'Tareas a ejecutar'

   # name = fields.Char(string='Tarea', required=True)
    #description = fields.Text(string='Descripcion')
    
   # frecuency = fields.Selection(string='Frecuencia',
    #                        selection=[('diaria', 'Diariamente'),
     #                                  ('semanal', 'Semanal'),
      #                                 ('mensual', 'Mensual')],
       #                     copy=False)

    
   # active = fields.Boolean(string='Activo', default=True)