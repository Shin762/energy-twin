# energy-twin

A small digital twin of an on-site energy system (cogeneration + battery + demand), built step by step while learning Python, optimization, cloud data pipelines and reinforcement learning.

コジェネ・蓄電池・電力需要からなる小さなエネルギーシステムのデジタルツインを、Python・数理最適化・クラウド・強化学習を学びながら自作していくリポジトリです。

> All data in this repository is synthetic or from public sources. No proprietary data is used.
> このリポジトリのデータはすべてダミーまたは公開情報です。

## Roadmap

| Phase | Period | Goal |
|---|---|---|
| 1 | 2026-12 → 2027-02 | Python basics → simulator of cogeneration + battery + demand → rule-based control vs. MILP (PuLP) |
| 2 | 2027-03 → 2027-05 | Stream simulator output to Azure as virtual IoT devices; reproduce the setup with IaC |
| 3 | 2027-06 → 2027-11 | Wrap the twin as a Gymnasium env, train an RL agent, add rule-based safety layer, compare with MILP |
| 4 | 2027-12 → | Physics simulators / physical AI |

## Layout

```
exercises/   # Phase 1 practice problems (week by week)
src/         # the simulator itself (from week 7)
tests/       # pytest
log/         # weekly learning log
```

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
