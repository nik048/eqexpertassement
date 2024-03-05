import requests

class GitHubClient():
    def __init__(self):
        self.github_url = "https://api.github.com"

    def get_user_gist(self, user_id: str):
        api_request = f"{self.github_url}/users/{user_id}/gists"
        
        response = requests.get(url=api_request, headers=self._getDefaultHeader())
        
        return response.json()
    
    def _getDefaultHeader(self):
        return {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28", 
        }

github_client = GitHubClient()