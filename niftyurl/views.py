from flask import abort, flash, redirect, render_template, request

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import (get_long_url, get_short_url, get_unique_short_id,
                    validate_custom_id)


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        long_url = form.original_link.data
        short_id = form.custom_id.data
        if URLMap.query.filter_by(original=long_url).first():
            return render_template(
                'index.html',
                url_exists=get_short_url(long_url),
                form=form
            )
        if short_id:
            if not validate_custom_id(short_id):
                flash(
                    'Your Nifty URL can only contain '
                    'latin characters and digits.',
                    'form-link'
                )
                return render_template('index.html', form=form)
            if URLMap.query.filter_by(short=short_id).first():
                flash(
                    'Sorry, this name is already taken :(',
                    'form-link'
                )
                return render_template('index.html', form=form)
        else:
            short_id = get_unique_short_id()
            while URLMap.query.filter_by(short=short_id).first():
                short_id = get_unique_short_id()

        urlmap = URLMap(
            original=form.original_link.data,
            short=short_id
        )
        db.session.add(urlmap)
        db.session.commit()
        form.original_link.data = ''
        form.custom_id.data = ''
        return render_template(
            'index.html',
            url_generated=request.base_url + short_id,
            form=form
        )
    return render_template('index.html', form=form)


@app.route('/<short_id>', methods=['GET', 'POST'])
def map_url(short_id):
    if URLMap.query.filter_by(short=short_id).first():
        return redirect(get_long_url(short_id))
    abort(404)
