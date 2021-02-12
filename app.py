from webframework import Application, BaseView


class Index(BaseView):
    route = "/"
    template = "index.html"


class About(BaseView):
    route = "/about/"
    template = "about.html"


app = Application()
