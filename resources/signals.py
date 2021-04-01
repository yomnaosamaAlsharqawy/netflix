from resources.models import Genres

genres = [
    (1, 'action'),
    (2, 'dramas'),
    (3, 'anime'),
    (4, 'asian'),
    (5, 'crime'),
    (6, 'comedy'),
    (7, 'romance')
]


def init_genres(sender, *args, **kwargs):
    for genre in genres:
        Genres(id=genre[0], genre=genre[1]).save()
