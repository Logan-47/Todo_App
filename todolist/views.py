from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Category

# Index View


def index(request):
    # Query all todos with the object manager
    todos = TodoList.objects.all()

    # Getting all categories with object manager
    categories = Category.objects.all()

    #  If request Method is POST
    if request.method == "POST":
        # if request is to add a task
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            d_l = {
                "Jan":1,
                "Feb":2,
                "Mar":3,
                "apr":4,
                "May":5,
                "Jun":6,
                "Jul":7,
                "Aug":8,
                "Sep":9,
                "Oct":10,
                "Nov":11,
                "Dec":12,

                }
            date = str(request.POST["date"])
            date = date.split()
            new_date = str(date[2])+'-'+str(d_l[str(date[0])])+'-'+str(date[1][:-1])

            category = request.POST["category_select"]

            content = title + " -- " + new_date + " " + category

            todo = TodoList(title=title, content=content, due_date=new_date,
                            category=Category.objects.get(name=category))

            todo.save()

            # main Page
            return redirect("/")
        # if there is a request to delete a Task
        if "taskDelete" in request.POST:

            # To be deleted
            try:
                checked_list = request.POST.getlist("checkedbox")

        
                for todo_id in checked_list:

                    todo = TodoList.objects.get(id=int(todo_id))
                    todo.delete()
            except:
                pass

    return render(request, "todolist/index.html", {"todos": todos, "categories": categories})
