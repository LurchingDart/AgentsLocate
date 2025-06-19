"""Custom exception classes for agent error handling."""

class InvalidURLError(ValueError):
    """Raised when repository URL format is invalid."""
    pass

class InvalidTokenError(ValueError):
    """Raised when GitHub token is invalid or expired."""
    pass

class InsufficientPermissionsError(PermissionError):
    """Raised when token lacks required repository permissions."""
    pass

class RepoTooLargeError(ValueError):
    """Raised when repository exceeds processing size limits."""
    pass

class ProcessingFailedError(Exception):
    """Raised when repository processing fails."""
    pass

class StorageError(Exception):
    """Raised when data storage operations fail."""
    pass

class UnsupportedFormatError(Exception):
    """Raised when repository format is not supported."""
    pass