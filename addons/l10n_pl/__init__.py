# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


def _preserve_tag_on_taxes(env):
    from odoo.addons.account.models.chart_template import preserve_existing_tags_on_taxes
    preserve_existing_tags_on_taxes(env, 'l10n_pl')


def load_translations(env):
    env.ref('l10n_pl.pl_chart_template').process_coa_translations()


def post_init_hook(env):
    _preserve_tag_on_taxes(env)
    load_translations(env)
