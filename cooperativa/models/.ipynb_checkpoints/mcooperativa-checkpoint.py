# -*- coding utf-8 -*-

from odoo import models, fields, api

class Cooperativa(models.Model):
    _name = 'tareas.cooperativa'
    _description = 'Odoo Ejercicio Cooperativa'
    
    name = fields.Char(string='Tarea a Realizar', required= True)
    description = fields.Text(string='Descripcion de la actividad')
    
    level = fields.Selection(string='Frecuencia',
                            slection=[('dia', 'Diaria'),
                                      ('semana', 'Semanal'),
                                      ('mes', 'Mensual')],
                             copy=False)
    
    active = fields.Boolean(string='Active', default=True)