import requests
import json
from datetime import datetime
from pathlib import Path
from logger_config import setup_logger

logger = setup_logger()
now = datetime.now()

try:
    logger.info("Starting flights ingestion process")

    logger.info(f"Sending request to API")
    response = requests.get("https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5")
    response.raise_for_status()

    logger.info("API request completed successfully")

    data = response.json()
    logger.info("Response converted to JSON successfully")

    folder = Path(
        f"data/raw/flights/"
        f"ingestion_date={now.date()}/"
        f"ingestion_time={now.strftime('%H-%M-%S')}"
    )

    folder.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output folder created: {folder}")

    file_path = folder / "flights_raw.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    logger.info(f"Raw JSON saved successfully to: {file_path}")
    logger.info("Flights ingestion process finished successfully")

except Exception as e:
    logger.error(f"Flights ingestion process failed: {e}")
    raise

