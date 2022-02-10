from celery import Celery

app = Celery('proj')

app.conf.update(result_expires=3600)

"""
importacion del archivo config desde la raiz del repo
"""
app.config_from_object("proj.celeryconfig")

if __name__ == '__main__':
    app.start()
