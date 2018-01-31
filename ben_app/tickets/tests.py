from django.test import TestCase
from tickets.models import Ticket

# Create your tests here.


class TicketTestCase(TestCase):
    def setup(self):
        Ticket.objects.create(title="404", category="Severe", status="Under Review", description="Page not found.")

    def test_to_string(self):
        ticket = Ticket.objects.get(title="404", category="Severe", status="Under Review", description="Page not found.", rating=2)
        self.assertEqual(ticket.__str__(), "404")
