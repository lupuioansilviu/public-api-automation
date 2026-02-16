import pytest
from src.api_client import JsonPlaceholderClient

client = JsonPlaceholderClient()

def test_get_posts_status_200():
    r = client.get_posts()
    assert r.status_code == 200

def test_get_posts_returns_list():
    r = client.get_posts()
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "title" in data[0]

@pytest.mark.parametrize("post_id", [1, 2, 3, 50, 100])
def test_get_post_by_id(post_id):
    r = client.get_post(post_id)
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == post_id
    assert "title" in data
    assert "body" in data

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_comments_for_post(post_id):
    r = client.get_comments_for_post(post_id)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert all(item["postId"] == post_id for item in data)