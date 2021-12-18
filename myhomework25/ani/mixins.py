from django.contrib.auth.mixins import UserPassesTestMixin

class CommentUserCheckMixin(UserPassesTestMixin):
    def test_func(self):
        comment=self.get_object()
        return self.request.user==comment.user