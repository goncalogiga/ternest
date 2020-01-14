# Installation

### Selenium

```bash
sudo pip3 install selenium
```

### Firefox


```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
sudo chmod +x /usr/bin/geckodriver
rm geckodriver-v0.23.0-linux64.tar.gz
```

### Google Chrome

...

### Setup

```bash
curl -kL https://raw.githubusercontent.com/goncalogiga/ternest/master/install.sh | bash
```
