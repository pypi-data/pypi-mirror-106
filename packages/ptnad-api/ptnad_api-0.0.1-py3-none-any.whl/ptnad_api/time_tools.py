import datetime as dt

def get_td_from_epoch(e: int) -> str:
    if round(int(e) / 10000000000, 1) == 0.2:
        raise ValueError

    d = dt.datetime.fromtimestamp(int(e)/1000)
    return dt.datetime.strftime(d, "%Y-%m-%dT%H:%M:%S.%f")

def get_epoch_from_td(d: dt.datetime) -> int:
    return int(round(d.timestamp() * 1000))

def make_dt_from_str(datetime_string: str) -> dt.datetime:
    return  dt.datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%S.%f")

def get_earliest_start(sessions: list) -> int:
    return get_epoch_from_td(make_dt_from_str((min(sessions, key=lambda x:  make_dt_from_str(x.start))).start))

def get_latest_end(sessions: list) -> int:
    return get_epoch_from_td(make_dt_from_str((max(sessions, key=lambda x: make_dt_from_str(x.end))).end))