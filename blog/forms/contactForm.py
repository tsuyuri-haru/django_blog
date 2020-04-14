from django import forms
from django.contrib.auth.models import User


CATEGORIES = (
    ('1','サイト内容に関する問い合わせ'),
    ('2','その他の問い合わせ'),
    )

class ContactForm(forms.Form):
    """問い合わせ用フォーム"""
    name = forms.CharField(
        label = 'お名前', max_length= 50,
        required=True, help_text="*必須"
        )
    

    email = forms.EmailField(
        label='メールアドレス', required=False, help_text='*任意'
        )

    text = forms.CharField(label='問い合わせ内容', widget=forms.Textarea)
    category = forms.ChoiceField(label='カテゴリ', choices=CATEGORIES)

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name:
            self.add_error('名前の入力は必須です。')
        if name in ('暴言'):
            self.add_error('name','名前に暴言を含めないでください！')
            if name == 'idiot':
                self.add_error('name','英語でも駄目です')
        return name



