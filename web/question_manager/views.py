from django.shortcuts import render
from question_manager import models


def show_categories(request):
    return render(request, 'question_manager/category_list.html',
                  {'categories': models.Category.objects.all()})
