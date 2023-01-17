from .models import UserPost
from django.forms import ModelForm, TextInput, Textarea, Select


class UserPostForm(ModelForm):
    class Meta:
        model = UserPost
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter your name (optional)'}),
            'case': Textarea(attrs={
                'rows': "6",
                'placeholder': 'Courthouse, the judge, any professionals that were significant '
                               'in the case or anyone professional/agency that you are referring'
            }),
            'abuse_from_CPS_DCFS': Select(attrs={'placeholder': 'Were there any abuse or safety issues'}),
            'parental_alienation': Select(attrs={'placeholder': 'Confirmed parental alienation'}),
            'allegations': Select(attrs={'placeholder': 'Allegations of parental alienation'}),
            'falsified': Select(attrs={'placeholder': 'Falsified allegations'}),
            'duration': Textarea(attrs={
                'rows': "6",
                'placeholder': 'How long has the case been in the Utah family court system'
            }),
            'money': Textarea(attrs={
                'rows': "6",
                'placeholder': 'How much money has been paid in fees?'
            }),
            'left_broken': Textarea(attrs={
                'rows': "6",
                'placeholder': 'Ethics / Abuse criteria / Safety issues were left or were broken'
            }),
            'abuse_criteria': Textarea(attrs={
                'rows': "6",
                'placeholder': 'Abuse criteria that was not acknowledged addressed or treated'
            }),
            'result': Textarea(attrs={
                'rows': "6",
                'placeholder': 'What was the result?'
            }),
        }
