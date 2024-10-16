from datetime import datetime

from flask import request

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(1024), nullable=False)
    short = db.Column(db.String(16))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now())

    def from_api_input(self, data):
        self.original = data['url']
        self.short = data['custom_id']

    def to_api_output(self):
        return dict(
            short_link=request.base_url.replace('api/id/', '') + self.short,
            url=self.original,
        )
