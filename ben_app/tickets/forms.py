from django import forms

from tickets.models import Ticket
from tickets.widgets.star_replacer import StarReplacerWidget


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'category', 'status', 'description', 'rating', 'board')
        widgets = {
            'rating': StarReplacerWidget(),
        }


class SearchForm(forms.Form):
    CATEGORY_CHOICES = (('', ''), ('Severe', 'Severe'), ('Moderate', 'Moderate'), ('Minor', 'Minor'))
    STATUS_CHOICES = (('', ''), ('New', 'New'), ('Under Review', 'Under Review'), ('Solved', 'Solved'))

    author = forms.CharField(required=False)
    title = forms.CharField(required=False)
    category = forms.ChoiceField(required=False, choices=CATEGORY_CHOICES)
    status = forms.ChoiceField(required=False, choices=STATUS_CHOICES)

