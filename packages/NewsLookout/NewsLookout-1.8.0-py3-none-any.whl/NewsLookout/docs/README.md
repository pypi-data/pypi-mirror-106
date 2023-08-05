# NewsLookout Web Scraping Application
The NewsLookout web scraping application for financial events.
 Scalable, modular and configurable multi-threaded python console application.
Extensible by adding NLP and data pre-processing.


## Installation
Create separate directory locations for:
  - the application itself,
  - the data files downloaded from the news websites, and
  - the log files


Install the dependencies using pip:
pip install -r requirements.txt

## Usage

Run the shell script for unix-like operating systems, or use the windows batch command script under windows.

The script can be invoked by scheduling it via cron or Windows Task Scheduler for automated processing.


## Maintenance

The log files will rotate themselves on reaching the set size.

The data directory will need to be monitored since its size could grow quickly due the the data scraped form the web.

