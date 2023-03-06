from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields=['symbol', 'type', 'investor_first_name', 'investor_last_name', 'date_of_the_order',
                'floors', 'area', 'walls', 'ceiling', 'roof', 'elevation', 'view']
