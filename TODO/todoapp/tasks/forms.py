from django import forms
from .models import TaskItem

class datePickerInput(forms.DateInput):
    input_type = 'date'

class TaskItemCreateForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields =('title', 'description','deadline','category')
        widgets = {
            'deadline': datePickerInput(),
        }

class TaskItemUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields =('title','description','deadline','task_finished','category')
        widgets = {
            'deadline': datePickerInput(),
        }