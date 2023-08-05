[![PyPi Package](https://img.shields.io/pypi/dm/google-sheets-to-csv?label=pypi%20downloads)](https://pypi.org/project/google-sheets-to-csv)
# Google sheets to csv

[![google spreadsheet to csv logo](https://assets.gitlab-static.net/uploads/-/system/project/avatar/26368119/logo.png)](https://gitlab.com/micro-entreprise/google-sheets-to-csv "Project home page")


An utility tool to download google sheets to csv files.

## Install

As common python library you can use pip to get the latest stable release

```
pip install google-sheets-to-csv
```

## Usage

The most accurate information will be available using ``gs-to-csv --help``::

```bash
gs-to-csv --help
usage: gs-to-csv [-h] [--service-account-credential-file SERVICE_ACCOUNT] [-f]
                 [-b BUFFER_LINES] [--logging-file LOGGING_FILE]
                 [--logging-level LOGGING_LEVEL]
                 [--logging-format LOGGING_FORMAT]
                 spreadsheet selector directory

Convert google spreadsheet sheets to csv

optional arguments:
  -h, --help            show this help message and exit

Converter options:
  --service-account-credential-file SERVICE_ACCOUNT
                        If you want to use this command in a script without
                        user interractions, you can create a service account
                        from google console:
                        https://developers.google.com/workspace/guides/create-
                        credentials#create_a_service_account and share read
                        access sheets you want to export. (default: None)
  -f, --force           Tell this app tp overwrite existing files if present.
                        (default: False)
  -b BUFFER_LINES, --buffer-lines BUFFER_LINES
                        Maximum number of lines to retreive by http calls.
                        (default: 500)
  spreadsheet           Id of the spreadsheet you want to export to csv.
                        Spreadsheet id is the weird data present in the uri
                        just after `d/`:
                        https://docs.google.com/spreadsheets/d/<the
                        spreadsheet id is here>/
  selector              Sheet selector is a regex expression to match sheets
                        titles. Some examples: - `.*`: would export all sheets
                        - `(abcd)|(efgh)`: would export abcd and efgh sheets
  directory             Output directory with write access where csv files
                        will bewritten.

Logging params:
  --logging-file LOGGING_FILE
                        Logging configuration file, (logging-level and
                        logging-format are ignored if provide) (default: None)
  --logging-level LOGGING_LEVEL
  --logging-format LOGGING_FORMAT

This will create a .csv file per sheet with title match with the regex
expression.
```

## Authentication

There are two ways to let this program access to your google sheets:

* You can provide [google service account](https://developers.google.com/workspace/guides/create-credentials#create_a_service_account)
  credentials with `--service-account-credential-file` option.

* By default script will open your browser that let you authorize (or not)
  readonly access to **all your Google Sheets documents** to this application
  which is running on your computer. An authorization token
  will be saved in your home directory: `.gs-to-csv-token.json`
  (You can control that path using `GS_TO_CSV_TOKEN_FILE_PATH` env
  variable). You can watch following howto on youtube:

  [![Discover on Youtube](https://img.youtube.com/vi/7zacMyv_ooU/0.jpg)](
    https://youtu.be/7zacMyv_ooU
    "Watch on Youtube how to donwload your Google Sheets using oauth authentication")

## Behavior (limitations)

* Google sheets API give a `columnCount` value which is a bit useless
  as we get extra cells. So for convenience this return, for each row,
  the same number of cells as the first line (expected header line!)
  which can result with empty lines or truncated data.

* lines without any values do not return blank line even in the middle
  of the sheet.

* Using user account (with auth flow) has http call rate limit using an
  highest `--buffer-lines` option can counter part a bit this limitation.


## Other solutions

### using wget

- Share your spreadsheet using "Anyone with link can view".
- Then do a wget (or curl) with the download url, you'll find the
  `document_id` and `sheet_id` in the url in your browser

```bash
$ wget --output-file="logs.csv" "https://docs.google.com/spreadsheets/d/<document_id>/export?format=csv&gid=<sheet_id>" -O "downloaded_content.csv"
```

The data will be in the file: downloaded_content.csv

* **pros**:
  - nothing special to install

* **cons**:
  - enable share link access on each spreadsheet
  - get `sheet_id` for any sheets you want to download
  - use one command per sheet to export


## Credits

Logo is derived from [CSV File by Milinda Courey from the Noun Project](
https://thenounproject.com/term/csv/305198/)


## Changelog

* Major version introduce API change
* Minor version change behaviour
* Patch version are about released documentation or refactor
  or hotifx that do not meant to change previous numbers

# Version 0.2

* The `.gs-to-csv-token.json` token file is create in read/write
  only for the current user.

# Version 0.1

* Initial implementation
