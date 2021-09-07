# vscp-python-send-file-measurement

Send a measurement value received from standard input to a VSCP daemon as a [Level II string measurement event](https://grodansparadis.github.io/vscp-doc-spec/#/./class2.measurement_str).

## Syntax

```
echo "1.23" | ./vscp-python-send-file-measurement host user password guid type sensorindex zone subzone
```

| Parameter | Description |
| --------- | ----------- |
| **host** | The hostname or IP address of the VSCP daemon. |
| **user** | The username to use for authentication. |
| **password** | The password to use for authentication. |
| **guid** | The GUID to use for the measurement event. |
| **type** | The type of the measurement event. |
| **sensorindex** | The sensor index to use for the measurement event. OPtional. Defaults to 0. |
| **zone** | The zone to use for the measurement event. OPtional. Defaults to 0. |
| **subzone** | The subzone to use for the measurement event. Optional. Default to 0. |

## Usage

Typical usage is to send a measurement stored in a file bye some other program. This is common in many sensor networks. For example, a sensor network that uses a temperature sensor can store the temperature in a file and send it to the VSCP daemon.

For example a one wire temperature sensor on a Raspberry Pi can be read from 

```
/sys/bus/w1/devices/28-000004d9b8ff/temperature
```
so 

```
cat /sys/bus/w1/devices/28-000004d9b8ff/temperature | ./sendfile_measurement.py 192.167.1.7 admin secret 6 1
```

will send a [temperature measurement event](https://grodansparadis.github.io/vscp-doc-spec/#/./class2.measurement_str?id=type6) to the VSCP daemon at address _192.168.1.7_. 

typically used in a cron job.

----

This file is part of the VSCP project (https://www.vscp.org)



