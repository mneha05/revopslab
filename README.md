# RevOpsLab

**Salesforce/HubSpot-ready revenue-operations analytics for CRM pipeline, quota, win/loss, and campaign A/B performance.**

```text
Salesforce SOQL ─┐
                 ├─► normalized deals ─► funnel / pipeline / win-loss / owner metrics
HubSpot CRM API ─┘

campaign events ─► open rate / CTR / conversion / revenue / A-B lift
```

## Run immediately

```bash
pip install -e .
revopslab demo --out demo-output
```

Open `demo-output/index.html`.

The demo uses deterministic synthetic CRM and campaign data, so it works without external credentials.

## CRM connectors

Salesforce connector uses the REST query endpoint and an existing access token:

```bash
export SALESFORCE_INSTANCE_URL=https://your-domain.my.salesforce.com
export SALESFORCE_ACCESS_TOKEN=...
```

HubSpot connector uses a private-app token:

```bash
export HUBSPOT_PRIVATE_APP_TOKEN=...
```

The repo does **not** claim a live production CRM connection unless those credentials are supplied.

## Pipeline analytics

RevOpsLab computes:
- stage counts and dollar pipeline
- weighted active pipeline
- closed-won revenue
- win rate
- average won sales-cycle length
- owner-level pipeline and won revenue

## Campaign execution analytics

The campaign path tracks delivered, opened, clicked, converted, and revenue events by A/B variant and computes:
- open rate
- CTR
- conversion rate
- revenue per delivery
- conversion lift
- two-proportion z-score

## Why this project exists

It connects CRM data to the metrics used by revenue, growth, and go-to-market teams rather than treating CRM as a contact database.
