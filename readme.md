To use DVC with the Google Drive folder I've used for experiment data, create an OAuth client in Google Cloud Console and contact me at karimullin.tr@gmail.com so I can share the Drive folder with your account.

Quick local example:

```
dvc remote add -d gdrive gdrive://1V41rlDHL7BvMwoc72ZBLAxfXTcnBd2Hk
dvc remote modify gdrive gdrive_client_id <YOUR_GOOGLE_OAUTH_CLIENT_ID> --local
dvc remote modify gdrive gdrive_client_secret <YOUR_GOOGLE_OAUTH_CLIENT_SECRET> --local
dvc pull -r gdrive
```

If you wish to run your pipelines in Colab, or in any cloud realy, consider generating Oauth credentials and passing it to DVC cache by hand like I do in `scripts/generate_pydrive_cred.py` and `notebooks/colab_run.ipynb`