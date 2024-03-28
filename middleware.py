from django.shortcuts import redirect

#*****Authentication*****

def auth(view_funtion):
    def wrapped_function(request, *args , **keys):
        if request.user.is_authenticated== 'False':
            return redirect('/login/')
        return view_funtion(request, *args , **keys)
    return wrapped_function
#***GUEST***
def guest(view_funtion):
    def wrapped_function(request, *args , **keys):
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        return view_funtion(request, *args , **keys)
    return wrapped_function