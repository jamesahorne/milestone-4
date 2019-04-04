from django import forms
from .models import BugTicket, FeatureTicket


class BugTicketForm(forms.ModelForm):
    class Meta:
        model = BugTicket
        fields = ('bug_issue_type', 'bug_issue_name', 'bug_issue_description',
                  'bug_status', 'bug_urgent')


class FeatureTicketForm(forms.ModelForm):
    class Meta:
        model = FeatureTicket
        fields = ('feature_issue_type', 'feature_issue_name',
                  'feature_issue_description', 'feature_status',
                  'feature_urgent')
