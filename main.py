from pathlib import Path

from ingest import ingest_flights
from transform_flights import build_processed_flights
from blob_storage import upload_file_to_blob


raw_file_path = ingest_flights()

raw_blob_name = raw_file_path.relative_to("data/raw").as_posix()

upload_file_to_blob(
    local_file_path=raw_file_path,
    blob_name=raw_blob_name
)

processed_file_path = build_processed_flights()

processed_blob_name = processed_file_path.relative_to("data").as_posix()

upload_file_to_blob(
    local_file_path=processed_file_path,
    blob_name=processed_blob_name
)
