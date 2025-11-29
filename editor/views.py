from django.http import HttpResponseRedirect 
from django.shortcuts import render
from django.urls import reverse
from discover.models import User
from .models import Graph
from .forms import GraphSaveForm
import json

def index(request):
    if (request.method == "POST"):
        form = GraphSaveForm(request.POST)
        if (form.is_valid()):
            save_file, created = Graph.objects.update_or_create(
                name=form.cleaned_data["name"],
                creator=User.objects.filter(name=form.cleaned_data["user"]).first(),
                defaults={"state": form.cleaned_data["state"]}
            )
            save_file.save()
            context = {
                "user": save_file.creator,
                "state": json.dumps(form.cleaned_data["state"]),
                "name": form.cleaned_data["name"],
                "form": GraphSaveForm()
            }
            return render(request, "editor/editor.html", context)

    context = {
        "user": User.objects.first(),
        "form": GraphSaveForm()
    }
    return render(request, "editor/editor.html", context)