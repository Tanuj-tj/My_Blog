from django.forms import ModelForm
from .models import Post


class PostEditForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author','title','category', 'thumbnail', 'content',]

    def __init__(self, *args, **kwargs):
        super(PostEditForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', })

        self.fields['category'].widget.attrs.update(
            {'class': 'form-control', })

        self.fields['content'].widget.attrs.update(
            {'class': 'form-control', })


# class ProjectForm(ModelForm):

#     class Meta:
#         model = Project
#         fields = ['title', 'thumbnail', 'body']

#     def __init__(self, *args, **kwargs):
#         super(ProjectForm, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update(
#             {'class': 'form-control'})

#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control', })
