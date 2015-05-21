from django.utils import timezone
from users.models import User


class UpdateUserTempMeta(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        if request.user.is_authenticated():
            User.objects.filter(id=request.user.id).update(last_activity=timezone.now(),
                                                           latest_ip=request.META['REMOTE_ADDR'])