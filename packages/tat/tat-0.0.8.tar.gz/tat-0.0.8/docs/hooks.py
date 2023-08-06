import os
import io
import re
import hashlib
from pbr.git import _iter_log_oneline, _iter_changelog, _run_git_command


def sha256_file(file):
    sha256 = hashlib.sha256()
    with open(file, 'rb') as f:
        sha256.update(f.read())
    return sha256


def generate_changelog(*args, **kwargs):
    changelog = _iter_log_oneline(git_dir='.git')
    if changelog:
        changelog = _iter_changelog(changelog)
    if not changelog:
        return

    new_changelog = os.path.join('docs', 'changelog.md')

    new_content = bytearray()
    for _, content in changelog:
        new_content += content.encode('utf-8')

    if os.path.isfile(new_changelog) and hashlib.sha256(new_content).digest() == sha256_file(new_changelog).digest():
        return

    with io.open(new_changelog, "wb") as changelog_file:
        changelog_file.write(new_content)


def generate_authors(*args, **kwargs):
    old_authors = 'AUTHORS.in'
    new_authors = os.path.join('docs', 'authors.md')
    if os.path.isfile(new_authors) and not os.access(new_authors, os.W_OK):
        # If there's already an AUTHORS file and it's not writable, just use it
        return

    ignore_emails = '((jenkins|zuul)@review|infra@lists|jenkins@openstack)'
    git_dir = '.git'
    authors = []

    # don't include jenkins email address in AUTHORS file
    git_log_cmd = ['log', '--format=%aN <%aE>']
    authors += _run_git_command(git_log_cmd, git_dir).split('\n')
    authors = [a for a in authors if not re.search(ignore_emails, a)]

    # get all co-authors from commit messages
    co_authors_out = _run_git_command('log', git_dir)
    co_authors = re.findall('Co-authored-by:.+', co_authors_out,
                            re.MULTILINE)
    co_authors = [signed.split(":", 1)[1].strip()
                  for signed in co_authors if signed]

    authors += co_authors
    authors = sorted(set(authors))

    new_authors_str = bytearray()

    if os.path.exists(old_authors):
        with open(old_authors, "rb") as old_authors_fh:
            new_authors_str += old_authors_fh.read()
    new_authors_str += (('\n'.join(authors) + '\n').encode('utf-8'))

    if new_authors and hashlib.sha256(new_authors_str).digest() == sha256_file(new_authors).digest():
        return

    with open(new_authors, 'wb') as f:
        f.write(new_authors_str)


def on_pre_build(*args, **kwargs):
    generate_changelog()
    generate_authors()
