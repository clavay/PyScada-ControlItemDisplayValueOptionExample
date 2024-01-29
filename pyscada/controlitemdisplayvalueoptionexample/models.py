from django.db import models
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError

from pyscada.hmi.models import DisplayValueOption, TransformData
from pyscada.models import Variable


class TransformDataMeanAndDivByVar(models.Model):
    display_value_option = models.OneToOneField(
        DisplayValueOption, on_delete=models.CASCADE
    )
    variable = models.ForeignKey(
        Variable, on_delete=models.CASCADE, blank=True, null=True
    )

    class FormSet(BaseInlineFormSet):
        def clean(self):
            super().clean()
            class_name = self.model.__name__
            if (
                self.data["transform_data"] != ""
                and TransformData.objects.get(id=self.data["transform_data"])
                is not None
            ):
                transform_data_name = TransformData.objects.get(
                    id=self.data["transform_data"]
                ).inline_model_name
                if (
                    class_name == transform_data_name
                    and self.data[transform_data_name.lower() + "-0-variable"] == ""
                    and self.data["transform_data"] != ""
                ):
                    raise ValidationError("Variable is required.")
