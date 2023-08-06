# Mark-II-sniffer
Small piece of software running on-board (Omega2S+) sniffers to gather sensors data and operate some board control.

### MQTT publisher: live data
Running the **pub_main.py** starts a publisher client that will continually read the board's data via Modbus and send it to the _.../system_data_ MQTT topic. 
The Modbus communication is done over Serial by default, but can be configured for TCP clients.

### MQTT subscriber: update automation
Running the **sub_main.py** starts a subscriber client that listens on the _.../update_ topic. When receiving a message on this topic, 
the _update_sniffer.sh_ script will be called, executing a git pull and rebooting the module.

## Setup on the Omega2S+

#### 1. Configure the system timezone
We want to make sure that the onion is configured at the correct timezone for the data to be accurate.

- List all the timezones with ```onion time list```
- Scroll through the available zones and copy the line that represents your
- Set the correct timezone with ```onion time set <timezone> <timezone string>```
- For more details, you can follow [this tutorial](https://onion.io/2bt-onion-config-script/).

#### 2. Install basic packages
- Install **python3 light** with ```opkg install python3-light```
- Install **git** with ```opkg install git git-http ca-bundle```
- Install **pip** for python3 with ```opkg install python3-pip```
 

#### 3. Clone the repository and install requirements
The automation requires the omega to do a _git pull_ when receiving an update. By using a personnal access token to clone the repository at first, 
we don't have to authenticate with git for subsequent pulls. Anyways, since 2020 [using password-based authentication for Git is deprecated](https://github.blog/2020-07-30-token-authentication-requirements-for-api-and-git-operations/), and using a PAT is more secure. 
For more information, see [Creating a personal access token.](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

- Go to the root directory of the onion
- Clone the repository with ```git clone https://ac7856efdf646a40d5d7b7a891e842b361b41b6d@github.com/Positive-Degree/Mark-II-sniffer.git```
- In the project folder, install the required libraries with ```pip3 install -r requirements.txt```
- If the app has to communicate modbus over TCP, install [**pymodbus**](https://pymodbus.readthedocs.io/en/latest/readme.html#summary) with ```pip3 install -U pymodbus```

#### 4. Configure the app with the appropriate info
Some environment variables have to be configured into your environment for the application to work.
(They can also be added in a .env file for development).

The necessary variables are listed in the .env.example file and can be sourced with bash. To make those
variables persistent on a Linux system, add them in a bash (.sh) file in _/etc/profile.d_.

On the Onion, the [python-dotenv](https://github.com/theskumar/python-dotenv) library is used to read the environment variables for the script, so make sure
you have a .env file that is populated with your configuration.

#### 3. Start sniffer code on boot
The _start_sniffer.sh_ contains the commands to launch the publisher and subscriber clients. Hence, we just have to call this script on boot to start them.

- edit the _/etc/rc.local_ file on the Omega
- add the line ```sh /root/Mark-II-sniffer/scripts/start_sniffer.sh <mode> <protocol> &```
- the mode is either 'sniffer' or 'controller' and the protocol 'tcp' or 'serial'
- If the app has to communicate modbus over TCP, we presume it won't run on the Onion. 
Hence, you can use the PM2 process manager or another method to start the script on boot/reboot for your system.

For further reference, see the [full Onion documentation.](https://docs.onion.io/omega2-docs/)
