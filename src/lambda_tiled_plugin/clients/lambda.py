from tiled.client.container import Container
from datetime import datetime

class LambdaExperiment(Container):
    def __repr__(self):
        dt = datetime.fromtimestamp(self.metadata["start"]["time"])
        return (
            f"<LambdaExperiment "
            f"uid={self.metadata['start']['uid']}"
        )


class MXLambdaExperiment(LambdaExperiment):
    ...

class SAXSLambdaExperiment(LambdaExperiment):
    ...

class CryoEMLambdaExperiment(LambdaExperiment):
    ...
