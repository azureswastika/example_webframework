from webframework import Application
from webframework.tools import render
from webframework.views import TemplateView, View

from models import SiteAdmin, Category, Course

app = Application()


class Index(TemplateView):
    route = "/"
    template = "index.html"


class CoursesList(TemplateView):
    route = "/courses"
    template = "courses.html"

    def get(self, request):
        courses = SiteAdmin.get(Course)
        return render(self.template, request, {"courses": courses})


class CreateCourse(View):
    route = "/create_course"
    template = "create_course.html"

    def get(self, request):
        categories = [i.category for i in SiteAdmin.get(Category)]
        return render(self.template, request, {"categories": categories})

    def post(self, request):
        if post := request.get("POST"):
            name = post.name
            type_ = post.type
            category = SiteAdmin.get(Category, category=post.category)[0]
            SiteAdmin.create_course(type_, name, category)
        return self.get(request)


class CategoriesList(TemplateView):
    route = "/categories"
    template = "categories.html"

    def get(self, request):
        categories = SiteAdmin.get(Category)
        return render(self.template, request, {"categories": categories})


class CreateCategory(View):
    route = "/create_category"
    template = "create_category.html"

    def post(self, request):
        if post := request.get("POST"):
            SiteAdmin.create_category(post.name)
        return self.get(request)


def setup():
    SiteAdmin.create_category("Python")
    SiteAdmin.create_category("JavaScript")
    SiteAdmin.create_course("InteractiveCourse", "Python разработка", "Python")
    SiteAdmin.create_course("OfflineCourse", "JavaScript разработка", "JavaScript")


if __name__ == "__main__":
    setup()
    app.start()
