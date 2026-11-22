"""Week 3-4: dict, class, exceptions, file I/O.

Fill in each part so that `pytest exercises/week03` passes.
Write it yourself. Ask Claude for hints, not answers.

各問の中身を自分で書いて、`pytest exercises/week03` が全部通るようにする。
"""


# ---------------------------------------------------------------- dict
def count_by_status(records):
    """Q1. 機器の状態の記録リストから、状態ごとの台数を数えた辞書を返す。

    records の例:
        [{"unit": "CGS1", "status": "run"},
         {"unit": "CGS2", "status": "stop"},
         {"unit": "CGS3", "status": "run"}]
    返り値の例: {"run": 2, "stop": 1}
    空のリストなら {}。
    """
    raise NotImplementedError


def energy_by_unit(records):
    """Q2. 発電量の記録リストから、機器ごとの合計発電量 [kWh] の辞書を返す。

    records の例:
        [{"unit": "CGS1", "kwh": 100},
         {"unit": "CGS2", "kwh": 50},
         {"unit": "CGS1", "kwh": 30}]
    返り値の例: {"CGS1": 130, "CGS2": 50}
    """
    raise NotImplementedError


# ---------------------------------------------------------------- class
class Battery:
    """Q3. 蓄電池を表すクラス。

    - Battery(capacity_kwh, soc_kwh=0) で作る。
      属性 capacity_kwh（容量）と soc_kwh（今の残量）を持つ。
    - charge(energy_kwh): energy_kwh だけ充電する。ただし容量を超える分は入らない。
      **実際に充電できた量** を返し、soc_kwh を更新する。
    - discharge(energy_kwh): energy_kwh だけ放電する。ただし残量より多くは出せない。
      **実際に放電できた量** を返し、soc_kwh を更新する。
    - soc_ratio(): 残量の割合（0〜1）を返す。

    例:
        b = Battery(100, 50)
        b.charge(30)     -> 30   （残量 80）
        b.charge(30)     -> 20   （残量 100、あふれた 10 は入らない）
        b.discharge(130) -> 100  （残量 0）
    """

    def __init__(self, capacity_kwh, soc_kwh=0):
        raise NotImplementedError

    def charge(self, energy_kwh):
        raise NotImplementedError

    def discharge(self, energy_kwh):
        raise NotImplementedError

    def soc_ratio(self):
        raise NotImplementedError


class Generator:
    """Q4. 発電機を表すクラス。

    - Generator(rated_kw, efficiency) で作る。rated_kw は定格出力、efficiency は発電効率（0〜1）。
    - fuel_input_kw(output_kw): output_kw [kW] を出すのに必要な燃料の入力 [kW] を返す。
      燃料入力 = 出力 ÷ 効率
    - output_kw がマイナス、または定格を超えるときは ValueError を raise する。

    例:
        g = Generator(100, 0.4)
        g.fuel_input_kw(40)   -> 100.0
        g.fuel_input_kw(120)  -> ValueError
    """

    def __init__(self, rated_kw, efficiency):
        raise NotImplementedError

    def fuel_input_kw(self, output_kw):
        raise NotImplementedError


# ---------------------------------------------------------------- file I/O
def read_demand_csv(path):
    """Q5. 需要データの CSV ファイルを読み、demand_kw 列を float のリストで返す。

    ファイルの形（1行目は見出し）:
        hour,demand_kw
        0,320.5
        1,310.0
    返り値の例: [320.5, 310.0]
    ヒント: 標準ライブラリの csv モジュール（csv.DictReader）を調べてみる。
    """
    raise NotImplementedError


# ---------------------------------------------------------------- combined
def simulate_peak_cut(hourly_demand_kw, threshold_kw, battery):
    """Q6. 蓄電池（Q3 の Battery）でピークカットしたときの、各時刻の買電量 [kW] のリストを返す。

    1時刻 = 1時間とする。各時刻で:
      - 需要が threshold_kw を超えたら、超えた分を battery から放電する（残量が足りなければ出せるだけ）
      - 買電量 = 需要 - 実際に放電できた量
    battery の残量は時刻をまたいで減っていく（充電はしない）。

    例: battery = Battery(100, 50)
        simulate_peak_cut([400, 520, 480, 600, 550], 500, battery)
        -> [400, 500, 480, 570, 550]
        （1時目に 20 放電して残り 30、3時目は 100 必要だが 30 しか出せない、4時目は空）
    """
    raise NotImplementedError
