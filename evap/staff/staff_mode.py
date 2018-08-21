import time

from django.contrib import messages
from django.utils.translation import ugettext as _

from evap.settings import STAFF_MODE_TIMEOUT


class StaffModeMiddleware(object):
    """
    Middleware handling the staff mode.

    If too much time has passed, the staff mode will be exited.
    Otherwise, the last request time will be updated.
    """


    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response

    def process_request(self, request):
        if request.session.get('in_staff_mode', False):
            if time.time() <= request.session.get('staff_mode_start_time', 0) + STAFF_MODE_TIMEOUT:
                # just refresh time
                enter_staff_mode(request)
            else:
                exit_staff_mode(request)
                messages.info(request, _("Your staff mode timed out."))


def enter_staff_mode(request):
    request.session['in_staff_mode'] = True
    request.session['staff_mode_start_time'] = time.time()
    request.session.modified = True

def exit_staff_mode(request):
    del request.session['in_staff_mode']
    del request.session['staff_mode_start_time']
    request.session.modified = True