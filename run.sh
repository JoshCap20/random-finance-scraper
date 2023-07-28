# MAC OS ONLY (unless you have geckodriver in path)

# VENV SETUP
if [ -d "venv" ]; then
    echo "Virtual environment found, skipping setup"
    source venv/bin/activate
else
    echo "Setting up virtual environment (you'll thank me later)"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

# DOWNLOAD FOLDER SETUP
if [ -d "download" ]; then
    rm -rf download
fi

mkdir download
cd download
DOWNLOAD_PATH=$(pwd)

cd ..

# GECKO DRIVER SETUP
if [ -f "geckodriver" ]; then
    echo "geckodriver exists"
else
    echo "geckodriver does not exist"
    wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-macos.tar.gz
    tar -xvzf geckodriver-v0.33.0-macos.tar.gz
    rm geckodriver-v0.33.0-macos.tar.gz
fi

DRIVER_PATH=$(pwd)/geckodriver

python main.py $DOWNLOAD_PATH $DRIVER_PATH