# Copyright 2020 NextERP Romania SRL
# License OPL-1.0 or later
# (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#).

{
    "name": "Demo Data Module",
    "version": "14.0.1.0.0",
    "category": "General",
    "author": "NextERP Romania SRL,Asociatia Comunitatii Odoo",
    "website": "https://github.com/odoo-romania/demo_data",
    "summary": """Create demo data for Romanian Localisation""",
    "depends": [
        "l10n_ro_account_period_close",
        "l10n_ro_account_report_invoice",
        "l10n_ro_city",
        "l10n_ro_fiscal_validation",
        "l10n_ro_partner_unique",
        "l10n_ro_stock_account",
        "sale_management",
    ],
    "external_dependencies": {"python3": ["faker", "faker-commerce"]},
    "data": [
        "security/ir.model.access.csv",
        "views/res_company_views.xml",
        "data/res_partner.xml",
        "data/product_category.xml",
        "data/product_product.xml",
        "data/sale_order.xml",
    ],
    "installable": True,
    "auto_install": False,
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
    "license": "OPL-1",
}
