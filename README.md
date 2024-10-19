# Sarica 

![](https://files.catbox.moe/vpr3cb.png)

Select a random video from a random subscription from your Pornhub account.

It will work on Termux.

# Features
- command-line interface
- open the link on your default browser

# Installation
### First Method
```bash
git clone --depth 1 --branch main <REPO URL> sarica
pip install ./sarica
```
### Second Method
```bash
pip install git+<REPO URL>@main
```

# Configuration
**WARNING: Only Linux is supported as of now. Why? Because I am lazy.**

Rename `config.yaml.example` to `config.yaml`, move it to `~/.config/sarica/`, then update the credentials in that file.

# Command-Line Arguments
```
usage: __main__.py [-h] [-S SEED]

Select a random video from a random Pornhub subscription.

options:
  -h, --help            show this help message and exit
  -S SEED, --seed SEED  Set randomizer seed. Defaults to 'None'.
```
