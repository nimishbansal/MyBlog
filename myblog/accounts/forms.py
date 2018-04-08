from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    def __init__(self):
        self.password1.help_text
        super(SignupForm,self).__init__()
        print(locals())


x=SignupForm()