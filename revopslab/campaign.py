from __future__ import annotations
import csv, math
from collections import defaultdict

def analyze(path):
    rows=list(csv.DictReader(open(path,encoding="utf-8")))
    groups=defaultdict(lambda:{"delivered":0,"opened":0,"clicked":0,"converted":0,"revenue":0.0})
    for r in rows:
        g=groups[r["variant"]]
        for k in ["delivered","opened","clicked","converted"]:
            g[k]+=int(r[k])
        g["revenue"]+=float(r["revenue"])
    out={}
    for v,g in groups.items():
        d=max(g["delivered"],1)
        out[v]={
            **g,
            "open_rate":g["opened"]/d,
            "ctr":g["clicked"]/d,
            "conversion_rate":g["converted"]/d,
            "revenue_per_delivery":g["revenue"]/d,
        }
    if "A" in out and "B" in out:
        a,b=out["A"],out["B"]
        p=(a["converted"]+b["converted"])/(a["delivered"]+b["delivered"])
        se=math.sqrt(max(p*(1-p)*(1/a["delivered"]+1/b["delivered"]),1e-12))
        z=(b["conversion_rate"]-a["conversion_rate"])/se
        out["comparison"]={
            "conversion_lift":b["conversion_rate"]-a["conversion_rate"],
            "z_score":z,
            "winner_by_conversion":"B" if b["conversion_rate"]>a["conversion_rate"] else "A",
        }
    return out
