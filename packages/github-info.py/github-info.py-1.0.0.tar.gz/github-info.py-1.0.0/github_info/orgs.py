from requests import get as request
from dateutil import parser


def get(name: str):
    """
    Get info about a user on github

    :param name: The name of the org to find info of
    :return: GitHub org info
    """
    data = request(f"https://api.github.com/orgs/{name}").json()
    try:
        if data["message"]:
            data = None
    except KeyError:
        pass
    if data:
        data = {
            "username": data["login"],
            "id": data["id"],
            "avatar": data["avatar_url"],
            "url": data["html_url"],
            "name": data["name"],
            "description": data["description"],
            "location": data["location"],
            "company": f"https://github.com/{data['company']}"
            if data["company"]
            else None,
            "website": data["blog"],
            "twitter": f"https://twitter.com/{data['twitter_username']}"
            if data["twitter_username"]
            else None,
            "email": data["email"],
            "public_repos": data["public_repos"],
            "public_gists": data["public_gists"],
            "followers": data["followers"],
            "following": data["following"],
            "created_at": parser.parse(data["created_at"]).timestamp(),
            "updated_at": parser.parse(data["updated_at"]).timestamp(),
        }
    return data
