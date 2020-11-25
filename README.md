## Overzicht
## Tender Retail Merchant Connect Multi Log Data Analysis

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c873292c6eae4dc6a1a4ffbb72c52463)](https://app.codacy.com/gh/bd0n4lds/overzicht?utm_source=github.com&utm_medium=referral&utm_content=bd0n4lds/overzicht&utm_campaign=Badge_Grade)
[![Python 3.8](https://img.shields.io/badge/Python-3.8-yellow.svg)](http://www.python.org/download/)
[![Build Status](https://travis-ci.org/bdonalds/overzicht.svg?branch=master)](https://travis-ci.org/bdonalds/overzicht)

## Installation

## Requirements

Required:

## Installation on Ubuntu & Debian

sudo add-apt-repository universe
sudo apt-get install git python3-pip
git clone https://github.com/bdonalds/overzicht
cd overzicht
python3 -m pip install setuptools
python3 -m pip install -r requirements.txt
python3 oz.py
```

## Installation on OSX

```
git clone https://github.com/bdonalds/overzicht
cd overzicht
sudo python3 -m pip install -r requirements.txt
python3 overzicht.py
```

## Running on Docker

```
git clone https://github.com/bdonalds/overzicht
cd overzicht
docker build -t overzicht .
docker run -it --rm overzicht
```