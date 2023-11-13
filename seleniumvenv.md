# Selenium venv

#### 1. Install the chromedriver + python pip and venv modules.

> sudo apt install chromium-driver  
> sudo apt install python3-pip python3-venv

#### 2. Create project directory and venv inside

> mkdir $projectdir && cd $projectdir

> python3 -m venv venv

#### 3. Start the venv and install selenium

> source $projectdir/venv/bin/activate  
> pip install selenium

#### 4. Set browser+driver to be used by selenium with selenium-manager

> ./venv/lib/python3.9/site-packages/selenium/webdriver/common/linux/selenium-manager --browser chrome --driver chromedriver --debug --trace

