from commitizen.cz.conventional_commits.conventional_commits import (
    ConventionalCommitsCz,
)
from commitizen.question import CzQuestion


class ConventionalPlusCz(ConventionalCommitsCz):
    def questions(self) -> list[CzQuestion]:
        questions = super().questions()
        for q in questions:
            if q.get("name") == "prefix":
                q["choices"].extend(  # ty: ignore[invalid-key]
                    (
                        {
                            "value": "chore",
                            "name": "chore: Other changes that don't modify src or test files",
                        },
                        {
                            "value": "revert",
                            "name": "revert: Reverts a previous commit",
                        },
                    )  # ty: ignore[invalid-argument-type]
                )
        return questions
