from haystack.generic_views import SearchView
from .page_display import per_display

class MySearchView(SearchView):
    """My custom search view."""

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        # context['word'] = '1'
        context['second_line'] = '2'
        num = int(context['page_obj'].paginator.num_pages)
        now = context['page_obj'].number
        # 调用自定义函数，返回要显示的页码的角标
        page_list = per_display(num, now, 9)
        context['page_list'] = page_list
        return context


