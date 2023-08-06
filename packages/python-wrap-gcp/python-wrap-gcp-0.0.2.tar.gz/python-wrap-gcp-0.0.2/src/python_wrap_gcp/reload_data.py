import inspect, pickle, json
import pandas as pd
from python_wrap_gcp.misc.helpers import log
from python_wrap_gcp.io import get_blob_update_date, emulate_open
from python_wrap_gcp.docs.config import GCPConfig


def load_gcs_file(blob, fmt=None, **kwargs):
    """
    Load GCP blob (file) name with one of supported Python formats: pickle, parquet, json
    :param blob: str, blob name
    :param fmt: str, in case blob name doesn't end with file format
    :return: tuple:
        data: requested file
        data_last_seen: datetime, the latest time blob has been updated
    """
    if blob.endswith(".prq") or blob.endswith('.parquet') or fmt == 'parquet':
        data = pd.read_parquet(blob)
    else:
        as_str = emulate_open(blob, method='rb', from_local=False)
        if blob.endswith(".pkl") or blob.endswith('.pickle') or fmt == 'pickle':
            data = pickle.loads(as_str)
        elif blob.endswith(".json") or fmt == 'json':
            data = json.loads(as_str)
        else:
            raise ValueError("data format not understood")
    prefix = blob.split(GCPConfig.BUCKET)[-1]
    if prefix[0] == '/':  # reduce leading bar
        prefix = prefix[1:]
    data_last_seen = get_blob_update_date(prefix).replace(microsecond=0)
    return data, data_last_seen

def reload(blob, last_time_seen, **kwargs):
    """
    Reload a file from Google Cloud Storage upon file update
    :param blob: str, name of blob
    :param last_time_seen: datetime, time when the last time data seen
    :return: False or tuple:
        data, the last time data seen
    """
    lsh_dict_last_seen = get_blob_update_date(blob.split('/')[-1])
    if (lsh_dict_last_seen - last_time_seen).total_seconds() > GCPConfig.SECONDS_THRESHOLD:
        log(inspect.stack(),
            f"data change detected. Current: {last_time_seen}; available: {lsh_dict_last_seen}", "I")
        data, last_time_seen = load_gcs_file(blob, **kwargs)
        log(inspect.stack(), f"data reloaded", "I")
        return data, last_time_seen
    return False
