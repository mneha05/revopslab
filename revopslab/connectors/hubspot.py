from __future__ import annotations
import json, os, urllib.parse, urllib.request

def deals(token: str|None=None, limit: int=100):
    token=token or os.getenv("HUBSPOT_PRIVATE_APP_TOKEN")
    if not token: raise RuntimeError("Set HUBSPOT_PRIVATE_APP_TOKEN")
    props="dealname,amount,dealstage,hs_lastmodifieddate,pipeline"
    url="https://api.hubapi.com/crm/v3/objects/deals?"+urllib.parse.urlencode({"limit":limit,"properties":props})
    req=urllib.request.Request(url,headers={"Authorization":f"Bearer {token}"})
    with urllib.request.urlopen(req,timeout=30) as resp: return json.load(resp)
