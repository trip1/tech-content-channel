#!/usr/bin/env python3
"""Scaffold an episode folder from a GitHub issue URL.
Requires an authenticated GitHub CLI (`gh`).
Example: python3 scripts/scaffold-issue-episode.py https://github.com/eslint/eslint/issues/20987
"""
import argparse, json, re, subprocess
from datetime import date
from pathlib import Path
def slugify(text): return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:70]
def parse_issue_url(url):
    match = re.search(r'github\.com/([^/]+/[^/]+)/issues/(\d+)', url)
    if not match: raise SystemExit('Expected URL like https://github.com/owner/repo/issues/123')
    return match.group(1), int(match.group(2))
def gh_json(args):
    proc = subprocess.run(['gh','api'] + args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return json.loads(proc.stdout)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('issue_url')
    parser.add_argument('--focus', default='Software Development / Open Source Debugging')
    args = parser.parse_args()
    repo, number = parse_issue_url(args.issue_url)
    issue = gh_json([f'repos/{repo}/issues/{number}'])
    meta = gh_json([f'repos/{repo}'])
    folder = Path('02-video-pipeline/episodes') / f"{date.today()}-{slugify(repo.split('/')[-1] + '-' + str(number) + '-' + issue['title'])}"
    folder.mkdir(parents=True, exist_ok=True)
    labels = ', '.join(label['name'] for label in issue.get('labels', []))
    (folder/'brief.md').write_text(f"""# Episode Brief: {repo} #{number}\n\n- Status: idea\n- Pillar: {args.focus}\n- Repository: [{repo}]({meta['html_url']})\n- Issue: [#{number} — {issue['title']}]({issue['html_url']})\n- Stars: {meta['stargazers_count']:,}\n- Labels: {labels}\n\n## Hook\n\nCan we reproduce and fix this real open-source issue in about a day?\n\n## First steps\n\n- [ ] Read issue and comments\n- [ ] Clone repo\n- [ ] Read contributing docs\n- [ ] Run baseline tests\n- [ ] Create failing reproduction/test\n""")
    (folder/'issue-context.json').write_text(json.dumps({'repo':repo,'issue':issue,'repo_meta':meta}, indent=2))
    print(folder)
if __name__ == '__main__': main()
