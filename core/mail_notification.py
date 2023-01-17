from django.core.mail import send_mail


def new_story_notification(name: str) -> str:
    send_mail('New voices was sent',
              f'New Voices of Hope was added by {name}',
              'empowermentonlline@gmail.com',
              ['empowermentonlline@gmail.com', ]
              )
    return 'New story -200'


def signing_up_for_an_online_group_notification(email: str) -> str:
    if email != '':
        send_mail('Signing up for an online group',
                  email,
                  'empowermentonlline@gmail.com',
                  ['empowermentonlline@gmail.com', ]
                  )
    return 'New entry to the online group -200'
