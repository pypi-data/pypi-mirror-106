"""Base action for bronotes."""
import os
from bronotes.config import cfg
from fuzzy_match import match
from datetime import datetime
from git import Repo
from git.exc import InvalidGitRepositoryError
from git.exc import GitCommandError
from abc import ABC, abstractmethod


class BronoteAction(ABC):
    """Base bronote action."""

    @property
    @abstractmethod
    def action(self):
        """Name of the action for cli reference."""
        pass

    @property
    @abstractmethod
    def arguments(self):
        """Allow arguments for the action."""
        pass

    @property
    @abstractmethod
    def flags(self):
        """Allow flags for the action."""
        pass

    def __init__(self, config=False):
        """Construct the action."""
        if config:
            self.cfg = config
        else:
            self.cfg = cfg

    @abstractmethod
    def init(self):
        """Construct the child."""
        pass

    @abstractmethod
    def process(self, **kwargs):
        """Process the action."""
        pass

    def set_attributes(self, args):
        """Set attributes based on arguments and flags.

        Parameters:
            args: Arguments given from CLI
        """
        for flag in self.flags.keys():
            flagname = flag[2:]
            try:
                setattr(self, flagname, getattr(args, flagname))
            except AttributeError:
                setattr(self, flagname, None)

        for argument in self.arguments.keys():
            try:
                setattr(self, argument, getattr(args, argument))
            except AttributeError:
                setattr(self, argument, None)

    @classmethod
    def add_arguments(cls, subparser):
        """Add an actions arguments to a subparser."""
        for argument in cls.arguments.keys():
            argdict = cls.arguments[argument]

            subparser.add_argument(
                argument,
                help=argdict['help'],
                nargs=argdict['nargs']
            ).complete = {
                "zsh": f"_files -W {cfg.notes_dir}",
            }

    @classmethod
    def add_flags(cls, subparser):
        """Add an actions flags to a subparser."""
        for flag in cls.flags.keys():
            flagdict = cls.flags[flag]

            subparser.add_argument(
                flagdict['short'],
                flag,
                action=flagdict['action'],
                help=flagdict['help']
            )

    @classmethod
    def add_subparser(cls, subparsers):
        """Add a subparser based on a actions arguments and flags."""
        subparser = subparsers.add_parser(
            cls.action, help=cls.__doc__)

        subparser.set_defaults(action=cls)
        cls.add_arguments(subparser)
        cls.add_flags(subparser)

    def sync(self):
        """Sync with git."""
        try:
            repo = Repo(self.cfg.notes_dir)
        except InvalidGitRepositoryError:
            return 'Not a git repo. Set one up first, use the git \
action to execute git commands in your notes directory and set things up. \
Auto-syncing can be enable through the set action.'

        try:
            if not repo.remotes:
                return 'No remotes configured, go figure it out.'
        except AttributeError:
            return 'Git is not set up correctly.'

        repo.git.remote('update')
        commits_behind = len([i for i in repo.iter_commits(
            'master..origin/master')])

        if commits_behind > 0:
            pull_result = repo.git.pull('origin', 'master')
            print(pull_result)

        if repo.is_dirty() or repo.untracked_files:
            self.push(repo)
            return 'Synced with git.'

        return 'No pushing needed.'

    def push(self, repo):
        """Push to git."""
        git = repo.git
        git.add('--all')
        try:
            print(git.commit('-m', f"Automatic sync {datetime.now()}"))
        except GitCommandError:
            pass
        git.push('origin', 'master')

    def find_note(self, filename):
        """Find best match of a note traversing from the base folder.

        Excludes .git directory.
        """
        choices = {}
        exclude_dirs = ['.git']

        for root, dirs, files in os.walk(self.cfg.notes_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for file in files:
                choices[file] = f"{root}/{file}"

        (result, match_index) = match.extractOne(
            filename,
            [i for i in choices.keys()]
        )

        return choices[result]
