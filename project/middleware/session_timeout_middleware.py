# import time
# from django.shortcuts import redirect
# from django.conf import settings

# class SessionTimeoutMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             last_activity = request.session.get('last_activity')
#             current_time = time.time()

#             if last_activity and (current_time - last_activity) > settings.SESSION_TIMEOUT:
#                 return redirect('login')
            
#             request.session['last_activity'] = current_time
        
#         response = self.get_response(request)
#         return response

        