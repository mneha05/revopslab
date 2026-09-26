from __future__ import annotations
import argparse,json
from pathlib import Path
from .demo import generate
from .pipeline import analyze as pipeline_analyze
from .campaign import analyze as campaign_analyze
from .report import render

def main():
    p=argparse.ArgumentParser(prog="revopslab"); sub=p.add_subparsers(dest="cmd",required=True)
    d=sub.add_parser("demo"); d.add_argument("--out",type=Path,default=Path("demo-output"))
    a=sub.add_parser("pipeline"); a.add_argument("deals",type=Path)
    c=sub.add_parser("campaign"); c.add_argument("events",type=Path)
    args=p.parse_args()
    if args.cmd=="demo":
        deals,events=generate(args.out); pl=pipeline_analyze(deals); ca=campaign_analyze(events)
        (args.out/"pipeline.json").write_text(json.dumps(pl,indent=2)); (args.out/"campaign.json").write_text(json.dumps(ca,indent=2)); (args.out/"index.html").write_text(render(pl,ca)); print(args.out/"index.html")
    elif args.cmd=="pipeline": print(json.dumps(pipeline_analyze(args.deals),indent=2))
    else: print(json.dumps(campaign_analyze(args.events),indent=2))
