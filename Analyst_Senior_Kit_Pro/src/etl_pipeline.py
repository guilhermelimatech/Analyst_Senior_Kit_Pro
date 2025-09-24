import os, logging, sys
from pathlib import Path
from dotenv import load_dotenv

LOG_PATH = Path("logs/etl.log")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_PATH),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def main():
    load_dotenv()
    try:
        logging.info("Início do pipeline")
        # TODO: ingestão, tratamento, modelagem
        logging.info("Pipeline finalizado com sucesso")
        return 0
    except Exception as e:
        logging.exception("Falha no pipeline: %s", e)
        return 1

if __name__ == "__main__":
    sys.exit(main())
