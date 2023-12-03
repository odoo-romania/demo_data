# Copyright 2020 NextERP Romania SRL
# License OPL-1.0 or later
# (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#).

{
    "name": "Demo Data Module",
    "version": "15.0.1.0.0",
    "category": "General",
    "author": "NextERP Romania SRL",
    "website": "https://github.com/OCA/l10n-romania",
    "summary": """Create demo data for Romanian Localisation""",
    "depends": [
        "l10n_ro_account",
        "l10n_ro_account_anaf_sync",
        "l10n_ro_account_bank_statement_report",
        "l10n_ro_account_edi_ubl",
        "l10n_ro_account_edit_currency_rate",
        "l10n_ro_account_period_close",
        "l10n_ro_account_report_invoice",
        "l10n_ro_city",
        "l10n_ro_dvi",
        "l10n_ro_fiscal_validation",
        "l10n_ro_nondeductible_vat",
        "l10n_ro_partner_unique",
        "l10n_ro_payment_receipt_report",
        "l10n_ro_payment_to_statement",
        "l10n_ro_stock_account_date_wizard",
        "l10n_ro_stock_account_mrp",
        "l10n_ro_stock_account_notice",
        "l10n_ro_stock_account_reception_in_progress",
        "l10n_ro_stock_picking_comment_template",
        "l10n_ro_stock_picking_valued_report",
        "l10n_ro_stock_price_difference",
        "l10n_ro_stock_report",
        "sale_management"
    ],
    "external_dependencies": {"python3": ["faker", "faker-commerce"]},
    "demo": [
        "demo/res_partner.xml",
        "demo/product_category.xml",
        "demo/product_product.xml",
        "demo/sale_order.xml",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_company_views.xml",
    ],
    "installable": True,
    "auto_install": False,
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
    "license": "OPL-1",
}
