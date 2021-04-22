from django import forms

family_choice=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4')
)

education_choice=(
    ('1','Undergrad'),
    ('2','Graduate'),
    ('3','Professional')
)

common_choice=(
    ('0','No'),
    ('1','Yes'),
)
class PersonForm(forms.Form):
    age = forms.IntegerField()
    income = forms.IntegerField()
    family = forms.ChoiceField(choices=family_choice)
    ccavg = forms.FloatField()
    education = forms.ChoiceField(choices=education_choice)
    mortgage = forms.IntegerField()
    sec_account = forms.ChoiceField(choices=common_choice)
    cd_account = forms.ChoiceField(choices=common_choice)
    online = forms.ChoiceField(choices=common_choice)
    credit_card = forms.ChoiceField(choices=common_choice)