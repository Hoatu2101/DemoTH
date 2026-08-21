import pytest
from flask import Flask

from demoapp.app import login_manager, db


def create_test_app():
    app = Flask("DiscountsManagementApp")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["PAGE_SIZE"] = 3
    app.config["TESTING"] = True
    app.secret_key = 'APTX4869'
    db.init_app(app)
    login_manager.init_app(app)

    return app


@pytest.fixture
def test_client(test_app):
    return test_app.test_client()


@pytest.fixture
def test_app():
    app = create_test_app()
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
        db.engine.dispose()


@pytest.fixture
def test_session(test_app):
    yield db.session
    db.session.rollback()
    db.session.remove()

@pytest.fixture
def selenium_driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()