import time
import django
import os
import datetime
import requests
os.environ['DJANGO_SETTINGS_MODULE'] = 'mail_rules.settings'
django.setup()
from api.models import Email, Mailbox
from exchangelib import Credentials, Account, Configuration, DELEGATE, EWSDateTime
from django.db.utils import IntegrityError
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from api.serializers import EmailSerializer
import pytz

API_ROOT="mailbox-admin.ctg.lu"

#password = "B186o73l7a$145"

#refresh_interval = int(os.getenv("REFRESH_INTERVAL")) or 10
refresh_interval = 10


#account = Account(, credentials=credentials, autodiscover=True)

from datetime import timedelta
#config = Configuration(server=mail_server, credentials=credentials)
start = EWSDateTime.now() - timedelta(days=2)
print(start)
start = pytz.utc.localize(start)
tz = pytz.timezone('Europe/Paris')


def get_emails():
    mailboxes=Mailbox.objects.all()
    
    for mailbox in mailboxes:
        credentials = Credentials(mailbox.username, mailbox.password)
        config = Configuration(server=mailbox.server, credentials=credentials)
        
        account = Account(primary_smtp_address=mailbox.name, config=config,
                    autodiscover=False, access_type=DELEGATE)


        
        for item in account.inbox.filter(datetime_received__gt=start).order_by('-datetime_received')[:20]:
            
            email = Email()
            email.subject = item.subject
            email.sender = item.sender.email_address
            email.received = item.datetime_received
            email.mailbox= mailbox
            email.body = item.body
            try:
                channel_layer = get_channel_layer()
                email.save()
                try:
                    async_to_sync(channel_layer.group_send)("emails", {"type": "new_email_message", "email": EmailSerializer(email).data}) #this is just websocket stuff, can fail if we are not running an asgi server
                except:
                    pass
          
            except IntegrityError:
                #print("already exists, skipping")
                pass
            

          
get_emails()

