from django.contrib.auth.models import User
from django import forms


# 장고에서의 form : HTML 의 form 역할, 또는 데이터 베이스에 저장할 내용을 형식과 제약조건을 만드는 역할.
# 장고의 form 기능을 적극 활용할 수 있도록 하자.

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username' : '아이디',
            'first_name':'이름(성)',
            'last_name' : '이름',
            'email' : '이메일'
        }
        
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('패스워드가 일치하지 않습니다.')
        return cd['password2']