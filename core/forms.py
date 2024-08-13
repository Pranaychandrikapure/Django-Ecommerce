from django import forms
from core.models import ProductReview

class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Write an review...'}), max_length=200, required=True)
    class Meta:
        model = ProductReview
        fields = ['review','rating']
