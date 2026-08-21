from test_base import test_app, test_session

def test_add_sample_user(test_session):
    from demoapp.app import add_sample_user, User

    add_sample_user()
    user = test_session.query(User).filter_by(username="1").first()
    assert user is not None
    assert user.username == "1"
    assert user.password == "1"
    assert user.is_active is True