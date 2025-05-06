from django import forms
from engine_app.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["user_name", "comment", "rating", "user_phone_number"]
