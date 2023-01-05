BLEHeartRateLogger.py
=====================

BLEHeartRateLogger.py is a Bluetooth Low-Energy (BLE) Heart Rate Monitor (HRM) data logger written in Python for Linux. With this tool you can log your heart rate and heart rate variability (RR) during exercise, sleep or whatever comes to mind.

Communication with the BLE HRM is established using `hcitool` and `gatttool`. The output of those tools is then parsed and saved to a sqlite database.

The code was used successfully with the following devices:
- Polar H7
- Zephyr HxM
- Wahoo TICKR


## Installation

On Debian/Ubuntu:
```
$ apt-get install bluetooth python-pexpect
$ git clone https://github.com/fg1/BLEHeartRateLogger.git
```

Run the script as root user or correctly specify the rights on `hcitool` and `gatttool`.



## Usage

To start the tool (as root or with correct rights):
```
# ./BLEHeartRateLogger.py
2015-01-10 13:40:59,326  Trying to find a BLE device
2015-01-10 13:41:00,856  Establishing connection to 00:11:22:33:44:55
2015-01-10 13:41:01,115  Connected to 00:11:22:33:44:55
2015-01-10 13:41:03,412  Heart rate: 65
2015-01-10 13:41:04,357  Heart rate: 65
```

To quit the tool, simply Ctrl-C.


Command line options:
```
usage: BLEHeartRateLogger.py [-h] [-m MAC] [-b] [-g PATH] [-o FILE] [-v]

Bluetooth heart rate monitor data logger

optional arguments:
  -h, --help  show this help message and exit
  -m MAC      MAC address of BLE device (default: auto-discovery)
  -b          Check battery level
  -g PATH     gatttool path (default: system available)
  -o FILE     Output filename of the database (default: none)
  -v          Verbose output
```

## Using the tool as non-root user

The `setcap` command can be used to give `hcitool` permission to be used by users other than root:
```
sudo setcap cap_net_raw+eip $(eval readlink -f `which hcitool`)
sudo setcap cap_net_admin+eip $(eval readlink -f `which hciconfig`)
```

## Troubleshooting

In case the tool is not able to connect to your BLE HRM, first check manually that your computer and BLE HRM device are able to talk to eachother using the following steps (as root).
```
# hcitool lescan
```
This should list the BLE devices around you with their MAC address with something which looks like this: 00:11:22:33:44:55. You can safely Ctrl-C when the device has been found. We will the connect to the device:
```
# gatttool -b 00:11:22:33:44:55 -I
```
This should open a prompt. Type the following commands:
```
> connect
> characteristics
> exit
```

In case one of the steps mentionned above fails, check your Linux installation and eventually `bluez` version (>= v.5 recommended).



## Contributing

Contributions are welcome.

1. [Fork the repository](https://github.com/fg1/BLEHeartRateLogger/fork)
2. Create your feature branch (`git checkout -b my-feature`)
3. Commit your changes (`git commit -am 'Commit message'`)
4. Push to the branch (`git push origin my-feature`)
5. Create a pull request

