from django.db.models import Q
from django.shortcuts import render

from feeds.models import Feed


def feed_page(request):

    search = request.GET.get('search')

    feeds = Feed.objects.filter(
        is_published=True
    ).prefetch_related(
        'media_files',
        'tags'
    ).select_related(
        'category',
        'subcategory'
    )

    if search:

        feeds = feeds.filter(

            Q(title__icontains=search) |

            Q(short_description__icontains=search) |

            Q(description__icontains=search) |

            Q(category__name__icontains=search) |

            Q(subcategory__name__icontains=search)

        )

    feeds = feeds.order_by('-created_at')

    context = {
        'feeds': feeds
    }

    return render(
        request,
        'feeds/feed.html',
        context
    )