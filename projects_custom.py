from openerp.osv import fields, osv

class projects_custom(osv.osv):

    _inherit = "project.project"

    _columns = {
        'manager_name': fields.char('Manager Name', size=11)
    }
    _defaults ={
        'manager_name': 'Frontend'
    }  

projects_custom();
