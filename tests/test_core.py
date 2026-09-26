from pathlib import Path
from revopslab.demo import generate
from revopslab.pipeline import analyze as pa
from revopslab.campaign import analyze as ca

def test_demo(tmp_path: Path):
    d,e=generate(tmp_path,120,800); p=pa(d); c=ca(e)
    assert p["deals"]==120 and 0<=p["win_rate"]<=1
    assert {"A","B","comparison"} <= set(c)
    assert c["A"]["delivered"]==400
