class ScholarAcquireError(Exception):
    """Base exception for the package."""


class IdentifierError(ScholarAcquireError):
    pass


class ConfigurationError(ScholarAcquireError):
    pass


class NetworkError(ScholarAcquireError):
    pass


class RateLimitError(NetworkError):
    pass


class ProviderError(ScholarAcquireError):
    pass


class NotFoundError(ProviderError):
    pass


class AccessDeniedError(ProviderError):
    pass


class ContentValidationError(ProviderError):
    pass


class RuntimeProtocolError(ScholarAcquireError):
    """Invalid operation in the tool-mediated ChatGPT runtime protocol."""


class FetchRequired(ScholarAcquireError):
    """Raised when the runtime needs an external tool to satisfy an HTTP request."""

    def __init__(self, request):
        super().__init__(f"External fetch required: {request.method} {request.url}")
        self.request = request


class RuntimeUnavailableError(RuntimeProtocolError):
    """Canonical runtime/build evidence is missing; execution must stop."""


class RuntimeIntegrityError(RuntimeProtocolError):
    """Materialized runtime bytes do not match the canonical build manifest."""
