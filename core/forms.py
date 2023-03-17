from .models import UserPost
from django.forms import ModelForm, TextInput, Textarea, Select, \
    Form, EmailField, EmailInput, ChoiceField, RadioSelect


class OnlineGroupForm(Form):
    email = EmailField(widget=EmailInput(attrs={'placeholder': 'Email'}))


class UserPostForm(ModelForm):
    class Meta:
        model = UserPost
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter your name (optional)', 'class': 'q-form'}),
            'case': Textarea(attrs={
                'rows': "6",
                'placeholder': 'Courthouse, the judge, any professionals that were significant '
                               'in the case or anyone professional/agency that you are referring',
                'class': 'q-form'
            }),
            'abuse_from_CPS_DCFS': Select(attrs={'placeholder': 'Were there any abuse or safety issues'}),
            'parental_alienation': Select(attrs={'placeholder': 'Confirmed parental alienation'}),
            'allegations': Select(attrs={'placeholder': 'Allegations of parental alienation'}),
            'falsified': Select(attrs={'placeholder': 'Falsified allegations'}),
            'duration': Textarea(attrs={
                'rows': "6",
                'placeholder': 'How long has the case been in the Utah family court system',
                'class': 'q-form'
            }),
            'money': Textarea(attrs={
                'rows': "6",
                'placeholder': 'How much money has been paid in fees?',
                'class': 'q-form'
            }),
            'left_broken': Textarea(attrs={
                'rows': "6",
                'placeholder': 'Ethics / Abuse criteria / Safety issues were left or were broken',
                'class': 'q-form'
            }),
            'abuse_criteria': Textarea(attrs={
                'rows': "6",
                'placeholder': 'Abuse criteria that was not acknowledged addressed or treated',
                'class': 'q-form'
            }),
            'result': Textarea(attrs={
                'rows': "6",
                'placeholder': 'What was the result?',
                'class': 'q-form'
            }),
        }


class CoParentingForm(Form):
    QUESTIONS = [
        "Are you constantly being criticized or bad-mouthed by your co-parent to your child?",
        "Does your co-parent try to turn your child against you or prevent your child from having a relationship with you?",
        "Does your child seem torn between you and your co-parent, or feel like they have to choose sides?",
        "Does your child seem afraid to express their love or affection for you in front of your co-parent?",
        "Has your child been told by your co-parent to keep secrets from you or to lie to you?",
        "Does your child seem to be used as a messenger between you and your co-parent to convey messages or information?",
        "Does your child seem to be caught in the middle of conflicts between you and your co-parent?",
        "Does your child feel like they have to protect your co-parent from you?",
        "Have you been threatened or coerced into cutting off contact with your child by your co-parent?",
        "Does your co-parent seem to be trying to turn your child against you?",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i, question in enumerate(self.QUESTIONS):
            self.fields[f"question{i+1}"] = ChoiceField(
                label=question,
                choices=[(1, "Yes"), (0, "No")],
                widget=RadioSelect,
                required=True,
            )
