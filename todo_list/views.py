from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import TodoList, Category


def redirect_view(request):
    return redirect("/category")


class TodoListView(TemplateView):
    template_name = "todo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = TodoList.objects.all()
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if "Add" in request.POST:
            title = request.POST["description"]
            date = request.POST["date"]
            category = request.POST["category_select"]
            TodoList.objects.create(
                title=title,
                content=f"{title} -- {date} {category}",
                due_date=date,
                category=Category.objects.get(name=category)
            )
        elif "Delete" in request.POST:
            checked_list = request.POST.getlist('checkedbox')
            TodoList.objects.filter(id__in=checked_list).delete()
        return redirect("todo")


class CategoryView(TemplateView):
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if "Add" in request.POST:
            name = request.POST["name"]
            Category.objects.create(name=name)
        elif "Delete" in request.POST:
            check = request.POST.getlist('check')
            Category.objects.filter(id__in=check).delete()
        return redirect("category")
