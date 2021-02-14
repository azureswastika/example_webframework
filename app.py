from webframework import Application
from webframework.views import TemplateView, View


class Index(TemplateView):
    route = "/"
    template = "templates/index.html"


class About(TemplateView):
    route = "/about/"
    template = "templates/about.html"


class Contacts(View):
    route = "/contacts/"
    template = "templates/contacts.html"

    def post(self, request):
        email = request.get("email")
        subject = request.get("subject")
        message = request.get("message")
        print("Письмо от: {}\nТема: {}\nТекст: {}".format(email, subject, message))
        return self.get(request)


app = Application()
