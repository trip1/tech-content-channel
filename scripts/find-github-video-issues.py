#!/usr/bin/env python3
"""Find GitHub issues that may make good one-day troubleshooting videos.
Requires an authenticated GitHub CLI (`gh`).
Example: python3 scripts/find-github-video-issues.py --limit 20
"""
import argparse, json, re, subprocess, sys
DEFAULT_REPOS = ['storybookjs/storybook','TanStack/query','eslint/eslint','vitejs/vite','remix-run/react-router','caddyserver/caddy','keploy/keploy','kubernetes/minikube','go-gitea/gitea','syncthing/syncthing','detekt/detekt','coil-kt/coil','ktorio/ktor','square/okhttp','JetBrains/compose-multiplatform']
HELPFUL_LABELS = re.compile(r'good|beginner|first|easy|help wanted|up for grabs|accepted|triage', re.I)
DETAIL_WORDS = re.compile(r'repro|steps|expected|actual|screenshot|stack|trace|proposal|implementation|motivation|solution|test', re.I)
def gh_json(args):
    proc = subprocess.run(['gh','api'] + args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode: raise RuntimeError(proc.stderr or proc.stdout)
    return json.loads(proc.stdout)
def score_issue(issue, meta):
    labels = [label['name'] for label in issue.get('labels', [])]
    body = issue.get('body') or ''
    label_text = ' '.join(labels)
    score = 0
    if HELPFUL_LABELS.search(label_text): score += 50
    if re.search(r'bug|enhancement|feature|rule|autofix|testing', label_text, re.I): score += 15
    if len(body) > 800: score += 20
    if len(body) > 1600: score += 10
    if 1 <= issue.get('comments', 0) <= 15: score += 10
    if not issue.get('assignees'): score += 5
    if meta.get('stargazers_count', 0) > 5000: score += 5
    if DETAIL_WORDS.search(body): score += 15
    return score
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', action='append', help='owner/name repo to scan; can be repeated')
    parser.add_argument('--limit', type=int, default=30)
    parser.add_argument('--min-score', type=int, default=60)
    args = parser.parse_args()
    candidates = []
    for repo in args.repo or DEFAULT_REPOS:
        meta = gh_json([f'repos/{repo}'])
        issues = gh_json(['-X','GET',f'repos/{repo}/issues','-f','state=open','-f','per_page=100','-f','sort=updated','-f','direction=desc'])
        for issue in issues:
            if 'pull_request' in issue: continue
            score = score_issue(issue, meta)
            if score < args.min_score: continue
            candidates.append({'score':score,'repo':repo,'stars':meta.get('stargazers_count'),'language':meta.get('language'),'number':issue['number'],'title':issue['title'],'url':issue['html_url'],'labels':[label['name'] for label in issue.get('labels', [])],'comments':issue.get('comments',0),'body_len':len(issue.get('body') or ''),'updated_at':issue.get('updated_at')})
    candidates.sort(key=lambda item: (item['score'], item['stars'] or 0, item['body_len']), reverse=True)
    print(json.dumps(candidates[:args.limit], indent=2))
if __name__ == '__main__':
    try: main()
    except Exception as exc:
        print(f'error: {exc}', file=sys.stderr); sys.exit(1)
