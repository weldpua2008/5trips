# DY DevOP challenge - 5trips

## Background story
Due to the danger outside, DY's new CSO (chief security officer) has decreed that the office will be locked down in 10:15 every morning. All of the bus-faring employees are worried that they won't arrive in time, so the newest DevOp was asked to develop a small utility that will allow each employee to specifiy his origin station, and get the 5 LATEST routes that land him at 10:00 or earlier in the bus station near the office.

## App description:
* You have two hardcoded parameters (config file):
  * Time of arrival: `10:00`. All employees are to arrive at the station as late as possible, BEFORE that time
  * Station: `13031` (`בן יהודה/שלום עליכם`). This is the station number according to the metal sign outside AND NOT the internal identifier in the DB.
* For your sake, the application only handles single-line trips. No switchovers.
* The application should allow each employee to specify his origin station and show them the 5 trips that leave their station and arrive at work before the TOA specified in the config file.
* For the employees' sake, you'll only allow them to choose from stations that share a line with the destination station.

## Required output:
* A git repository containing Vagrant configuration that serves the application on port `8080` on the host (see [port redirection](https://docs.vagrantup.com/v2/networking/forwarded_ports.html)).  
    It's supposed to be a fork of this, but if you're feeling really creative you can make your own.
* The repository should contain the application code as well
* The creation of the machine (using `vagrant up`) should end in the application ready - no manual steps
* Reprovisioning the machine (`vagrant provision` for example) will cause the app to serve the latest DB data (see below)
* **bonus**: Have an API with a clean URI (all parameters specified neatly) that returns a YAML file (let's say it's for our mobile app)

## Guidance:
* The Israely mot (משרד התחבורה) publishes a nightly file containing loads of bus data.
    * Source: ftp://gtfs.mot.gov.il/israel-public-transportation.zip
    * Manifest / guide: http://media.mot.gov.il/PDF/HE_TRAFFIC_PUBLIC/GTFS.pdf
* The contained files in aformentioned zip are CSV files. You can load them into mysql (recommended datastore for this) using `load data infile`. See the mysql docs.
* This repo contains a ready-to-go Vagrantfile. You're allowed to modify it (if you don't like Ubuntu, for instance)
* Don't keep the database in the git repo. seriously.

# GLHF
