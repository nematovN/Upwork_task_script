# Text Processing Tool (Python & PHP)

## 📌 Upwork Job

[🔗 View This Job on Upwork]([https://www.upwork.com/job-link-here](https://www.upwork.com/jobs/~021927708932488243264?referrer_url_path=%2Fbest-matches%2Fdetails%2F~021927708932488243264))

## 💰 Payment Info

The client offers **$25** for the Python version and **$25** for the PHP version — total of **$50**.


This repository contains both **Python** and **PHP** implementations of a string processing script based on the following requirements:

## 📌 Features

* Read names from `names.txt`
* For each name, generate variations by:

  * ✅ Removing continuous duplicate characters (e.g., `EENDIA` → `ENDIA`)
  * ✅ Removing consecutive vowels or consonants (e.g., `DKIA` → `DK`)
  * ✅ Removing stopwords listed in `stopwords.txt` (e.g., `JPING LIMITED` → `JPING`)
  * ✅ Replacing similar words using `similar.txt` (e.g., `BINGO` → `PINGO`, `PIMGO`, etc.)
  * ✅ Removing vowels to shorten words (e.g., `JAPAN` → `JPN`)
  * ✅ Converting numbers to words and vice versa (e.g., `9English` → `Nine English`, `Five PM` → `5PM`)
* The final output is written to `output.csv` in the format:

  ```
  originalstring,Listofgenerated
  9English,NineEnglish,9nglsh
  BINGO,BNG,PINCO,PIMGO,PINGO
  ...
  ```

## 📁 File Structure

```
project/
├── script.py        # Python version
├── script.php       # PHP version
├── names.txt        # List of input names
├── stopwords.txt    # Words to exclude
├── similar.txt      # Similar word mappings
└── output.csv       # Output with generated variations
```

## ⚙️ How to Run

### Python

```bash
python3 script.py
```

### PHP

```bash
php script.php
```

## 📅 Sample Files Format

### `names.txt`

```
9English
BINGO
JPING LIMITED
```

### `stopwords.txt`

```
LIMITED
PRIVATE
```

### `similar.txt`

```
BINGO=PINGO,PIMGO,PINCO
JPING=JPPING,JPENG
```


---

## 📜 License

This project is built for freelance work and educational purposes.
