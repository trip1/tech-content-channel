# Script: Zero-downtime Docker Compose without Kubernetes

## Episode brief

- Status: ready-to-build
- Pillar: Server Infrastructure / Homelab
- Format: tutorial explainer
- Source story: HN "Zero-Downtime Deployments with Docker Compose, No Kubernetes Required"
- Target length: 9-12 minutes

## Packaging

### Title options

1. **Zero-downtime deploys without Kubernetes**
2. **You do not need Kubernetes for this**
3. **Docker Compose can deploy without dropping requests**
4. **The small-server deploy trick I actually like**

Best pick: **Zero-downtime deploys without Kubernetes**

### Thumbnail

Visual: Kubernetes logo pushed aside, Docker Compose stack with two app containers labeled blue and green, traffic flowing around a deploy.

Text: **NO K8S**

## Cold open / hook

> Show a tiny app refreshing while a deployment happens in another terminal.

This page is going to keep responding while I deploy a new version.

No Kubernetes. No cluster. No Helm chart archaeology. Just Docker Compose, a reverse proxy, and a deployment pattern that small servers can actually live with.

If you run a homelab, a side project, or a tiny SaaS, this is the deployment problem you eventually hit: you want boring updates without building a miniature platform team.

## Setup

- What we're building: a blue-green style Compose deployment.
- Why it matters: many small apps need reliability, not Kubernetes complexity.
- Constraints: single host, Docker Compose, reverse proxy, health checks, rollback.

## Segment 1: the real problem

A normal Compose deploy often does this:

1. pull new image
2. stop old container
3. start new container
4. hope it boots quickly

That gap might be two seconds. It might be thirty. If the new container fails, the gap becomes an outage.

The fix is simple in concept: start the new version before removing the old one.

## Segment 2: the pattern

The pattern is blue-green deployment.

- Blue is live.
- Green is the new version.
- Bring green up quietly.
- Health check it.
- Move traffic.
- Keep blue around long enough to roll back.

The important part is not the color names. The important part is that traffic only moves after the new version proves it can answer requests.

## Segment 3: what the demo needs

For a real demo, record these pieces:

```bash
docker compose ps
curl -i http://app.local/health
docker compose up -d --scale app_green=1
curl -i http://app-green.local/health
# switch reverse proxy target
curl -i http://app.local/version
```

Show the page refreshing during the switch. The visual proof matters more than the command list.

## Segment 4: where it breaks

Be honest here.

This pattern does not magically solve database migrations. If version two needs a destructive schema change, blue-green gets harder.

It also does not solve multi-host failover. If the server dies, your app is still down.

And it can get messy if your app stores uploads or sessions on local disk.

So the rule is:

- stateless web app: great fit
- app with careful backward-compatible migrations: possible
- app with one-off local state everywhere: fix that first

## Result

By the end, the viewer should see a deploy happen while requests keep working.

That is the payoff. Not theory. The page stays up.

## Wrap

Kubernetes is useful when you actually need what it gives you.

But a lot of small services do not need a cluster. They need a sane deploy pattern, health checks, and a rollback path.

CTA: If you want the follow-up, I will build this into a reusable Compose template with Caddy or Traefik and a one-command rollback.

## Shorts cuts

1. "You do not need Kubernetes to avoid downtime."
2. "The deployment rule: start the new version before killing the old one."
3. "Blue-green is not magic. Database migrations are where it gets real."
