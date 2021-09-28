{
    "name": "Sale report Extensions",
    "summary": "Personalización de las plantilas de cotización y facturas - Localización Venezuela",
    "version": "14.0.1.0.1",
    "category": "Sales",
    #"website": "https://github.com/OCA/partner-contact",
    "author": "TeletrabajoVE - Luis Magin Mata",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "auto_install": False,
  #  "depends": ["partner_contact_personal_information_page"],
    "depends": ["sale", "product_brand_sale"],
    "data": [
       "report/templates.xml",
       "views/sale_view_order_form.xml",
       "report/header_footer.xml"
     #  "views/quot_digital.xml"  
       ]


    #"data": ["views/res_partner.xml", "data/data.xml"],
   # "post_init_hook": "post_init_hook",
}
