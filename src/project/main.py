from project.config import ProjectConfig

logger = ProjectConfig.getLogger()

def main():
    logger.info("start python blueprint")


if __name__ == "__main__":
    main()
