try:
    from ..cms import views
except ValueError:
    from cms import views


class ItemsListView(views.ListView):
    default_template = "cms/items_list.html"

    def get_queryset(self, **filter_kwargs):
        module_id = self.request.GET.get("module_id")
        if module_id:
            filter_kwargs.update({"module_id": module_id})
        qs = super().get_queryset(**filter_kwargs)
        return qs.distinct()
