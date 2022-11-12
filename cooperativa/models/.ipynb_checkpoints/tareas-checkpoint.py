# -*- coding utf-8 -*-

from odoo import models, fields, api

class Cooperativa(models.Model):
    _name = 'tasks.tareas'
    _description = 'Odoo Ejercicio Cooperativa'
    
    name = fields.Char(string='Nombre de la Tarea', required= True)
    description = fields.Text(string='Descripcion')
    #start_task = fields.Datetime(string="Inicio Tarea")
    #end_task = fields.Datetime(string="Fin Tarea")
    
    frecuencia = fields.Selection(string='Frecuencia',
                            selection=[('dia', 'Diariamente'),('semana', 'Semanal'),('mes', 'Mensual')],)
    
    active = fields.Boolean(string='Activo', default=True)
    