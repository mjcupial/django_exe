from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {
        'insert_content' : "HELLO Im FROM FST APP!"
    }
    return render(request, 'Fst_app/index.html', context=my_dict)