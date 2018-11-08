from django.shortcuts import render, redirect
from myApp.forms import ProfileForm # 上传图片的图表
from myApp.models import Profile # 保存上传图片相关信息的模型



def index(request):
    context = {}
    form = ProfileForm
    context['form'] = form 
    return render(request, 'index.html', context)


def save_profile(request):
    if request.method == "POST":
        # 接收 post 方法传回后端的数据
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            # 构造一个 Profile 实例
            profile = Profile()
            profile.name = form.cleaned_data["name"]
            profile.picture = form.cleaned_data["picture"]
            profile.save()

        else:
            form = ProfileForm()

        return redirect(to='show')


def show(request):
    context = {}

    pictures = Profile.objects.all()
    context['pictures'] = pictures
    return render(request, 'show.html', context)