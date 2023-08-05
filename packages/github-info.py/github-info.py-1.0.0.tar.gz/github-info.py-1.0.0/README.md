# GitHub Info
GitHub Info is a small package that provides info fetched from the GitHub API for orgs and users (more in the works).
You can find the methods below.

## Users
Example:
```python
import github_info as github
print(github.users.get("cxllm"))
```
Outcome:
```python
{
    "username": "cxllm",
    "id": 59397232,
    "avatar": "https://avatars.githubusercontent.com/u/59397232?v=4",
    "url": "https://github.com/cxllm",
    "name": "Callum",
    "bio": "A 13 year old TypeScript/Python developer from the UK",
    "location": "United Kingdom",
    "organization": "https://github.com/@SkyNightLabs",
    "website": "cxllm.xyz",
    "twitter": "https://twitter.com/CX11M",
    "email": None,
    "public_repos": 12,
    "public_gists": 0,
    "followers": 19,
    "following": 0,
    "created_at": 1577812053.0,
    "updated_at": 1621186488.0,
    "site_admin": False,
}

```
## Orgs
Example:
```python
import github_info as github
print(github.orgs.get("skynightlabs"))
```
Outcome:
```python
{
    "username": "SkyNightLabs",
    "id": 82262039,
    "avatar": "https://avatars.githubusercontent.com/u/82262039?v=4",
    "url": "https://github.com/SkyNightLabs",
    "name": "SkyNight Labs",
    "description": "The home for your next project",
    "location": "United Kingdom",
    "company": None,
    "website": "https://skynightlabs.com",
    "twitter": "https://twitter.com/SkyNightLabs",
    "email": "hello@skynightlabs.com",
    "public_repos": 0,
    "public_gists": 0,
    "followers": 0,
    "following": 0,
    "created_at": 1618045287.0,
    "updated_at": 1621165797.0,
}

```