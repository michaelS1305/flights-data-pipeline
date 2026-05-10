from ingest import ingest_flights
from upload_to_blob import upload_run_folder_to_blob

run_folder = ingest_flights()
upload_run_folder_to_blob(run_folder)