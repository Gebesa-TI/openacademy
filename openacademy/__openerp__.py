# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "openacademy",
    "summary": "Openacademy",
    "version": "9.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://odoo-community.org/",
    "author": "<AUTHOR(S)>, Cesar Barron",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
    ],
    "data": [
        "view/openacademy_curse_view.xml",
        "view/openacademy_session_view.xml",
        "view/res_partner_view.xml",
    ],
    "demo": [
        "demo/openacademy_curse.xml",
        "demo/res_partner_academy.xml",
    ],
    "qweb": [
        "static/src/xml/module_name.xml",
    ]
}
