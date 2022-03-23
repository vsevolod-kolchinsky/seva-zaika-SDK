class BaseLotrSdkError(Exception):
    """Base class for errors"""


class EntityImproperlyConfigured(BaseLotrSdkError):
    """Entity class is not configured properly"""


class LotrApiError(BaseLotrSdkError):
    """API Error"""

    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.status_code = status_code
