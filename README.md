# base64Encoder

This is a Flask API that takes an image URL and returns base64 encoding of the image.

Created to use [WAGRI PRISM API](https://wagri.net/ja-jp/wagriapi/methodinfo/300b9af0-3053-44cf-a877-6ca85e194989) inside Airtable automation scripts, which doesn't allow the usage of `FileReader.readAsDataUrl()`

`Procfile` is not in use any more since this is now run on Google Compute Engine, not Heroku.