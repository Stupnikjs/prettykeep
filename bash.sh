# gcloud run deploy prettykeep     --region europe-west9 --source .

python $(pwd)/db/initdb.py 

python ingest.py -p takeout.zip
