from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(max_length=4000,widget=forms.Textarea(
        attrs={'rows':5, 'placeholder':'What is your mind?'}
    ),
                              help_text="The max length is 40"
                              )

    class Meta:
        model = Topic
        fields = ['subject', 'message']