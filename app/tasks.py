from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def send_notification(description):
    pass
# timestamp = datetime.utcnow()
# notification = Notification(description=description, timestamp=timestamp)
# # db.session.add(notification)
# # db.session.commit()
# print("Услуга забронирована", description, timestamp)
