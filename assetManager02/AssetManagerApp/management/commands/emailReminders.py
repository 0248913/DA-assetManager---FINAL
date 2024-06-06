from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from AssetManagerApp.models import UserLog

class Command(BaseCommand):
    help = 'Sends email reminders for return dates'

    def handle(self, *args, **options):
        current_time = timezone.now()
        logs_to_remind = UserLog.objects.filter(return_by__gt=current_time)

        for log in logs_to_remind:
            subject = 'Reminder: Return By Date Approaching'
            message = f'Dear {log.user.username},\n\nThis is a reminder that the return by date for log "{log.title}" is approaching.'
            from_email = 'dicksonassetmanager@example.com' 
            to_email = [log.email]

            send_mail(subject, message, from_email, to_email, fail_silently=False)

        self.stdout.write(self.style.SUCCESS('Email reminders sent successfully.'))
