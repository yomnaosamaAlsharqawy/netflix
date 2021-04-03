from resources.models import Genres, Moods

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


moods = [
    (1, 'action'),
    (2, 'dramas'),
    (3, 'anime'),
    (4, 'asian'),
    (5, 'crime'),
    (6, 'comedy'),
    (7, 'romance')
]


def init_moods(sender, *args, **kwargs):
    for mood in moods:
        Moods(id=mood[0], mood=mood[1]).save()
