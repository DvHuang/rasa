from rasa.shared.exceptions import RasaException


class TFLayerConfigException(RasaException):
    """Raised when wrong parameters are passed to tensorflow layers."""


class TFModelConfigException(RasaException):
    """Raised when wrong parameters are passed to `RasaModel`s."""
