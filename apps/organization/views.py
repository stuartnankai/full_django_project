from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg, CityDict, Teacher
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class OrgView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_cities = CityDict.objects.all()
        hot_orgs  = all_orgs.order_by("-click_num")[:3]
        # Pick the city

        city_id = request.GET.get('city',"")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))


        # Pick the org type

        category = request.GET.get('ct',"")
        if category:
            all_orgs = all_orgs.filter(category = category)


        sort = request.GET.get('sort',"")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")


        # split the page
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 1,request=request)

        orgs = p.page(page)
        org_nums = all_orgs.count()
        teachers = Teacher.objects.all()
        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_cities": all_cities,
            "org_nums": org_nums,
            "city_id":city_id,
            "category":category,
            "hot_orgs":hot_orgs,
            "sort":sort,
        })
