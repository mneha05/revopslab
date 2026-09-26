from __future__ import annotations
import csv
from collections import defaultdict

ORDER=["Prospecting","Qualification","Proposal","Negotiation","Closed Won","Closed Lost"]

def analyze(path):
    rows=list(csv.DictReader(open(path,encoding="utf-8")))
    total=sum(float(r["amount"]) for r in rows)
    won=[r for r in rows if r["stage"]=="Closed Won"]
    lost=[r for r in rows if r["stage"]=="Closed Lost"]
    active=[r for r in rows if not r["stage"].startswith("Closed")]
    by_stage=defaultdict(lambda:{"count":0,"amount":0.0})
    for r in rows:
        by_stage[r["stage"]]["count"]+=1
        by_stage[r["stage"]]["amount"]+=float(r["amount"])
    closed=len(won)+len(lost)
    win_rate=len(won)/closed if closed else 0.0
    avg_cycle=sum(float(r["days_open"]) for r in won)/len(won) if won else 0.0
    weighted=sum(float(r["amount"])*{"Prospecting":.1,"Qualification":.25,"Proposal":.5,"Negotiation":.75}.get(r["stage"],0) for r in active)
    owner=defaultdict(lambda:{"pipeline":0.0,"won":0.0,"deals":0})
    for r in rows:
        o=owner[r["owner"]]
        o["deals"]+=1
        o["pipeline"]+=float(r["amount"])
        if r["stage"]=="Closed Won":
            o["won"]+=float(r["amount"])
    return {
        "deals":len(rows),
        "gross_pipeline":total,
        "active_weighted_pipeline":weighted,
        "closed_won_revenue":sum(float(r["amount"]) for r in won),
        "win_rate":win_rate,
        "avg_won_cycle_days":avg_cycle,
        "by_stage":dict(by_stage),
        "by_owner":dict(owner),
    }
