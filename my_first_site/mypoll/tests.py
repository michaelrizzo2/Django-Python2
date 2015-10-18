import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question
from django.core.urlresolvers import reverse

# Create your tests here.

class QuestionMethodTests(TestCase):
    #was published recently should return false for future questions

    def test_was_published_recently_with_future_question(self):
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        time=timezone.now()-datetime.timedelta(days=30)
        old_question=Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        time=timezone.now()-datetime.timedelta(hours=1)
        recent_question=Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(),True)

def create_question(question_text,days):


    """
        Creates a question with the given `question_text` published the given
        number of `days` offset to now (negative for questions published
        in the past, positive for questions that have yet to be published).
    """

    time=timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)

class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no question exists , an appropiate message should be displayed
        """
        response=self.client.get(reverse('mypoll:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])
