from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth import logout
from django.views.generic.base import View
from django.db.models import Q

# Create your views here.
def list_view(request, page_number=1):
    if request.user.is_superuser:
        user= request.user
        return render(request, 'index.html', {
            'users':user,
            })
    if request.user.is_authenticated:
        user= request.user
        return render(request, 'index.html', {
            'users':user,
            })
    return render(request, 'index.html', {
      
    })



class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/auth"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView,self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "auth.html"
    success_url = "/account"
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

def account_view(request ):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Exception:
            profile = Profile(user=request.user, has_music=False, bg="#f0f3fa")
            profile.save()
        if request.user.is_superuser:
            messages = Chat.objects.filter(is_readed=False, type_message=2)
            users = User.objects.filter(is_superuser=False)
            return render(request, 'users.html', {
          'users':users,
          'messages':messages,
        })
        profile = Profile.objects.get(user=request.user)
        bg = profile.bg
        first_name = request.user.first_name
        last_name = request.user.last_name
        homework = Homework.objects.filter(user=request.user, status=2) | Homework.objects.filter(user=request.user, status=3)
        number_not_read = Chat.objects.filter(is_readed=False, type_message=1, user=request.user).count()
        answer = Answers.objects.filter(user=request.user)
        type_user = profile.type_user
        if type_user is "":
            typeu = "None"
        else:
            typeu = type_user
        return render(request, 'cabinet.html', {
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'count':number_not_read,
          'has_music': profile.has_music,
          'homework':homework.count(),
          'typeu': typeu,
        })
    else:
        return HttpResponseRedirect('/auth/')

def one_homework_users_view(request, homework_id, todo_id):
    if request.user.is_superuser:
        user = User.objects.get(id=todo_id)
        profile = Profile.objects.get(user=user)
        bg = profile.bg
        first_name = user.first_name
        last_name = user.last_name
        
        form = CheckHomeworkForm()
        if request.method == 'POST':
            form = CheckHomeworkForm(request.POST)
            if(form.is_valid()):
                comment = form.cleaned_data['comment']
                Homework.objects.filter(id=homework_id).update(comment=comment, status=3)
                return render(request, 'one_homework_users.html', {
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'form':form,
          'has_music': profile.has_music,
        })
        return render(request, 'one_homework_users.html', {
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'form':form,
          'has_music': profile.has_music,
        })
    else:
        return HttpResponseRedirect('/auth/')


