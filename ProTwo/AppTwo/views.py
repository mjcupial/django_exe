from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("""
    <em>My Second App</em>
    <form action="/action_page.php">
    <label for="fname">First name:</label><br>
    <input type="text" id="fname" name="fname" value="John"><br>
    <label for="lname">Last name:</label><br>
    <input type="text" id="lname" name="lname" value="Doe"><br><br>
    </form> 
    """)

def help(request):
    template_dict = {
        'template_1': "HELP PAGE!"
    }
    return render(request, 'AppTwo/help.html', context=template_dict)
