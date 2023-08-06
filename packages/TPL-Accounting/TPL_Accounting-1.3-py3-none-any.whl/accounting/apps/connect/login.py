# PYTHON IMPORTS
import logging
from sys import _getframe
# DJANGO IMPORTS
# from django.contrib import messages
from django.contrib.auth import get_user_model, views
from django.shortcuts import redirect
# from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
# CORE IMPORTS


logger = logging.getLogger(__name__)
USER_MODEL = get_user_model()


class LoginView(views.LoginView):
    """Overriding Django LoginView from django.contrib.auth.views"""

    @staticmethod
    def get_redirect_message(request):
        """Returns a message to user when redirected"""
        return _(
            f"You are already logged in as {request.user}. "
            f"Redirected you to Index page. "
            f"Please logout if you wish to log in as a new user."
        )

    def get(self, request, *args, **kwargs):
        """overriding GET method"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"{request.user} is authenticated: {request.user.is_authenticated}"
        )
        # redirect authenticated users
        if request.user.is_authenticated:
            return redirect(
                request=request, message=self.get_redirect_message(request)
            )

        # if user is not authenticated, proceed with LoginView
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """overriding POST method"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Performing form validation..."
        )
        # redirect authenticated users
        if request.user.is_authenticated:
            return redirect(
                request=request, message=self.get_redirect_message(request)
            )

        # if user is not authenticated, proceed with LoginView
        return super().post(request, *args, **kwargs)
