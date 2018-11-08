from django import forms

# 用来上传图像的表单
class ProfileForm(forms.Form):
    name = forms.CharField(max_length = 100, label='名字：')
    picture = forms.ImageField(label='图片：') 