HotPizzas
=========

A web application for finding hot pizzas in your area.

#Building/Deploying

Some of the intro stuff is different, but afterwards it should become identical.

##Ubuntu 14.04

- Install dependencies `sudo apt install -y python3 vitualenvwrapper postgresql`
- Make a virtual environment `mkvirtualenv -p /usr/bin/python3 hotpizzas`
- Install git `sudo apt install -y git`

Continue on to the generic section

##OSX 10.9

- Install command line tools `xcode-select --install`
- Install homebrew `ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`
- Install python3.4 `brew install python3`
- Install virtualenvwrapper `brew install pyenv-virtualenvwrapper`
- Make a virtual environment `mkvirtualenv -p /usr/local/bin/python3 hotpizzas` --you may have to do some work to get virtualenv working or the wrapper working
- Install git `brew install git`
- Install postgres.app http://postgresapp.com/
- Make sure your path has postgres in it `PATH="/Applications/Postgres.app/Contents/Versions/9.3/bin:$PATH"`
- Start postgres app

Continue on to the generic section


##Generic

Continue after completing one of the above sections:

- Check this repo out with git clone https://github.com/Automato/HotPizzas.git
- Switch to the directory and activate the hotpizzas virtualenv `workon hotpizzas`
- Get the requirements with pip `pip install -r "./requirements/base.txt"`
- cd to scripts.
- run `./create_dev_db.sh` to build an empty db and "hotpizzas" user in postgres
- run `./runserver.sh` to start a server on localhost port 5000
