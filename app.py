from webframework import Application
from webframework.views import TemplateView, View

app = Application()


class Index(TemplateView):
    route = "/"
    template = "templates/index.html"


class About(TemplateView):
    route = "/about"
    template = "templates/about.html"


class Contacts(View):
    route = ["/contacts", "/contact"]
    template = "templates/contacts.html"

    def post(self, request):
        if post := request.get("POST"):
            email = post.email
            subject = post.subject
            message = post.message
            print("Письмо от: {}\nТема: {}\nТекст: {}".format(email, subject, message))
        return self.get(request)


if __name__ == "__main__":
    app.start()
