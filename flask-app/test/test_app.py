from flask import url_for, redirect
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
        SECRET_KEY='bA5qzruPYLAyyx5QFNUVCg',
        DEBUG=True,
        WTF_CSRF_ENABLED=False
        )
        return app

