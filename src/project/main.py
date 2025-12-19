"""Main entry point for the project."""

from project.config import ProjectConfig


logger = ProjectConfig.get_logger()


def main() -> None:
    """Start the python blueprint."""
    logger.info("start python blueprint")


if __name__ == "__main__":
    main()
