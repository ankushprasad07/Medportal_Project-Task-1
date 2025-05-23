# from django import forms
# from .models import BlogPost

# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
#             'category': forms.Select(attrs={'class': 'form-control'}),
#             'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Short summary'}),
#             'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Full content'}),
#             'is_draft': forms.CheckboxInput(),
#         }


from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Title',
            }),
            'category': forms.Select(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
            'summary': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2 h-20 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Short summary',
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded px-3 py-2 h-40 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Full content',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full text-gray-700',
            }),
            'is_draft': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 text-blue-600 rounded focus:ring-blue-500',
            }),
        }
