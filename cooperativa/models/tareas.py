# -*- coding utf-8 -*-

from odoo import models, fields, api

class Cooperativa(models.Model):
    _name = 'tasks.tareas'
    _description = 'Odoo Ejercicio Cooperativa'
    
    name = fields.Char(string='Nombre de la Tarea', required= True)
    description = fields.Text(string='Descripcion')
    
    frecuencia = fields.Selection(string='Frecuencia',
                            selection=[('dia', 'Diariamente'),('semana', 'Semanal'),('mes', 'Mensual')],)
    
    activo = fields.Boolean(string='Active', default=True)
    