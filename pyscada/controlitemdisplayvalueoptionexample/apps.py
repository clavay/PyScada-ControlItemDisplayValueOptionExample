# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.db.utils import ProgrammingError, OperationalError

from . import __app_name__


class PyScadaControlItemDisplayValueOptionExampleConfig(AppConfig):
    name = "pyscada." + __app_name__.lower()
    verbose_name = _("PyScada " + __app_name__ + " Master/Client")
    path = os.path.dirname(os.path.realpath(__file__))
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        try:
            from pyscada.hmi.models import TransformData

            TransformData.objects.update_or_create(
                short_name="MeanAndDivByVar",
                defaults={
                    "inline_model_name": "TransformDataMeanAndDivByVar",
                    "js_function_name": "PyScadaControlItemDisplayValueTransformDataMeanAndDivByVar",
                    "js_files": "pyscada/js/pyscada/TransformDataMeanAndDivByVarPlugin.js",
                    "css_files": "",
                    "need_historical_data": True,
                },
            )
        except ProgrammingError:
            pass
        except OperationalError:
            pass

        try:
            from pyscada.hmi.models import DisplayValueOptionTemplate

            # create the circular gauge for control item display value option
            DisplayValueOptionTemplate.objects.update_or_create(
                label="Example",
                defaults={
                    "template_name": "example.html",
                    "js_files": "pyscada/js/pyscada/DisplayValueOptionTemplateExample.js",
                    "css_files": "",
                },
            )
        except ProgrammingError:
            pass
        except OperationalError:
            pass
