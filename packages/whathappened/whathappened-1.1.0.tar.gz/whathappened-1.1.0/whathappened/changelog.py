import re

from datetime import datetime
from itertools import groupby

# imported to make this module the base module for all external calls to functions
try:
    from whathappened.git_commits import get_commits  # noqa
except ImportError:  # for development use
    from git_commits import get_commits  # noqa

# https://semver.org/spec/v2.0.0.html
semver_regex = re.compile(
    r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)"
    r"(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)


class VersionFormatException(Exception):
    """Raise when a version string cannot be correctly parsed."""

    pass


class Version:
    """
    All the changes committed prior to a new version being released.

    Also includes their attributes, such as breaking, feature, or fix.
    """

    def __init__(self, ref, date):
        self.ref = ref
        self.date = (
            datetime.strptime(date, "%a %b %d %H:%M:%S %Y %z")
            if isinstance(date, str)
            else date
        )  # str input format Wed Apr 22 18:58:54 2020 +0200

        self.breaking = 0
        self.feature = 0
        self.fix = 0

        self.commits = []

    def __repr__(self):
        return (
            f"Version('{self.ref}',"
            f" {self.date},"
            f" breaking={self.breaking},"
            f" feature={self.feature},"
            f" fix={self.fix},"
            f" num_commits={len(self.commits)})"
        )  # pragma: no cover


class Commit:
    """The content and attributes of a single Git commit."""

    commit_regex = re.compile(
        r"(?:(?P<breaking>break(?:ing)?)? ?(?P<type>\w+){1}"
        r" ?(?:\((?P<scope>[^\(\):]+)\))?: (?P<description>.+)|"
        r"(?P<description_alt>.+))",
        flags=re.IGNORECASE,
    )

    group_types = {
        'build': 'build',
        'chore': 'build',
        'ci': 'ci',
        'doc': 'docs',
        'docs': 'docs',
        'feat': 'feat',
        'feature': 'feat',
        'features': 'feat',
        'fix': 'fix',
        'fixes': 'fix',
        'perf': 'perf',
        'performance': 'perf',
        'refac': 'refactor',
        'refactor': 'refactor',
        'revert': 'revert',
        'test': 'test',
    }

    def __init__(self, commit_dict):
        # add items in dictionary to class
        for key, value in commit_dict.items():
            setattr(self, key, value)

        # parse commit title for commit-it-simple parameters
        result = Commit.commit_regex.match(self.title)
        self._breaking = result.group('breaking')
        self._commit_type = result.group('type')
        self._scope = result.group('scope')
        self._description = result.group('description')
        self._description_alt = result.group('description_alt')

    @property
    def breaking(self):
        return self._breaking

    @property
    def commit_type(self):
        """Group equivalent commit types."""
        try:
            return Commit.group_types[self._commit_type]
        except KeyError:
            # if commit type group not specified, return raw commit type
            return self._commit_type if self._commit_type is not None else 'other'

    @property
    def description(self):
        return (
            self._description
            if self._description is not None
            else self._description_alt
        )

    @property
    def scope(self):
        return self._scope

    @property
    def is_breaking(self):
        return self.breaking is not None

    @property
    def is_feature(self):
        return "feat" in self.commit_type.lower()

    @property
    def is_fix(self):
        return "fix" in self.commit_type.lower()

    def __repr__(self):
        return (
            f"Commit({{"
            f"'hash': '{self.hash[:6]}', "
            f"'title': '{self.title}', "
            f"}})"
        )  # pragma: no cover


def _sentence(string):
    """Format a given string in sentence case."""
    try:
        return string[0].upper() + string[1:]
    except IndexError:
        # zero-length string
        return string


def calculate_next(versions, prefix=""):
    """
    Calculate the next version number to be released.

    Based on changes made since the previous version.
    """
    global semver_regex

    try:
        previous = versions[1]
    except IndexError:
        # if no previous version has been found
        return f"{prefix}0.1.0"

    previous_version = previous.ref[len(prefix) :]
    result = semver_regex.match(previous_version)

    # extract version numbers if possible:
    try:
        major, minor, patch = (
            int(result.group('major')),
            int(result.group('minor')),
            int(result.group('patch')),
        )
    except AttributeError:
        raise VersionFormatException(
            f"The version number of '{previous_version}' with prefix='{prefix}' cannot"
            f" be parsed. Please enter the appropriate prefix or use a version string"
            f" like 'X.Y.Z'. See https://semver.org/spec/v2.0.0.html for more details."
        )

    latest_version = versions[0]

    if major == 0:
        # this is a development release and only receives minor and patch increments
        if latest_version.breaking > 0:
            return f"{prefix}{major}.{minor+1}.0"
        elif latest_version.feature > 0 or latest_version.fix > 0:
            return f"{prefix}{major}.{minor}.{patch+1}"
        else:
            # no api changes
            return f"{prefix}{major}.{minor}.{patch}"

    else:
        # this is production release and receives major, minor, and patch increments
        if latest_version.breaking > 0:
            return f"{prefix}{major+1}.0.0"
        elif latest_version.feature > 0:
            return f"{prefix}{major}.{minor+1}.0"
        elif latest_version.fix > 0:
            return f"{prefix}{major}.{minor}.{patch+1}"
        else:
            # no api changes
            return f"{prefix}{major}.{minor}.{patch}"


