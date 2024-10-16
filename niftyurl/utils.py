from random import choice
from re import fullmatch
from string import ascii_lowercase, ascii_uppercase, digits

from flask import request

from .models import URLMap


def get_unique_short_id():
    return ''.join(
        choice(
            ascii_uppercase + ascii_lowercase + digits
        ) for _ in range(6))


def validate_custom_id(custom_id):
    return fullmatch(r'[A-Za-z0-9]*', custom_id)


def get_short_url(long_url):
    return (request.base_url +
            URLMap.query.filter_by(
                original=long_url
            ).first().short)


def get_long_url(short_id):
    return URLMap.query.filter_by(
        short=short_id
    ).first().original
