# -*- coding utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError

class Cooperativa(models.Model):
    _name = 'tasks.tareas'
    _description = 'Odoo Ejercicio Cooperativa'
    
    name = fields.Char(string='Nombre de la Tarea', required= True)
    description = fields.Text(string='Descripcion')
    #start_task = fields.Datetime(string="Inicio")
    #end_task = fields.Datetime(string="Fin")
    start_task = fields.Char(string='Hora Inicio')
    end_task = fields.Char(string='Hora Finalizacion')
    
    frecuencia = fields.Selection(string='Frecuencia',
                            selection=[('dia', 'Diariamente'),('semana', 'Semanal'),('mes', 'Mensual')],)
    
    active = fields.Boolean(string='Activo', default=True)
    
    status = fields.Selection(string='Estado de la tarea',
			   selection=[('borrador','Borrador'),
				     ('preparado','Preparado'),
				     ('ejecucion','En ejecucion'),
				     ('listo','Listo')],)
    lider = fields.Text(string='Lider de la Tarea',default='')
    
    status_change = fields.Text(string='Estado de la Tarea')
    
    @api.onchange('status', 'lider')
    def _onchange_status(self):
                if self.lider == none:
                    raise UserError('')
            
                self.status = "Listo"
                
    @api.constrains('status')
    def _check_status(self):
        for record in self:
            if record.status == none:
                raise ValidationError('Debe asignar un Estado a la Tarea')