import requests

class JsonPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        return requests.get(f"{self.BASE_URL}/posts", timeout=15)

    def get_post(self, post_id: int):
        return requests.get(f"{self.BASE_URL}/posts/{post_id}", timeout=15)

    def get_comments_for_post(self, post_id: int):
        return requests.get(f"{self.BASE_URL}/comments", params={"postId": post_id}, timeout=15)