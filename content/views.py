from django.shortcuts import render


def view_brand_content(request):
    """ A view that renders the bag contents page """

    return render(request, 'content/content.html')
