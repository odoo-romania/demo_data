# Copyright 2020 NextERP Romania SRL
# License OPL-1.0 or later
# (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#).

from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _parse_anaf_vat_info(self):
        """Return tuple with split info (country_code, identifier_type and
        vat_number) from vat and country partner
        """
        self.ensure_one()
        country_code = vat_number = False
        identifier_type = "4"
        if (self.vat or self.country_id) and self.is_l10n_ro_record:
            vat_number = self.vat
            country_code = False
            if vat_number:
                country_code = self._split_vat(vat_number)[0].upper()
            if not country_code and self.country_id:
                country_code = self.country_id.code.upper()
            country_code = self._l10n_ro_map_vat_country_code(country_code)
            if country_code in self._get_l10n_ro_anaf_europe_codes():
                identifier_type = "3"
            if country_code == "RO":
                if self.l10n_ro_vat_subjected:
                    identifier_type = "1"
                else:
                    identifier_type = "2"

            if vat_number:
                vat_number = vat_number.replace(country_code, "")
        return country_code, identifier_type, vat_number
