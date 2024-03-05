import pytest

from fastapi import FastAPI
from src.routers import github_gist
from fastapi.testclient import TestClient
from unittest.mock import call
import json
from src.main import app
# app = FastAPI()
# app.include_router(github_gist.router)

client = TestClient(app)

class TestGithubGist:
    
    def test_get_gist_for_valid_user(self, mock_github_api, expected_response):
        testUser = "octocat"
        uri = f"/users/{testUser}"
        mock_github_api.get_user_gist.return_value = expected_response
        
        response = client.get(uri)
        
        assert response.status_code == 200
        assert response.json() == expected_response

    @pytest.fixture
    def mock_github_api(self, mocker):
        return mocker.patch("src.routers.github_gist.github_client")
    
    @pytest.fixture
    def expected_response(self):
        return [
                    {
                        "url": "https://api.github.com/gists/6cad326836d38bd3a7ae",
                        "forks_url": "https://api.github.com/gists/6cad326836d38bd3a7ae/forks",
                        "commits_url": "https://api.github.com/gists/6cad326836d38bd3a7ae/commits",
                        "id": "6cad326836d38bd3a7ae",
                        "node_id": "MDQ6R2lzdDZjYWQzMjY4MzZkMzhiZDNhN2Fl",
                        "git_pull_url": "https://gist.github.com/6cad326836d38bd3a7ae.git",
                        "git_push_url": "https://gist.github.com/6cad326836d38bd3a7ae.git",
                        "html_url": "https://gist.github.com/octocat/6cad326836d38bd3a7ae",
                        "files": {
                            "hello_world.rb": {
                                "filename": "hello_world.rb",
                                "type": "application/x-ruby",
                                "language": "Ruby",
                                "raw_url": "https://gist.githubusercontent.com/octocat/6cad326836d38bd3a7ae/raw/db9c55113504e46fa076e7df3a04ce592e2e86d8/hello_world.rb",
                                "size": 175
                            }
                        },
                        "public": True,
                        "created_at": "2014-10-01T16:19:34Z",
                        "updated_at": "2024-01-14T06:42:08Z",
                        "description": "Hello world!",
                        "comments": 281,
                        "user": None,
                        "comments_url": "https://api.github.com/gists/6cad326836d38bd3a7ae/comments",
                        "owner": {
                            "login": "octocat",
                            "id": 583231,
                            "node_id": "MDQ6VXNlcjU4MzIzMQ==",
                            "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4",
                            "gravatar_id": "",
                            "url": "https://api.github.com/users/octocat",
                            "html_url": "https://github.com/octocat",
                            "followers_url": "https://api.github.com/users/octocat/followers",
                            "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                            "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                            "organizations_url": "https://api.github.com/users/octocat/orgs",
                            "repos_url": "https://api.github.com/users/octocat/repos",
                            "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                            "received_events_url": "https://api.github.com/users/octocat/received_events",
                            "type": "User",
                            "site_admin": False
                        },
                        "truncated": False
                    }
                ]