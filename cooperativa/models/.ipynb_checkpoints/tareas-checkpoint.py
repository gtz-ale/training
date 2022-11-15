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
    
    #status = fields.Selection(string='Estado de la tarea',
	#		   selection=[('borrador','Borrador'),
	#			     ('listo','Listo'),
	#			     ('progreso','En Progreso'),
	#			     ('terminado','Terminado')], default='Borrador')
    
    status = fields.Char(string="Estado", default='Borrador')
    lider = fields.Char(string="Lider", default='')
    
    @api.onchange('status')
    def _onchange_status(self):
                if self.status == 'Borrador':
                    raise UserError('Ha cambiado el estado de la tarea.')
            
                self.status = 'Listo'
                
    @api.constrains('lider')
    def _check_lider(self):
        for record in self:
            if record.lider == '':
                raise ValidationError('Debe asignar un Lider a la Tarea')
