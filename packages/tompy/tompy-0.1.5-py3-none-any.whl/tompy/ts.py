import datetime
from typing import Optional, Tuple

import numpy as np
import pandas as pd
from sklearn import metrics

###############################################################################
# datetime
###############################################################################


def date(year: int, month: int, day: int) -> datetime.date:
    return datetime.date(year, month, day)


def date_today() -> datetime.date:
    """
    Return the current local date.
    """
    return datetime.date.today()


def date_add(d: datetime.date, days: int) -> datetime.date:
    """
    days range: -999999999 <= days <= 999999999
    """
    return d + datetime.timedelta(days=days)


def date_weekday(d: datetime.date) -> int:
    """
    Return the day of the week as an integer, Monday is 0 and Sunday is 6.
    """
    return d.weekday()


def date_is_weekend(d: datetime.date) -> bool:
    return date_weekday(d) > 4


def date_str(d: datetime.date) -> str:
    """
    Return a string representing the date in ISO 8601 format, YYYY-MM-DD.
    """
    return d.isoformat()


def date_from_str(datestr: str, fmt: str = "%Y-%m-%d") -> datetime.date:
    return datetime_from_str(datestr, fmt=fmt).date()


def datetime_today() -> datetime.datetime:
    """
    Return the current local datetime.
    """
    return datetime.datetime.today()


def datetime_from_str(
    datestr: str, fmt: str = "%Y-%m-%d"
) -> datetime.datetime:
    return datetime.datetime.strptime(datestr, fmt)


###############################################################################
# pandas
###############################################################################


def read_csv(
    fpath: str, index_col: Optional[int] = 0, parse_dates: bool = True
) -> pd.DataFrame:
    return pd.read_csv(fpath, index_col=index_col, parse_dates=parse_dates)


def write_csv(df: pd.DataFrame, fpath: str) -> None:
    df.to_csv(fpath)


def df_drop_weekends(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.index.dayofweek < 5]


def atr(
    df: pd.DataFrame, h: str, l: str, c: str, window: int = 20
) -> pd.DataFrame:
    df1 = pd.DataFrame()
    df1["C1"] = df[c].shift()
    df1["TR1"] = np.abs(df[h] - df[l])
    df1["TR2"] = np.abs(df[h] - df1["C1"])
    df1["TR3"] = np.abs(df[l] - df1["C1"])
    df1["TR"] = df1[["TR1", "TR2", "TR3"]].max(axis=1)
    df1["ATR"] = df1["TR"].rolling(window).mean()
    return df1[["ATR"]]


###############################################################################
# numpy
###############################################################################


def lr_from_sr(sr: np.ndarray) -> np.ndarray:
    """
    ndarray(m, n) -> ndarray(m, n)
    """
    ret = np.log(1.0 + sr)
    assert isinstance(ret, np.ndarray)
    return ret


def lr_to_sr(lr: np.ndarray) -> np.ndarray:
    """
    ndarray(m, n) -> ndarray(m, n)
    """
    ret = np.exp(lr) - 1.0
    assert isinstance(ret, np.ndarray)
    return ret


def crp_sr(sr: np.ndarray, w: np.ndarray) -> np.ndarray:
    """
    ndarray(m, n), ndarray(n,) -> ndarray(m,)
    """
    ret = np.dot(sr, w)
    assert isinstance(ret, np.ndarray)
    return ret


def crp_lr(lr: np.ndarray, w: np.ndarray) -> np.ndarray:
    """
    ndarray(m, n), ndarray(n,) -> ndarray(m,)
    """
    return lr_from_sr(crp_sr(lr_to_sr(lr), w))


def cummulative_lr(
    lr: np.ndarray,
) -> np.ndarray:
    cum_returns = np.cumsum(lr)
    return cum_returns


def annualized_lr_mean(
    lr: np.ndarray,
    ann_factor: int = 252,
) -> float:
    return float(np.mean(lr) * ann_factor)


def annualized_lr_volatility(
    lr: np.ndarray,
    ann_factor: int = 252,
) -> float:
    return float(np.std(lr, ddof=1) * np.sqrt(ann_factor))


def annualized_lr_sharpe(
    lr: np.ndarray,
    ann_factor: int = 252,
) -> float:
    m = annualized_lr_mean(lr, ann_factor=ann_factor)
    s = annualized_lr_volatility(lr, ann_factor=ann_factor)
    if s == 0.0:
        sharpe = 0.0
    else:
        sharpe = m / s
    return float(sharpe)


def mdd_lr(
    lr: np.ndarray,
) -> float:
    cumsum_lr = cummulative_lr(np.concatenate(([0.0], lr)))
    peak = np.maximum.accumulate(cumsum_lr)
    log_dd = cumsum_lr - peak
    log_mdd = np.min(log_dd)
    return float(log_mdd)


def analysis(
    lr: np.ndarray,
    column_name: str,
    ann_factor: int = 252,
) -> pd.DataFrame:
    """
    ndarray(n,)
    """
    n = lr.shape[0]
    cum = cummulative_lr(lr)[-1]
    mean = annualized_lr_mean(lr, ann_factor=ann_factor)
    if n > 1:
        vol = annualized_lr_volatility(lr, ann_factor=ann_factor)
        sharpe = annualized_lr_sharpe(lr, ann_factor=ann_factor)
    else:
        vol = np.nan
        sharpe = np.nan
    mdd = mdd_lr(lr)
    index = [
        "cum_lr",
        "ann_mean_lr",
        "ann_vol_lr",
        "ann_sharpe_lr",
        "mdd_lr",
    ]
    data = [
        cum,
        mean,
        vol,
        sharpe,
        mdd,
    ]
    df = pd.DataFrame(data=data, index=index)
    df.columns = [column_name]
    return df


def analysis_terms(
    lr: np.ndarray,
    verbose: bool = False,
) -> pd.DataFrame:
    """
    ndarray(n,)
    """
    ann_factor = 252
    D = 1
    W = 5
    M = 21
    Y = M * 12
    n = lr.shape[0]
    kvs = {
        "1D": 1 * D,
        "1W": 1 * W,
        "1M": 1 * M,
        "3M": 3 * M,
        "6M": 6 * M,
        "1Y": 1 * Y,
        "3Y": 3 * Y,
        "5Y": 5 * Y,
        "10Y": 10 * Y,
        "ITD": n,
    }

    dfo = pd.DataFrame()
    for key, term in kvs.items():
        if term <= n:
            dfi = analysis(lr[-term:], key, ann_factor=ann_factor)
            dfo = pd.concat([dfo, dfi], axis=1)
        else:
            dfo[key] = np.nan
    if verbose:
        print(dfo)
    return dfo


def confusion_matrix(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    convert_y_true: Optional[float] = 0.0,
    convert_y_pred: Optional[float] = 0.0,
    verbose: bool = False,
) -> Tuple[int, int, int, int]:
    """
    ndarray(n,), ndarray(n,)
    """

    if convert_y_true is not None:
        y_true[y_true >= convert_y_true] = 1.0
        y_true[y_true < convert_y_true] = 0.0
    if convert_y_pred is not None:
        y_pred[y_pred >= convert_y_pred] = 1.0
        y_pred[y_pred < convert_y_pred] = 0.0

    tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()
    if verbose:
        print("confusion_matrix")
        print("tp fn", tp, fn)
        print("fp tn", fp, tn)
        print("all", tp + fn + fp + tn)
        print("accuracy", (tp + tn) / (tp + fn + fp + tn))
        print("tp/(tp+fp)", tp / (tp + fp))
        print("tn/(tn+fn)", tn / (tn + fn))
    return tn, fp, fn, tp