def one_homework_view(request, homework_id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
           return HttpResponseRedirect('/account/')
        profile = Profile.objects.get(user=request.user)
        bg = profile.bg
        first_name = request.user.first_name
        last_name = request.user.last_name
        homework = Homework.objects.get(id=homework_id)
        form = SendHomeworkForm()
        if request.method == 'POST':
            form = SendHomeworkForm(request.POST, request.FILES)
            if(form.is_valid()):
                answer = form.cleaned_data['answer']
                Homework.objects.filter(id=homework_id).update(answer=answer, status=2)
                return render(request, 'one_homework.html', {
          'bg':bg,
          'first_name':first_name,
          'has_music': profile.has_music,
          'homework':homework,
          'form':form,
        })
        return render(request, 'one_homework.html', {
          'bg':bg,
          'first_name':first_name,
          'has_music': profile.has_music,
          'homework':homework,
          'form':form,
        })
    else:
        return HttpResponseRedirect('/auth/')

def homeworks_user_view(request, todo_id):
    if request.user.is_superuser:
        user = User.objects.get(id=todo_id)
        if user.is_superuser:
           return HttpResponseRedirect('/account/')
        profile = Profile.objects.get(user=user)
        bg = profile.bg
        first_name = user.first_name
        last_name = user.last_name
        not_maked = Homework.objects.filter(user=user, status=1)
        not_checked = Homework.objects.filter(user=user, status=2)
        checked = Homework.objects.filter(user=user, status=3)
        form = AddHomeworkForm()
        if request.method == 'POST':
            form = AddHomeworkForm(request.POST, request.FILES)
            if(form.is_valid()):
                task = form.cleaned_data['task']
                homework = Homework(task=task, user=user)
                homework.save()
                return render(request, 'homework_users.html', {
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'not_maked':not_maked,
          'not_checked':not_checked,
          'checked':checked,
          'form':form,
          'has_music': profile.has_music,
        })
        return render(request, 'homework_users.html', {
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'not_maked':not_maked,
          'not_checked':not_checked,
          'checked':checked,
          'form':form,
          'has_music': profile.has_music,
        })
    else:
        return HttpResponseRedirect('/auth/')


def main_views(request):
    return render(request, 'index.html', {
        
        })


def anketa_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
           return HttpResponseRedirect('/account/')
        profile = Profile.objects.get(user=request.user)
        bg = profile.bg
        form = AnketaForm()
        type_user = profile.type_user
        psyhotype = ""
        if type_user is "":
            typeu = "None"
        else:
            typeu = type_user
        if request.method == 'POST':
            if form.is_valid():
                form = AnketaForm(request.POST)
                one = form.cleaned_data['one']
	        two = form.cleaned_data['two']
	        three = form.cleaned_data['three']
	        four = form.cleaned_data['four']
	        five = form.cleaned_data['five']
	        six = form.cleaned_data['six']
	        seven = form.cleaned_data['seven']
	        eight = form.cleaned_data['eight']
	        nine = form.cleaned_data['nine']
	        ten = form.cleaned_data['ten']
	        eleven = form.cleaned_data['eleven']
	        twelve = form.cleaned_data['twelve']
	        thirteen = form.cleaned_data['thirteen']
	        fourteen = form.cleaned_data['fourteen']
	        fiveteen = form.cleaned_data['fiveteen']
	        sixteen = form.cleaned_data['sixteen']
	        seventeen = form.cleaned_data['seventeen']
	        eighteen = form.cleaned_data['eighteen']
	        nineteen = form.cleaned_data['nineteen']
	        twenty = form.cleaned_data['twenty']
	        twentyone = form.cleaned_data['twentyone']
	        twentytwo = form.cleaned_data['twentytwo']
	        twentythree = form.cleaned_data['twentythree']
                if one is True:
                    psyhotype = 'Astenic'
                elif two is True:
                    psyhotype = 'Senzitive'
                elif three is True:
                    psyhotype = 'Shizoid'
                elif four is True:
                    psyhotype = 'Labil'
                elif five is True:
                    psyhotype = 'Hypertim'
                elif six is True:
                    psyhotype = 'Epiliptoid'
                elif seven is True:
                    psyhotype = 'Isteroid'
                elif eight is True:
                    psyhotype = 'Neustoichivy'
		answer = Answers(one=one, two=two, three=tree, four=four, five=five, six=six, seven=seven, eight=eight, nine=nine, ten=ten, eleven=eleven, twelve=twelve, thirteen=thirteen, fourteen=fourteen, fiveteen=fiveteen, sixteen=sixteen, seventeen=seventeen, eighteen=eighteen, nineteen=nineteen, twenty=twenty, twentyone=twentyone, twentytwo=twentytwo, twentythree=twentythree, user=request.user, type_user=psyhotype)				
                answer.save()
	    else:
		return HttpResponseRedirect('/accoount')
        return render(request, 'anketa.html', {
          'form':form,
          'typeu':typeu,
          'bg':bg,
        })
    else:
        return HttpResponseRedirect('/auth/')



def homework_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
           return HttpResponseRedirect('/account/')
        profile = Profile.objects.get(user=request.user)
        bg = profile.bg
        first_name = request.user.first_name
        last_name = request.user.last_name
        not_maked = Homework.objects.filter(user=request.user, status=1)
        not_checked = Homework.objects.filter(user=request.user, status=2)
        checked = Homework.objects.filter(user=request.user, status=3)
        return render(request, 'homework.html', {
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'not_maked':not_maked,
          'not_checked':not_checked,
          'checked':checked,
          'has_music': profile.has_music,
        })
    else:
        return HttpResponseRedirect('/auth/')

def music_view(request ):
    if request.user.is_authenticated:
        if request.user.is_superuser:
           return HttpResponseRedirect('/account/')
        profile = Profile.objects.get(user=request.user)
        bg = profile.bg
        first_name = request.user.first_name
        last_name = request.user.last_name
        musics = Music.objects.filter(user=request.user)
        return render(request, 'music.html', {
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'musics':musics,
          'has_music': profile.has_music,
        })
    else:
        return HttpResponseRedirect('/auth/')


def music_delete(request, todo_id, music_id):
    if request.user.is_superuser:
        user = User.objects.get(id=todo_id)
        if user.is_superuser:
           return HttpResponseRedirect('/account/')
        music = Music.objects.get(id=music_id)
        music.delete()
        return HttpResponseRedirect('/music_clients/'+ todo_id)
    else:
        return HttpResponseRedirect('/auth/')

def music_user_view(request, todo_id):
    if request.user.is_superuser:
        user = User.objects.get(id=todo_id)
        if user.is_superuser:
           return HttpResponseRedirect('/account/')
        musics = Music.objects.filter(user=user)
        profile = Profile.objects.get(user=user)
        bg = profile.bg
        first_name = user.first_name
        last_name = user.last_name
        form = MusicForm()
        if request.method == 'POST':
            form = MusicForm(request.POST, request.FILES)
            if(form.is_valid()):
                title = form.cleaned_data['title']
                author = form.cleaned_data['author']
                upload = form.cleaned_data['upload']
                music = Music(title=title, author=author, upload=upload, user=user)
                music.save()
                return render(request, 'music_users.html', {
              'bg':bg,
              'first_name':first_name,
              'last_name':last_name, 
              'musics':musics,
              'form':form,
              'user':user,
              'has_music': profile.has_music,
               })
        return render(request, 'music_users.html', {
              'bg':bg,
              'first_name':first_name,
              'last_name':last_name, 
              'musics':musics,
              'form':form,
              'user':user,
              'has_music': profile.has_music,
               })
    else:
        return HttpResponseRedirect('/auth/')

def book_view(request ):
    if request.user.is_authenticated:
        if request.user.is_superuser:
           return HttpResponseRedirect('/account/')
        profile = Profile.objects.get(user=request.user)
        bg = profile.bg
        first_name = request.user.first_name
        last_name = request.user.last_name
        books = Book.objects.filter(user=request.user)
        form = BookForm()
        if request.method == 'POST':
            form = BookForm(request.POST)
            if(form.is_valid()):
                text = form.cleaned_data['text']
                book = Book(user=request.user, text=text)
                book.save()
                return render(request, 'book.html', {
                'bg':bg,
                'first_name':first_name,
                'last_name':last_name,
                'form':form,
                'books':books,
                'has_music': profile.has_music,
                })
        return render(request, 'book.html', {
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'form':form,
          'book':books,
          'has_music': profile.has_music,
        })
    else:
        return HttpResponseRedirect('/auth/')


def chat_view(request ):
    if request.user.is_authenticated:
        if request.user.is_superuser:
           return HttpResponseRedirect('/account/') 
        messages = Chat.objects.filter(user=request.user)
        profile = Profile.objects.get(user=request.user)
        bg = profile.bg
        first_name = request.user.first_name
        last_name = request.user.last_name
        Chat.objects.filter(is_readed=False, type_message=1, user=request.user).update(is_readed=True)
        form = ChatForm()
        if request.method == 'POST':
            form = ChatForm(request.POST)
            if(form.is_valid()):
                type_m = 2
                text = form.cleaned_data['text']
                user = request.user
                message = Chat(type_message=type_m, text=text, user=user, is_readed=False)
                message.save()
                return render(request, 'chat.html', {
                'bg':bg,
                'first_name':first_name,
                'last_name':last_name,
                'form':form,
                'messages':messages,
                'has_music': profile.has_music,
                })
        return render(request, 'chat.html', {
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'form':form,
          'messages':messages,
          'has_music': profile.has_music,
        })
    else:
        return HttpResponseRedirect('/auth/')


def auth_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/account/')
    else:
        form = AuthForm()
        if request.method == 'POST':
            form = AuthForm(request.POST)
            if(form.is_valid()):
               password = form.cleaned_data['password']
               username = form.cleaned_data['username'] 
               user = User.objects.filter(username=username, password=password)
               if user is not None:
                   
                   login(request, user)
                   return HttpResponseRedirect('/account/')
                   
               else:
                   return render(request, 'auth.html', {
                   'form':form,
                   })
            else:
                return render(request, 'auth.html', {
                'form':form,
                })
        else:
            return render(request, 'auth.html', {
    'form':form,
    })

def book_user_view(request, todo_id):
    if request.user.is_superuser:
        user = User.objects.get(id=todo_id)
        if user.is_superuser:
           return HttpResponseRedirect('/account/')
        books = Book.objects.filter(user=user)
        profile = Profile.objects.get(user=user)
        bg = profile.bg
        first_name = user.first_name
        last_name = user.last_name
        return render(request, 'book_users.html', {
              'bg':bg,
              'first_name':first_name,
              'last_name':last_name, 
              'books':books,
              'user':user,
              'has_music': profile.has_music,
               })
    else:
        return HttpResponseRedirect('/auth/')
           

def chat_user_view(request, todo_id):
    if request.user.is_superuser:
        user = User.objects.get(id=todo_id)
        if user.is_superuser:
           return HttpResponseRedirect('/account/') 
        messages = Chat.objects.filter(user=user)
        profile = Profile.objects.get(user=user)
        bg = profile.bg
        first_name = user.first_name
        last_name = user.last_name
        Chat.objects.filter(is_readed=False, type_message=2, user=user).update(is_readed=True)
        form = ChatForm()
        if request.method == 'POST':
            form = ChatForm(request.POST)
            if(form.is_valid()):
                type_m = 1
                text = form.cleaned_data['text']
                message = Chat(type_message=type_m, text=text, user=user)
                message.save()
                return render(request, 'chat_clients.html', {
                'bg':bg,
                'first_name':first_name,
                'last_name':last_name,
                'form':form,
                'messages':messages,
                'user':user,
                'has_music': profile.has_music,
                 })
        return render(request, 'chat_clients.html', {
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'form':form,
          'messages':messages,
          'user':user,
          'has_music': profile.has_music,
        })
    else:
        return HttpResponseRedirect('/auth/')




def view_user(request, todo_id):
    if request.user.is_superuser:
        form = ChangeColorForm()
        user = User.objects.get(id=todo_id)
        if user.is_superuser:
           return HttpResponseRedirect('/account/') 
        profile = Profile.objects.get(user=user)
        bg = profile.bg
        first_name = user.first_name
        last_name = user.last_name
        type_user = profile.type_user
        if type_user == "":
            typeu = "None"
        else:
            typeu = type_user
        number_not_read = Chat.objects.filter(is_readed=False, type_message=2, user=user).count()
        if request.method == 'POST':
            form = ChangeColorForm(request.POST)
            if(form.is_valid()):
               color = form.cleaned_data['bg']
               music = form.cleaned_data['has_music']
               Profile.objects.filter(user=user).update(bg=color, has_music=music)
               return render(request, 'cabinet_users.html', {
               'form':form,
               'bg':bg,
               'first_name':first_name,
               'last_name':last_name,
               'user':user,
               'count':number_not_read,
               'has_music': profile.has_music,
               'typeu':typeu,
               })
        return render(request, 'cabinet_users.html', {
          'form':form,
          'bg':bg,
          'first_name':first_name,
          'last_name':last_name,
          'user':user,
          'count':number_not_read,
          'has_music': profile.has_music,
          'typeu':typeu,
        })
    else:
        return HttpResponseRedirect('/auth/')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/auth")
