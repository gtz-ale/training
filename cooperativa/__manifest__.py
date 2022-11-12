# -*- coding utf-8 -*-
{
    'name': 'Cooperativa Exercise',
    'summary': """Training""",
    'description': """
    
    Control de Cooperativa:
    -Mercancias
    -Punto de Venta
    -Distribucion
    
    """,
    
    'author': 'Unifrut',
    
    'website': 'unifrut.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/tasks_security.xml',
        'security/ir.model.access.csv',
        'views/cooperativa_menuitem.xml',
        'views/tasks_views.xml',
    ],
        
    'license': 'OPL-1',
    
    'demo':[
        'demo/cooperativa_demo.xml',
    ],
    
}