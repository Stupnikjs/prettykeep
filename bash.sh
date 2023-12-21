# gcloud run deploy de-zoom     --region europe-west9 --source .

python $(pwd)/db/initdb.py 

python ingest.py -p unzipped 
