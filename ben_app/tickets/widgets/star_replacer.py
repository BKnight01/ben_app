from django.forms.widgets import NumberInput
from django.template import loader
from django.utils.safestring import mark_safe


class StarReplacerWidget(NumberInput):
    template_name = 'tickets\widgets\star_replacer.html'

    # This is a constructor
    # Override
    def __init__(self, *args, **kwargs):
        super(StarReplacerWidget, self).__init__(*args, **kwargs)

    # Override
    def render(self, name, value, attrs=None, **kwargs):
        count = 5
        context = {'name': name, 'value': value, 'count': count, 'n': range(count)}
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)
