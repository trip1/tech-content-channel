# Script: Bunny DNS is free now. Should homelab people care?

## Episode brief

- Status: ready-to-script
- Pillar: Homelab / Server Infrastructure
- Format: practical explainer
- Source story: HN "We're making Bunny DNS free"
- Target length: 7-9 minutes

## Packaging

### Title options

1. **Bunny DNS is free. Should you switch?**
2. **Your DNS bill should probably be zero**
3. **Free DNS sounds boring until you run real sites**
4. **The DNS pricing change homelabbers should notice**

Best pick: **Bunny DNS is free. Should you switch?**

### Thumbnail

Visual: DNS query counter spinning, invoice dropping to $0, domain map in the background.

Text: **FREE DNS?**

## Cold open / hook

DNS is one of those things you only think about when it breaks or when the bill gets weird.

Bunny just made DNS free. No query fees. No query limits.

That sounds like a small pricing update. For homelabbers and small builders, it is more interesting than that, because DNS sits right between your domain, your CDN, your tunnels, and the services you expose to the world.

So should you move anything?

## Setup

- What we're explaining: why free managed DNS matters.
- Why it matters: DNS is boring infrastructure, but it affects reliability and cost.
- Viewer outcome: know whether to stay put, test Bunny, or move low-risk domains first.

## Segment 1: why DNS pricing gets annoying

DNS starts free or cheap, then grows teeth when you add traffic, zones, failover, analytics, or a provider that charges per million queries.

Most homelabs will not generate enterprise DNS traffic. But creators and small projects can get surprised when a domain gets popular or when bots hammer records.

A flat "free" offer removes one variable from the bill.

## Segment 2: what free does not mean

Free does not automatically mean best.

Before moving DNS, check:

- reliability history
- global latency
- DNSSEC support
- API quality
- Terraform or automation support
- import/export workflow
- whether you depend on provider-specific records or proxying

If your current DNS is tightly tied to Cloudflare proxy rules, tunnels, or WAF features, DNS pricing is only one piece of the decision.

## Segment 3: homelab test plan

I would not move my most important domain first.

Test plan:

1. Pick a low-risk domain or subdomain.
2. Recreate records in Bunny DNS.
3. Lower TTL before switching nameservers.
4. Switch nameservers.
5. Watch propagation.
6. Test from multiple networks.
7. Keep rollback notes.

On screen, show:

```bash
dig example.com @1.1.1.1
dig example.com @8.8.8.8
dig +trace example.com
```

## Segment 4: when I would switch

Good fit:

- simple domains
- static sites
- homelab services
- projects already using Bunny CDN
- cost-sensitive side projects

Maybe not:

- heavily automated Cloudflare setups
- domains using advanced security rules
- business-critical domains with no migration window

## Result

This is not a hype video. DNS is plumbing.

But free, solid plumbing is worth noticing.

## Wrap

My take: test it with a boring domain first. If the API and reliability fit your workflow, then consider moving more.

CTA: Comment with your current DNS provider and the one feature that would stop you from switching.

## Shorts cuts

1. "DNS bills should be boring. Bunny just made theirs zero."
2. "Do not move your most important domain first. Test a boring one."
3. "Free DNS is not enough if your WAF, tunnels, and automation live somewhere else."
