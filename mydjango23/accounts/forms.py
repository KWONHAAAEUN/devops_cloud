from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# TODO: email을 추가로 입력 받으려 합니다
#   User 모델에 대한 ModelForm
#       -Meta.fields=>["username"]
#       -추가 form fields=>password1, password2

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta): # 모델 폼을 상속 받기 위해 폼의 이름을 앞에 지정
        fields=["username","email"]

class LoginForm(AuthenticationForm):
    answer=forms.CharField(
        label="퀴즈답",
        help_text="3+3=?",
    )

    def clean_answer(self):
        answer=self.cleaned_data.get("answer")
        if answer != "6":
            raise forms.ValidationError("땡.")
        return answer