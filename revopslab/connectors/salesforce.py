from __future__ import annotations
import json, os, urllib.parse, urllib.request

def query(soql: str, instance_url: str|None=None, access_token: str|None=None, api_version: str="v61.0"):
    instance_url=instance_url or os.getenv("SALESFORCE_INSTANCE_URL")
    access_token=access_token or os.getenv("SALESFORCE_ACCESS_TOKEN")
    if not instance_url or not access_token:
        raise RuntimeError("Set SALESFORCE_INSTANCE_URL and SALESFORCE_ACCESS_TOKEN")
    url=f"{instance_url.rstrip('/')}/services/data/{api_version}/query/?q={urllib.parse.quote(soql)}"
    req=urllib.request.Request(url,headers={"Authorization":f"Bearer {access_token}"})
    with urllib.request.urlopen(req,timeout=30) as resp: return json.load(resp)
