from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, FormView

from tickets.forms import TicketForm, SearchForm
from tickets.models import Ticket


class IndexView(TemplateView):
    template_name = 'tickets/index.html'


class CreateTicket(CreateView):
    template = 'tickets/ticket_form.html'
    model = Ticket
    success_url = '/tickets'
    form_class = TicketForm

    def form_valid(self, form):
        ticket = form.save(commit=False)
        ticket.author = self.request.user
        ticket.save()
        return super(CreateTicket, self).form_valid(form)


class ListTickets(ListView):
    template = 'tickets/ticket_list.html'
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super(ListTickets, self).get_context_data(**kwargs)

        context['tickets'] = Ticket.objects.all()

        return context


class SearchTickets(FormView):
    template_name = 'tickets/ticket_search.html'
    success_url = '/tickets/search/results'
    form_class = SearchForm

    def form_valid(self, form):
        title = form.cleaned_data['title']
        category = form.cleaned_data['category']
        status = form.cleaned_data['status']
        author = form.cleaned_data['author']

        data = {'title': title, 'category': category, 'status': status, 'author': author}

        self.request.session['result'] = data

        return super(SearchTickets, self).form_valid(form)


class SearchResults(ListView):
    template = 'tickets/ticket_list.html'
    model = Ticket

    def search(self):
        search_terms = self.request.session.get('result', None)

        results = []

        if search_terms['author'] != "":
            try:
                user = User.objects.get(username=search_terms['author'])
                results = Ticket.objects.filter(author=user)
            except User.DoesNotExist:
                pass

        if search_terms['title'] != "":
            results = Ticket.objects.filter(title=search_terms['title'])
        if search_terms['category'] != "":
            results = Ticket.objects.filter(category=search_terms['category'])
        if search_terms['status'] != "":
            results = Ticket.objects.filter(status=search_terms['status'])

        # check if results exist
        # Queryset stuff Ticket.objects.filter()

        return results  # result of queryset.

    def get_context_data(self, **kwargs):
        context = super(SearchResults, self).get_context_data(**kwargs)
        context['tickets'] = self.search()

        return context


class DeleteTicket(DeleteView):
    model = Ticket
    success_url = '/tickets'


class EditTicket(UpdateView):
    template = 'tickets/ticket_form.html'
    model = Ticket
    success_url = '/tickets'
    form_class = TicketForm

    def get_form_kwargs(self):
        values = super(EditTicket, self).get_form_kwargs()
        values['instance'] = Ticket.objects.get(id=self.kwargs['pk'])
        return values

    def form_valid(self, form):
        form.save()
        return super(EditTicket, self).form_valid(form)


class StatusBoard(TemplateView):
    template_name = 'tickets/status_board.html'
    model = Ticket

    def query(self):

        query_result = []

        for status in Ticket.STATUS_CHOICES:
            # print(status)
            query = Ticket.objects.filter(status=status[0])
            query_result.append(query)
            # create a dictionary here, or we at-least want to have 3 different context definitions.
            # print(query_result)

        return query_result

    def get_context_data(self, **kwargs):
        context = super(StatusBoard, self).get_context_data(**kwargs)
        context['ticket_list'] = self.query()

        return context




