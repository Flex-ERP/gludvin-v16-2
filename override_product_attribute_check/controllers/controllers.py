# -*- coding: utf-8 -*-
# from odoo import http


# class OverrideProductAttributeCheck(http.Controller):
#     @http.route('/override_product_attribute_check/override_product_attribute_check', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/override_product_attribute_check/override_product_attribute_check/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('override_product_attribute_check.listing', {
#             'root': '/override_product_attribute_check/override_product_attribute_check',
#             'objects': http.request.env['override_product_attribute_check.override_product_attribute_check'].search([]),
#         })

#     @http.route('/override_product_attribute_check/override_product_attribute_check/objects/<model("override_product_attribute_check.override_product_attribute_check"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('override_product_attribute_check.object', {
#             'object': obj
#         })
