# Screenshots Generator

`screenshotsgenerator.sh`

Version 0.1

This script will create screenshots using Screen.rip API and a url list used as input to generate the screen grabs. It will then save them in the /tmp folder, more precisely in `/tmp/screenshots<YYYYmmddhhmm>`.

Version 0.1 needs two files as input:
1. The `tokenkey` file, where the token that allows the API call to go through is stored
2. The `IRUK17Top100.csv` file, where the ID, URL code and URL itself live in

**Without these files the script doesn't work**

## Usage

Copy the .zip to your server
```
scp screenshot.zip username@[servername]:/[serverpath]
```
This will allow you to copy the .zip into the /serverpath in the server you have access to.

To have the script running in a scheduled manner `cron` is the perfect tool.

### Configure cron to run this script daily


```
crontab -e
```

```
* * * * * *
| | | | | |
| | | | | +-- Year              (range: 1900-3000)
| | | | +---- Day of the Week   (range: 1-7, 1 standing for Monday)
| | | +------ Month of the Year (range: 1-12)
| | +-------- Day of the Month  (range: 1-31)
| +---------- Hour              (range: 0-23)
+------------ Minute            (range: 0-59)
```

So in order to have the script running every weekday at 8am the configuration would be

```
0 8 * * 1-5 /[pathtoscript]/screenshotsgenerator.sh
```

---
### Notes

- Please note that now the name of the .csv file is hardcode in the script, being it currently called `IRUK17Top100.csv`.

### Future possible functionalities

- Access the mysql db and generate the file that will be consumed without needing it to be manually added to the folder
- Save the images to Amazon S3 
