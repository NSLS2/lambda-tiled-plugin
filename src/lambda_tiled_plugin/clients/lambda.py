from bluesky_tiled_plugins.clients.bluesky_run import BlueskyRun
from datetime import datetime

from tiled.client.base import JSON_ITEM
from tiled.utils import DictView

def get_in(d, keys, default=None) -> JSON_ITEM:
    cur = d
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur

class LambdaExperiment(BlueskyRun):
    _key_map = {}
    def __repr__(self):
        dt = datetime.fromtimestamp(self.item["attributes"]["metadata"]["start"]["time"])
        return (
            f"<LambdaExperiment "
            f"uid={self.item['attributes']['metadata']['start']['uid']}>"
        )


class MXLambdaExperiment(LambdaExperiment):
    _key_map = {
        "experiment_id": ["uid"],
        "pid": ["scan_id"],
        "facility": ["lambda", "facility"],
        "is_public": ["lambda", "is_public"],
        "protein_name": ["lambda", "protein_name"],
        "technique": ["lambda", "technique"],
        "instrument": ["lambda", "instrument"],
        "creation_date": ["time"],
        "PI": ["lambda.pi"],
        "creation_date_query": ["time"]
    }
    
    @property
    def metadata(self) -> DictView[str, JSON_ITEM]:
        md = self.item["attributes"]["metadata"]["start"]
        lambda_md = {
            k: get_in(md, self._key_map[k]) for k in self._key_map.keys()
        }
        return DictView(lambda_md)

class SAXSLambdaExperiment(LambdaExperiment):
    ...

class CryoEMLambdaExperiment(LambdaExperiment):
    ...
