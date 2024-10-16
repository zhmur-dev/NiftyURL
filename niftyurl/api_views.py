from flask import jsonify, request
from http import HTTPStatus

from . import app, db
from .const import SHORT_ID_MAX_LENGTH
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_long_url, get_unique_short_id, validate_custom_id


@app.route('/api/id/', methods=['POST'])
def post_new_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(
            'Request body missing'
        )
    if 'url' not in data:
        raise InvalidAPIUsage(
            '"url" required'
        )
    if URLMap.query.filter_by(original=data['url']).first():
        raise InvalidAPIUsage(
            'Original URL already in database'
        )
    if 'custom_id' in data and data['custom_id'] is not None:
        if (len(data['custom_id']) > SHORT_ID_MAX_LENGTH or
                not validate_custom_id(data['custom_id'])):
            raise InvalidAPIUsage(
                'Invalid short name proposed'
            )
        if URLMap.query.filter_by(short=data['custom_id']).first():
            raise InvalidAPIUsage(
                'Existing short name proposed'
            )
    else:
        data['custom_id'] = get_unique_short_id()
        while URLMap.query.filter_by(short=data['custom_id']).first():
            data['custom_id'] = get_unique_short_id()

    urlmap = URLMap()
    urlmap.from_api_input(data)
    db.session.add(urlmap)
    db.session.commit()

    return jsonify({'short_link': urlmap.to_api_output()['short_link'],
                    'url': urlmap.to_api_output()['url']}), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def map_url_api(short_id):
    if URLMap.query.filter_by(short=short_id).first():
        return {'url': get_long_url(short_id)}, HTTPStatus.OK
    return {'message': 'id not found'}, HTTPStatus.NOT_FOUND
