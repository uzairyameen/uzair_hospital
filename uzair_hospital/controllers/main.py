from odoo import http

class UzairHospitalController(http.Controller):
    @http.route('/uzair_hospital/hello', auth='public', website=True)
    def hello_world(self, **kwargs):
        return "You are using controllers in uzair_hospital!"

