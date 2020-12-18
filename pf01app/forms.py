from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

  def clean_username(self):
      username = self.cleaned_data.get('username')
      if User.objects.filter(username=username).exists():
          raise forms.ValidationError('The username has been already taken.')
      return username

  def clean_password(self):
      password = self.cleaned_data.get('password')
      if len(password) < 5:
          raise forms.ValidationError('Password must contain 5 or more characters.')
      return password