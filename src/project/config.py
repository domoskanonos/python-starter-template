import logging
from pathlib import Path


# configure centralized logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class ProjectConfig:
    """Central configuration for the project."""

    logger = logging.getLogger("project")

    @staticmethod
    def _ensure_dir(path: str) -> None:
        """Ensures that a directory exists."""
        Path(path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def get_logger() -> logging.Logger:
        """Returns the central logger."""
        return ProjectConfig.logger

    @staticmethod
    def get_base_dir() -> Path:
        """Returns the base directory of the project."""
        return Path(__file__).resolve().parent.parent.parent
