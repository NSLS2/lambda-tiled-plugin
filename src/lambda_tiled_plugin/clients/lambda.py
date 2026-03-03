from bluesky_tiled_plugins.clients.bluesky_run import BlueskyRun
from datetime import datetime

from tiled.client.base import JSON_ITEM
from tiled.utils import DictView

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
        lambda_md = {
            "experiment_id": self.item["attributes"]["metadata"]["start"]["uid"],
            "pid": self.item["attributes"]["metadata"]["start"]["scan_id"],
            "facility": self.item["attributes"]["metadata"]["start"]["lambda"]["facility"],
            "is_public": self.item["attributes"]["metadata"]["start"]["lambda"]["is_public"],
            "protein_name": self.item["attributes"]["metadata"]["start"]["lambda"]["protein_name"],
            "technique": self.item["attributes"]["metadata"]["start"]["lambda"]["technique"],
            "instrument": self.item["attributes"]["metadata"]["start"]["lambda"]["instrument"],
            "creation_date": self.item["attributes"]["metadata"]["start"]["time"],
            "PI": self.item["attributes"]["metadata"]["start"]["lambda"]["pi"],
            "creation_date_query": self.item["attributes"]["metadata"]["start"]["time"]
        }
        return DictView(lambda_md)

class SAXSLambdaExperiment(LambdaExperiment):
    ...

class CryoEMLambdaExperiment(LambdaExperiment):
    ...
