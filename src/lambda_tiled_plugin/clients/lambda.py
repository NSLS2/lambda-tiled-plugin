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
        md = self.item["attributes"]["metadata"]
        lambda_md = {
            "experiment_id": md["start"]["uid"],
            "pid": md["start"]["scan_id"],
            "facility": md["start"]["lambda"]["facility"],
            "is_public": md["start"]["lambda"]["is_public"],
            "protein_name": md["start"]["lambda"]["protein_name"],
            "technique": md["start"]["lambda"]["technique"],
            "instrument": md["start"]["lambda"]["instrument"],
            "creation_date": md["start"]["time"],
            "PI": md["start"]["lambda"]["pi"],
            "creation_date_query": md["start"]["time"]
        }
        return DictView(lambda_md)

class SAXSLambdaExperiment(LambdaExperiment):
    ...

class CryoEMLambdaExperiment(LambdaExperiment):
    ...
