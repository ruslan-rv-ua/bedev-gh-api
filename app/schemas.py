from typing import List

from pydantic import BaseModel


class RepoNames(BaseModel):
    repos: List[str]


class IssueCreationResult(BaseModel):
    issue_created: bool


class Issue(BaseModel):
    title: str
    body: str = ""
