from django import forms


class InputForm(forms.Form):
    """
    Form to get user input. The input should be the n parameter that will
    set the number of die sides and numner of throws.
    """
    n = forms.CharField(
        widget=forms.NumberInput()
    )

    def clean_n(self):
        """
        Custom validation for n field. In addition of n of being a valid
        number, it shall be positive and greater than 1.
        """
        n = int(self.cleaned_data['n'])

        if n < 0:
            raise forms.ValidationError(
                "n must be a positive integer number",
                code='negative_input'
            )
        elif n <= 1:
            raise forms.ValidationError(
                "n must be strictly greater than 1",
                code='small_input'
            )

        return n
