from django.test import TestCase
from probability.views import home_view
from probability.forms import InputForm
from probability.functions import get_prob_div, get_prob_it
from decimal import Decimal
from random import randint

# Create your tests here.


class HomePageTest(TestCase):

    def test_probability_div(self):
        """
        Test to check correctness of the division approach
        """
        self.assertEqual(get_prob_div(2), Decimal(0.5))
        self.assertAlmostEqual(get_prob_div(5), Decimal(0.0384), places=10)

    def test_probability_it(self):
        """
        Test to check correctness of the iterative approach
        """
        self.assertEqual(get_prob_it(2), Decimal(0.5))
        self.assertAlmostEqual(get_prob_it(5), Decimal(0.0384), places=10)

    def test_equivalent_approaches(self):
        """
        Test to check if both approaches get to the same result
        """
        n = randint(2, 100)
        self.assertAlmostEqual(get_prob_div(n), get_prob_it(n), places=20)

    def test_uses_home_template(self):
        """
        Test to check if the view return the correct template
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'probability/home.html')

    def test_form_negative_input(self):
        """
        Test form validation for negative inputs
        """
        n = randint(-9999, -1)
        form_data = {'n': str(n)}
        form = InputForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_small_input(self):
        """
        Test form validation for inputs less than 2
        """
        form_data = {'n': '1'}
        form = InputForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {'n': '0'}
        form = InputForm(data=form_data)
        self.assertFalse(form.is_valid())