def _is_valid_version(tag, prefix=""):
    """Check if the provided tag is a version number."""

    tag = tag[len(prefix) :]  # subtring the tag by prefix length
    result = semver_regex.match(tag)

    if result is None:
        return False
    else:
        return True


def compile_log(commits, prefix=""):
    """Iterate though a list of Commits, compiling a list of Versions based on tags."""
    versions = []

    # iterate through commits from latest to earliest

    # group by version
    for commit in commits:
        # make a new version if required
        if len(commit['tags']) > 0 and _is_valid_version(
            commit['tags'][0], prefix=prefix
        ):
            versions.append(Version(ref=commit['tags'][0], date=commit['date']))
        elif len(versions) == 0:
            versions.append(Version(ref='HEAD', date=commit['date']))

        this_commit = Commit(commit)

        # append to current version
        versions[-1].commits.append(this_commit)

        # check if commit is breaking, feature, or fix
        if this_commit.is_breaking:
            versions[-1].breaking += 1

        if this_commit.is_feature:
            versions[-1].feature += 1

        if this_commit.is_fix:
            versions[-1].fix += 1

    # for version in versions:
    #     print(version)

    return versions


def update_latest_version(versions, prefix=""):
    """Update the HEAD reference to show the next semver version."""
    latest_version = versions[0]
    latest_version.ref = calculate_next(versions, prefix=prefix)

    return versions


def override_latest_version(versions, overriding, prefix=""):
    """Update the HEAD reference to show the overriding version."""
    latest_version = versions[0]
    latest_version.ref = f"{prefix}{overriding}"

    return versions


def format_log(versions, emoji=False, development=False):
    """
    Produce a nicely formatted changelog - with emoji too if required.

    Always includes production headings.
    Includes additional headings if development is `True`.
    """
    output = "# Changelog"

    production_headings = {
        'docs': "Docs 📝",
        'feat': "Features ✨",
        'fix': "Fixes 🐛",
        'perf': "Performance ⚡️",
        'refactor': "Refactorings ♻️",
        'other': "Other 🃏",
    }

    development_headings = {
        'ci': "Continuous Integration 🤖",
        'revert': "Reverted ☠️",
        'test': "Testing 🧪",
    }

    if development is True:
        # combine both heading dictionaries into one
        headings = {**production_headings, **development_headings}
    else:
        # use only the production headings
        headings = production_headings

    if not emoji:
        # remove emoji (first two characters) from headings, and strip space character
        headings = {key: heading[:-2].strip() for key, heading in headings.items()}
    else:
        # leave emoji in headings
        pass

    for version in versions:
        output += f"\n\n## {version.ref} ({version.date.isoformat()[:10]})\n"

        # store groupby results as lists
        groups = []
        uniquekeys = []
        data = sorted(version.commits, key=lambda x: x.commit_type[:4])
        for k, g in groupby(data, lambda x: x.commit_type):
            groups.append(list(g))  # Store group iterator as a list
            uniquekeys.append(k)

        headings_in_this_version = [k for k in uniquekeys if k in headings]

        for key, group in zip(uniquekeys, groups):
            if key in headings:

                # check if Other is the only heading in this version
                if key == 'other' and len(headings_in_this_version) == 1:
                    # if it is, it is redundent and should not be displayed
                    output += "\n"
                else:
                    # else display the heading as usual
                    output += f"\n### {headings[key]}\n\n"

                for commit in sorted(group, key=lambda x: f"{x.scope} {x.description}"):
                    scope = f"{commit.scope} - " if commit.scope else ''
                    desc = commit.description.replace('_', '\\_')  # escape underscore
                    desc = _sentence(desc) if len(scope) == 0 else desc
                    breaking = " [BREAKING]" if commit.is_breaking else ''
                    output += f"* {_sentence(scope)}{desc}{breaking}\n"

    return output


def write_log(log, filename):
    with open(filename, 'w') as f:
        f.write(log)
