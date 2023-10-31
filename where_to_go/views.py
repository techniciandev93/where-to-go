from django.http import HttpResponse


def show_main_page(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Стартовая</title>
    </head>
    <body>
     <h1>Здесь будет карта</h1>
    </body>
    </html>
    """
    return HttpResponse(html)
