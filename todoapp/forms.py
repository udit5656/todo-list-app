from django import forms
from django.utils.datetime_safe import datetime
from django.utils.timezone import now


class TaskAddForm(forms.Form):
    task_text = forms.CharField(max_length=30)
    task_deadline = forms.DateTimeField()
    add_time = forms.DateTimeField()

    def clean(self):
        cleaned_data = super().clean()
        deadline = cleaned_data.get("task_deadline")
        addtime = cleaned_data.get("add_time")
        if deadline and addtime:
            if deadline < addtime:
                raise forms.ValidationError("Deadline should not be in past or before add time")
