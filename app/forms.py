from django import forms


class WordCountForm(forms.Form):
    text = forms.CharField(
        label='Text',
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Enter text here...'}),
        help_text='Enter some text to count words in it.'
    )
