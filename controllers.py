# -*- coding: utf-8 -*-
from openerp import http

# class Moduloinstalador(http.Controller):
#     @http.route('/moduloinstalador/moduloinstalador/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/moduloinstalador/moduloinstalador/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('moduloinstalador.listing', {
#             'root': '/moduloinstalador/moduloinstalador',
#             'objects': http.request.env['moduloinstalador.moduloinstalador'].search([]),
#         })

#     @http.route('/moduloinstalador/moduloinstalador/objects/<model("moduloinstalador.moduloinstalador"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('moduloinstalador.object', {
#             'object': obj
#         })