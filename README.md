WebSniper Framework
=====================

Description
----------------
WebSniper - Web Application Security Testing Framework, the framework is built under Python language, the framework will act as supplementary tool without needing to launch third-party tools, the framework can be used by testers during their manual assessment. The framework has a metasploit-like-console which testers can run different modules easily.

Contributors
----------------

semprix - Dax Labrador - contributor

shipcod3 - Jay Turla - contributor

godflux - Medz Barao - contributord

Directory structure
-------------------

	[root]
	| - auxiliary
    | - config
    | - data
    | - modules
    |  `- recon
    |  `- discovery
    |  `- exploitation
    | - unittest
    |  `- modules
    |      `- recon
    |	   `- crypto
    |  `- auxiliary
    |  `- exploits
    |
    `- websniper.py (core)
    `- bootstrap.py (dependency)
	`- Changelog
	`- Readme

Python Dependencies
-------------------
Run bootstrap.py to see all necessary python dependencies in order for WebSniper to run properly.

How to contribute?
-------------------
1. (Clone Us) Using git - git clone git@github.com:ROOTCONLabs/websniper.git
2. Check-out the Issues page - https://github.com/ROOTCONLabs/websniper/issues
3. Modify / Hack existing modules
4. Submit new modules
    - create your module at https://github.com/ROOTCONLabs/websniper/pulls
    - Send us a Pull Request
5. Happy hacking!!!

Coding Standards
-------------------
Maven Convention - http://maven.apache.org/developers/conventions/code.html

Python PEP - http://www.python.org/dev/peps/pep-0008/#code-lay-out

Install
------------------

Python2.7 should be present on the system

1. (Install Option #1) Using git - git clone git@github.com:semprix/WebSniper.git
2. (Install Option #2) Downloading master - download at https://github.com/ROOTCONLabs/websniper/archive/master.zip
3. Run bootstrap.py - this will check all python module dependencies
4. Run websniper.py - python websniper.py
