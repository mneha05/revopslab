from __future__ import annotations
import csv, random
from pathlib import Path

STAGES=["Prospecting","Qualification","Proposal","Negotiation","Closed Won","Closed Lost"]

def generate(out: Path, n_deals: int=300, n_events: int=2400):
    rng=random.Random(42)
    out.mkdir(parents=True,exist_ok=True)
    deals=out/"deals.csv"
    events=out/"campaign_events.csv"
    owners=["Avery","Jordan","Morgan","Riley"]
    sources=["organic","paid_search","email","partner"]

    with deals.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["deal_id","owner","stage","amount","days_open","source","won"])
        w.writeheader()
        for i in range(n_deals):
            stage=rng.choices(STAGES,weights=[22,18,16,14,18,12])[0]
            w.writerow({
                "deal_id":f"D{i:04d}",
                "owner":rng.choice(owners),
                "stage":stage,
                "amount":rng.randrange(5000,120000,1000),
                "days_open":rng.randint(2,140),
                "source":rng.choice(sources),
                "won":1 if stage=="Closed Won" else 0,
            })

    with events.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["campaign_id","variant","delivered","opened","clicked","converted","revenue"])
        w.writeheader()
        for i in range(n_events):
            variant="A" if i%2==0 else "B"
            opened=int(rng.random() < (0.34 if variant=="A" else 0.39))
            clicked=int(opened and rng.random() < (0.18 if variant=="A" else 0.22))
            converted=int(clicked and rng.random() < (0.11 if variant=="A" else 0.15))
            w.writerow({
                "campaign_id":"launch-q4",
                "variant":variant,
                "delivered":1,
                "opened":opened,
                "clicked":clicked,
                "converted":converted,
                "revenue":converted*rng.randint(80,280),
            })
    return deals,events
