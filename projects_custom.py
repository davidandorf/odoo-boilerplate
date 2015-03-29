from openerp import models, fields, api

class projects_custom(models.Model):

    _inherit = "project.project"

    
    department_id = fields.Many2one('hr.department',ondelete='set null', string="Department", index=True)
    price = fields.Integer(string='Price')
    qty = fields.Integer(string='Quantity')
    total = fields.Integer(string="Total",compute='_compute_total')
    
    @api.one
    @api.depends('price','qty')
    def _compute_total(self):
        self.total = self.price * self.qty
        
    @api.onchange('department_id')
    def _onchange_department_id(self):
        department = self.env['hr.department'].search([('department_id','=',department_id)])
        employee =  self.env['hr.employee'].search([('id','=',department.manager_id)])
        self.user_id = employee.user_id
        
        

