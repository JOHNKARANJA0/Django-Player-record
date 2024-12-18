from django.shortcuts import render, redirect
from MyAPP.forms import PLAYERFORM
from MyAPP.models import PLAYER


def ply(request):
    if request.method == 'POST':
        form = PLAYERFORM(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = PLAYERFORM()
    return render(request, "index.html", {'form': form})
def show(request):
    players = PLAYER.objects.all()
    return render(request, "show.html", {'players': players})
def edit(request, id):
    player = PLAYER.objects.get(id=id)
    return render(request, 'edit.html', {'player': player})
def update(request, id):
    player = PLAYER.objects.get(id=id)
    form = PLAYERFORM(request.POST, instance=player)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'player': player})
def delete(request, id):
    player =  PLAYER.objects.get(id=id)
    player.delete()
    return redirect('/show')

            

