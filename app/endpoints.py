from fastapi import APIRouter, Depends
from httpx import AsyncClient

from .schemas import Issue, IssueCreationResult, RepoNames
from .settings import settings

GH_API_URL = "https://api.github.com"

router = APIRouter()


async def get_http_client() -> AsyncClient:
    async with AsyncClient() as client:
        yield client


@router.get("/{username}/repos", response_model=RepoNames, tags=["repos"])
async def get_repo_names(username: str, http_client=Depends(get_http_client)) -> RepoNames:
    resp = await http_client.get(f"{GH_API_URL}/users/{username}/repos")
    resp.raise_for_status()
    repo_names = [repo_data["name"] for repo_data in resp.json()]
    return RepoNames(repos=repo_names)


@router.post("/{username}/{repo_name}/issue", response_model=IssueCreationResult, tags=["issues"])
async def create_issue(
    username: str, repo_name: str, issue: Issue, http_client=Depends(get_http_client)
) -> IssueCreationResult:
    resp = await http_client.post(
        url=f"{GH_API_URL}/repos/{username}/{repo_name}/issues",
        headers={"Authorization": f"Bearer {settings.GITHUB_TOKEN}", "Accept": "application/vnd.github+json"},
        json=issue.dict(),
    )
    return IssueCreationResult(issue_created=resp.status_code == 201)
