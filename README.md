PENA's an Entirely New Akinator
===============================

PENA is a game based on Twenty Questions that attempts to determine which character the player is thinking of by asking them a series of questions.

Help for Windows
----------------

### Prerequisites

* Install python-2.7.13.msi

* Install swipl-w32-723.exe

* Execute the command prompt as administrator and run:

		rename "C:\Program Files (x86)\swipl\bin\libswipl.dll" libpl.dll

### Installing pena CLI

* [Open a new command prompt](http://www.howtogeek.com/howto/windows-vista/stupid-geek-tricks-open-a-command-prompt-from-the-desktop-right-click-menu/) in PENA's root directory and run:

		python setup.py install

### Running pena CLI 

* [Open a new command prompt](http://www.howtogeek.com/howto/windows-vista/stupid-geek-tricks-open-a-command-prompt-from-the-desktop-right-click-menu/) in PENA's root directory and run:

		set PATH=C:\Program Files (x86)\swipl\bin;%PATH%
		pena questions_sample.json database.json localhost 5000
