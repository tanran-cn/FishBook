# _*_ coding: utf-8 _*_
from flask import Blueprint, render_template

__auther__ = "tanran"
__date__ = "2019/1/29 0:17"

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@web.app_errorhandler(500)
def something_wrong(e):
    return render_template('500.html'), 500


from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish