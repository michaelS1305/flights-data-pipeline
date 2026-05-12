import json
import pandas as pd

from datetime import datetime
from pathlib import Path

from logger_config import setup_logger


logger = setup_logger()


def build_processed_flights():

    now = datetime.now()

    try:
        logger.info("Starting flights processing pipeline")

        raw_file_path = Path("data/raw/flights")

        logger.info("Searching for latest raw flights file")

        latest_file = sorted(
            raw_file_path.rglob("flights_raw.json")
        )[-1]

        logger.info(f"Latest raw file found: {latest_file}")

        with open(latest_file, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        logger.info("Raw JSON loaded successfully")

        records = raw_data["result"]["records"]

        logger.info(f"Extracted {len(records)} records from raw JSON")

        df_raw = pd.DataFrame(records)

        logger.info(
            f"Created raw DataFrame with shape: {df_raw.shape}"
        )

        column_mapping = {
            "CHOPER": "airline_code",
            "CHFLTN": "flight_number",
            "CHOPERD": "airline_name",
            "CHSTOL": "scheduled_time",
            "CHPTOL": "actual_time",
            "CHAORD": "arrival_departure",
            "CHLOC1": "airport_code",
            "CHLOC1D": "airport_name",
            "CHLOC1T": "destination_name_english",
            "CHLOCCT": "country_code",
            "CHTERM": "terminal",
            "CHCINT": "check_in_counter_range",
            "CHCKZN": "check_in_zone",
            "CHRMINE": "status_code"
        }

        logger.info("Renaming columns")

        df_renamed = df_raw.rename(columns=column_mapping)

        column_order = [
            "airline_code",
            "flight_number",
            "airline_name",
            "scheduled_time",
            "actual_time",
            "arrival_departure",
            "airport_code",
            "airport_name",
            "destination_name_english",
            "country_code",
            "terminal",
            "check_in_counter_range",
            "check_in_zone",
            "status_code"
        ]

        logger.info("Selecting and ordering columns")

        df_ordered = df_renamed[column_order].copy()

        logger.info("Casting datetime columns")

        df_ordered["scheduled_time"] = pd.to_datetime(
            df_ordered["scheduled_time"],
            errors="coerce"
        )

        df_ordered["actual_time"] = pd.to_datetime(
            df_ordered["actual_time"],
            errors="coerce"
        )

        logger.info("Adding processing metadata")

        df_ordered["processed_at"] = pd.Timestamp.now()

        logger.info("Casting terminal column to string")

        df_ordered["terminal"] = (
            df_ordered["terminal"].astype(str)
        )

        text_cols = [
            "airline_code",
            "flight_number",
            "airline_name",
            "arrival_departure",
            "airport_code",
            "airport_name",
            "destination_name_english",
            "country_code",
            "check_in_counter_range",
            "check_in_zone",
            "status_code"
        ]

        logger.info("Standardizing text columns")

        for col in text_cols:

            df_ordered[col] = (
                df_ordered[col]
                .str.strip()
                .str.upper()
            )

        before_dedup = len(df_ordered)

        logger.info("Removing duplicate rows")

        df_ordered = df_ordered.drop_duplicates()

        after_dedup = len(df_ordered)

        logger.info(
            f"Removed {before_dedup - after_dedup} duplicate rows"
        )

        processed_folder = Path(
            f"data/processed/flights/"
            f"processed_date={now.date()}/"
            f"processed_time={now.strftime('%H-%M-%S')}"
        )

        logger.info(
            f"Creating processed output folder: {processed_folder}"
        )

        processed_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        output_path = (
            processed_folder / "flights_processed.parquet"
        )

        logger.info(
            f"Saving processed parquet file to: {output_path}"
        )

        df_ordered.to_parquet(
            output_path,
            index=False
        )

        logger.info(
            "Flights processing pipeline completed successfully"
        )

        return output_path

    except Exception as e:

        logger.error(
            f"Flights processing pipeline failed: {e}"
        )

        raise

build_processed_flights()