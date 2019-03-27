from django.db.models import Q


def search_query(obj):
    obj = obj.filter(
        Q(name__icontains=query) |
        Q(company__icontains=query)
    ).distinct()

    return obj
