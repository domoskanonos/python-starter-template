import logging
import os

# configure centralized logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
class ProjectConfig:

    logger = logging.getLogger("project")

    @staticmethod
    def _ensure_dir(path: str):
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

    @staticmethod
    def getLogger():
        """Returns the central logger."""
        return ProjectConfig.logger

    @staticmethod
    def getBaseDir():
        return os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..")
        )