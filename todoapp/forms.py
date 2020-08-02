from django import forms


class TaskAddForm(forms.Form):
    task_text = forms.CharField(max_length=30)
    task_deadline = forms.DateTimeField()
    add_time = forms.DateTimeField()
