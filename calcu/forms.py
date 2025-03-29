from django import forms


class WeirdCalcuForm(forms.Form):

    first_number = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'size':'1',
            'id': 'WeirdCalcu_first_number',
        }),
    )

    second_number = forms.FloatField(
        widget=forms.NumberInput(attrs={
            'size': '1',
            'id': 'WeirdCalcu_second_number',
        }),
    )
