from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question



def create_question(question_text, days):
    time = timezone.now().date() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_qustion(self):
        time = timezone.now().date() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_pubkished_recently_with_old_question(self):
        time = timezone.now().date() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now().date() - (datetime.timedelta(days=1) - datetime.timedelta(seconds=1))
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

