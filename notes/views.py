from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import NoteModelForm
from .models import Note
# Create your views here.

@login_required(login_url="/accounts/login/")
def note_list_view(request):
    error_message = None
    form = NoteModelForm()
    if request.method == "POST":
        form = NoteModelForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            if '매일' in form.cleaned_data['repeat']:
                note.repaeat = 'daily'
            else:
                note.repeat = ','.join(form.cleaned_data['repeat'])
            print(form.cleaned_data['container'])
            if Note.objects.filter(user=request.user.id, container=form.cleaned_data['container']).exists():
                error_message = "컨테이너가 이미 채워져있습니다."
            else:
                note.save()
                return redirect('note-list')
    else:
        form = NoteModelForm()
        
    to_do_list = Note.objects.filter(user=request.user.id, finished=False)
    finished_list = Note.objects.filter(user=request.user.id, finished=True)
    
    context = {
        'to_do_list': to_do_list,
        'finished_list': finished_list,
        'form': form,
        'error_message': error_message,
    }
    return render(request, "note_list.html", context)

def finish_item(request,id):
    note=get_object_or_404(Note,id=id)
    note.finished=True
    note.save()
    return redirect('note-list')

def recover_item(request,id):
    note=get_object_or_404(Note,id=id)
    note.finished=False
    note.save()
    return redirect('note-list')

def delete_item(request,id):
    note=get_object_or_404(Note,id=id)
    note.delete()
    return redirect('note-list')