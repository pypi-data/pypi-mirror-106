import datetime
import re
from typing import Dict, List, Optional

from keepachangelog._versioning import (
    actual_version,
    guess_unreleased_version,
    to_semantic,
    InvalidSemanticVersion,
)


def is_release(line: str) -> bool:
    return line.startswith("## ")


def add_release(changes: Dict[str, dict], line: str, show_unreleased: bool) -> dict:
    release_line = line[3:].lower().strip(" ")
    # A release is separated by a space between version and release date
    # Release pattern should match lines like: "[0.0.1] - 2020-12-31" or [Unreleased]
    version, release_date = (
        release_line.split(" ", maxsplit=1)
        if " " in release_line
        else (release_line, None)
    )
    if not show_unreleased and not release_date:
        return {}
    version = unlink(version)

    release_details = {"version": version, "release_date": extract_date(release_date)}
    try:
        release_details["semantic_version"] = to_semantic(version)
    except InvalidSemanticVersion:
        pass

    return changes.setdefault(version, release_details)


def unlink(value: str) -> str:
    return value.lstrip("[").rstrip("]")


def extract_date(date: str) -> str:
    if not date:
        return date

    return date.lstrip(" -(").rstrip(" )")


def is_category(line: str) -> bool:
    return line.startswith("### ")


def add_category(release: dict, line: str) -> List[str]:
    category = line[4:].lower().strip(" ")
    return release.setdefault(category, [])


# Link pattern should match lines like: "[1.2.3]: https://github.com/user/project/releases/tag/v0.0.1"
link_pattern = re.compile(r"^\[(.*)\]: (.*)$")


def is_link(line: str) -> bool:
    return link_pattern.fullmatch(line) is not None


def add_information(category: List[str], line: str):
    category.append(line.lstrip(" *-").rstrip(" -"))


def to_dict(changelog_path: str, *, show_unreleased: bool = False) -> Dict[str, dict]:
    changes = {}
    # As URLs can be defined before actual usage, maintain a separate dict
    urls = {}
    with open(changelog_path) as change_log:
        current_release = {}
        category = []
        for line in change_log:
            line = line.strip(" \n")

            if is_release(line):
                current_release = add_release(changes, line, show_unreleased)
            elif is_category(line):
                category = add_category(current_release, line)
            elif is_link(line):
                link_match = link_pattern.fullmatch(line)
                urls[link_match.group(1).lower()] = link_match.group(2)
            elif line:
                add_information(category, line)

    for version, url in urls.items():
        changes.get(version, {})["url"] = url

    return changes


def to_raw_dict(changelog_path: str) -> Dict[str, dict]:
    changes = {}
    # As URLs can be defined before actual usage, maintain a separate dict
    urls = {}
    with open(changelog_path) as change_log:
        current_release = {}
        for line in change_log:
            clean_line = line.strip(" \n")

            if is_release(clean_line):
                current_release = add_release(
                    changes, clean_line, show_unreleased=False
                )
            elif is_link(clean_line):
                link_match = link_pattern.fullmatch(clean_line)
                urls[link_match.group(1).lower()] = link_match.group(2)
            elif clean_line:
                current_release["raw"] = current_release.get("raw", "") + line

    for version, url in urls.items():
        changes.get(version, {})["url"] = url

    return changes


def release(changelog_path: str, new_version: str = None) -> str:
    changelog = to_dict(changelog_path, show_unreleased=True)
    current_version, current_semantic_version = actual_version(changelog)
    if not new_version:
        new_version = guess_unreleased_version(changelog, current_semantic_version)
    release_version(changelog_path, current_version, new_version)
    return new_version


def release_version(
    changelog_path: str, current_version: Optional[str], new_version: str
):
    unreleased_link_pattern = re.compile(r"^\[Unreleased\]: (.*)$", re.DOTALL)
    lines = []
    with open(changelog_path) as change_log:
        for line in change_log.readlines():
            # Move Unreleased section to new version
            if re.fullmatch(r"^## \[Unreleased\].*$", line, re.DOTALL):
                lines.append(line)
                lines.append("\n")
                lines.append(
                    f"## [{new_version}] - {datetime.date.today().isoformat()}\n"
                )
            # Add new version link and update Unreleased link
            elif unreleased_link_pattern.fullmatch(line):
                unreleased_compare_pattern = re.fullmatch(
                    r"^.*/(.*)\.\.\.(\w*).*$", line, re.DOTALL
                )
                # Unreleased link compare previous version to HEAD (unreleased tag)
                if unreleased_compare_pattern:
                    new_unreleased_link = line.replace(current_version, new_version)
                    lines.append(new_unreleased_link)
                    current_tag = unreleased_compare_pattern.group(1)
                    unreleased_tag = unreleased_compare_pattern.group(2)
                    new_tag = current_tag.replace(current_version, new_version)
                    lines.append(
                        line.replace(new_version, current_version)
                        .replace(unreleased_tag, new_tag)
                        .replace("Unreleased", new_version)
                    )
                # Consider that there is no way to know how to create a link to compare versions
                else:
                    lines.append(line)
                    lines.append(line.replace("Unreleased", new_version))
            else:
                lines.append(line)

    with open(changelog_path, "wt") as change_log:
        change_log.writelines(lines)
