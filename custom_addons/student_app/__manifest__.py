# -*- coding: utf-8 -*-


{
    'name': "student_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'hr', 'mail'],

    # always loaded
    'data': [
        # "security/student_group_Access.xml",
        # "security/ir.model.access.csv",
        # "security/ir.model.employee.csv",
        # 'views/views.xml',
        # 'views/templates.xml',
        "views/model_upgrade.xml",
        "views/sale_order_update_view.xml",
        "views/student_data_lines.xml",
        "views/student_corner.xml",
        "views/Configure_course.xml",
        "views/Configure_skills.xml",
        # "views/hr_employee_update.xml",
        "views/employee_document.xml",
        

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,  # for visual in admin as app install
}
