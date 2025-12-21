To use dvc with my google drive where Ive saved my experiment-related data, create an Oauth client in Google Cloud Platrorm, contact me via karimullin.tr@gmail.com and after I grant you read permissions on the folder run the following:

```
dvc remote add -d gdrive gdrive://1V41rlDHL7BvMwoc72ZBLAxfXTcnBd2Hk
dvc remote modify gdrive gdrive_client_id <YOUR_GOOGLE_OAUTH_CLIENT_ID> --local
dvc remote modify gdrive gdrive_client_secret <YOUR_GOOGLE_OAUTH_CLIENT_SECRET> --local
```