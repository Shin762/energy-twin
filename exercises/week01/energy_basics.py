"""Week 1-2: Python basics (variables, if, for, functions).

Fill in each function so that `pytest exercises/week01` passes.
Rules:
- Write it yourself. Ask Claude for hints, not answers.
- Do not use built-in sum() / max() / min() in this week's problems
  (practice for-loops instead).

各関数の中身を自分で書いて、`pytest exercises/week01` が全部通るようにする。
"""


def kw_to_kwh(power_kw, hours):
    """Q1. 出力 power_kw [kW] で hours 時間運転したときの電力量 [kWh] を返す。

    例: kw_to_kwh(100, 2) -> 200
    """
    raise NotImplementedError


def is_demand_over(demand_kw, contract_kw):
    """Q2. 需要 demand_kw が契約電力 contract_kw を「超えた」ら True を返す。

    ちょうど同じときは超えていないので False。
    例: is_demand_over(510, 500) -> True
    """
    raise NotImplementedError


def daily_energy(hourly_kw):
    """Q3. 1時間ごとの電力 [kW] のリストから、合計の電力量 [kWh] を返す。

    sum() を使わず for 文で足し合わせること。空のリストなら 0。
    例: daily_energy([10, 20, 30]) -> 60
    """
    raise NotImplementedError


def peak_hour(hourly_kw):
    """Q4. 1時間ごとの電力のリストで、一番大きい値が出た「時刻（インデックス）」を返す。

    max() を使わないこと。同じ最大値が複数あるときは、最初のものを返す。
    例: peak_hour([10, 50, 30, 50]) -> 1
    """
    raise NotImplementedError


def battery_soc_after(soc_kwh, power_kw, hours, capacity_kwh):
    """Q5. 蓄電池の残量 soc_kwh [kWh] に、power_kw [kW] で hours 時間充放電した後の残量を返す。

    power_kw がプラスなら充電、マイナスなら放電。
    残量は 0 未満にも capacity_kwh 超にもならない（はみ出たら端で止める）。
    例: battery_soc_after(50, 20, 1, 100) -> 70
        battery_soc_after(90, 20, 1, 100) -> 100
    """
    raise NotImplementedError


def peak_cut(hourly_demand_kw, threshold_kw):
    """Q6. 需要が threshold_kw を超えないように、蓄電池が各時刻に放電すべき量 [kW] のリストを返す。

    超えていない時刻は 0。
    例: peak_cut([400, 520, 480, 600], 500) -> [0, 20, 0, 100]
    """
    raise NotImplementedError
