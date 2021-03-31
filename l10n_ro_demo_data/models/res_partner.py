# Copyright 2020 NextERP Romania SRL
# License OPL-1.0 or later
# (https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#).

from odoo import models


class ResCompany(models.Model):
    _inherit = "res.partner"

    def _map_anaf_country_code(self, country_code):
        country_code_map = {
            "RE": "FR",
            "GP": "FR",
            "MQ": "FR",
            "GF": "FR",
            "EL": "GR",
        }
        return country_code_map.get(country_code, country_code)

    def _get_anaf_europe_codes(self):
        europe_codes = []
        europe_group = self.env.ref("base.europe", raise_if_not_found=False)
        if not europe_group:
            europe_group = self.env["res.country.group"].search(
                [("name", "=", "Europe")], limit=1
            )
        if europe_group:
            europe_codes = europe_group.country_ids.mapped("code") + ["XI"]
        return europe_codes

    def _parse_anaf_vat_info(self):
        """Return tuple with split info (country_code, identifier_type and
        vat_number) from vat and country partner
        """
        self.ensure_one()
        country_code = vat_number = False
        identifier_type = "4"
        if self.vat:
            vat_number = self.vat
            prefix = self._map_anaf_country_code(vat_number[:2].upper())
            if prefix in self._get_anaf_europe_codes():
                country_code = prefix
                identifier_type = "3"
            else:
                country_code = self._map_anaf_country_code(self.country_id.code) or ""
                if country_code in self._get_anaf_europe_codes():
                    identifier_type = "3"
                else:
                    identifier_type = "4"
            if country_code == "RO":
                if self.vat_subjected:
                    identifier_type = "1"
                else:
                    identifier_type = "2"

            vat_number = vat_number.replace(country_code, "")
        return country_code, identifier_type, vat_number
