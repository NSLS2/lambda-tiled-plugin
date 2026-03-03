from dataclasses import replace
from bluesky_tiled_plugins.clients.bluesky_run import BlueskyRun
from bluesky_tiled_plugins.clients.catalog_of_bluesky_runs import CatalogOfBlueskyRuns
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

class CatalogOfLambdaExperiments(CatalogOfBlueskyRuns):
    def _rewrite_query(self, query):
        if hasattr(query, "key"):
            return replace(query, key=_key_map.get(query.key, query.key))
        return query

    def search(self, query):
        return super().search(self._rewrite_query(query))

    def distinct(self, *metadata_keys, structure_families=False, specs=False, counts=False):
        server_keys = tuple(_key_map.get(k, k) for k in metadata_keys)
        return super().distinct(*server_keys, structure_families=structure_families, specs=specs, counts=counts)


class LambdaExperiment(BlueskyRun):
    def __repr__(self):
        dt = datetime.fromtimestamp(self.item["attributes"]["metadata"]["start"]["time"])
        return (
            f"<LambdaExperiment "
            f"uid={self.item['attributes']['metadata']['start']['uid']}>"
        )


class MXLambdaExperiment(LambdaExperiment):
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
