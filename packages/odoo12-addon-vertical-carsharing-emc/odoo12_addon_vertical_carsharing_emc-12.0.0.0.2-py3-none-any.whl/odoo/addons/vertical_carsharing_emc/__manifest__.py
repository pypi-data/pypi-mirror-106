# -*- coding: utf-8 -*-
{
  'name': "vertical_carsharing_emc",

  'summary': """
    Enhace EMC subscription request with carsharing logic""",

  'author': "Som Mobilitat",
  'website': "https://www.sommobilitat.coop",

  # Categories can be used to filter modules in modules listing
  # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
  # for the full list
  'category': 'vertical-carsharing',
  'version': '12.0.0.0.2',

  # any module necessary for this one to work correctly
  'depends': [
    'base',
    'vertical_carsharing',
    'easy_my_coop',
    'easy_my_coop_es',
    'sm_partago_user'
  ],

  # always loaded
  'data': [
    'views/views_subscription_request.xml',
    'views/views_cs_registration_request.xml'
  ],
  # only loaded in demonstration mode
  'demo': [],
}
