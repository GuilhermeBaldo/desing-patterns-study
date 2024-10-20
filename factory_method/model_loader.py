from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def predict(self, data): ...


class TorchModel(Model):
    def predict(self, data):
        return f"TorchModel predicted with {data}"


class TensorFlowModel(Model):
    def predict(self, data):
        return f"TensorFlowModel predicted with {data}"


class ModelLoader(ABC):
    @abstractmethod
    def load(self, model_path) -> Model: ...


class TorchModelLoader(ModelLoader):
    def load(self, model_path) -> Model:
        return TorchModel()


class TensorFlowModelLoader(ModelLoader):
    def load(self, model_path) -> Model:
        return TensorFlowModel()
