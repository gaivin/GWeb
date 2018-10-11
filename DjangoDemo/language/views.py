from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from language.chart import language_rank_chart, history_chart, world_cloud_chart
from language.models import Language, Rating

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def history_view(request):
    return render_chart(history_chart)


def rank_view(request):
    return render_chart(language_rank_chart)


def feature_cloud_view(request):
    return render_chart(world_cloud_chart)


def render_chart(chart_function):
    chart = chart_function()
    context = dict(
        title=chart.page_title,
        myechart=chart.render_embed(),
        host=REMOTE_HOST,
        script_list=chart.get_js_dependencies()
    )
    html = loader.render_to_string(template_name="language_template.html", context=context)
    return HttpResponse(html)


def home_view(request):
    languages = Language.objects.all()
    context = dict(language_list=languages)
    html = loader.render_to_string(template_name="home.html", context=context)
    return HttpResponse(html)
