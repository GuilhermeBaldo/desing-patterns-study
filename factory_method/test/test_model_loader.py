from factory_method.model_loader import (
    TorchModelLoader,
    TensorFlowModelLoader,
    TorchModel,
    TensorFlowModel,
)


def test_torch_model_loader_loader():
    model_loader = TorchModelLoader()
    model = model_loader.load("model_path")
    assert isinstance(model, TorchModel)
    assert model.predict("data") == "TorchModel predicted with data"


def test_model_b_loader():
    model_loader = TensorFlowModelLoader()
    model = model_loader.load("model_path")
    assert isinstance(model, TensorFlowModel)
    assert model.predict("data") == "TensorFlowModel predicted with data"
