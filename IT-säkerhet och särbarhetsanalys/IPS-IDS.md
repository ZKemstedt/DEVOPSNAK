# IPS / IDS
### IPS - Intrusion Prevention Systems
### IDS - Intrusion Detection Systems


IDS and IPS Characteristics
## Detect and Stop Attacks
* An IDS monitors traffic offline and generates an alert (log) when it detects malicious traffic including:
  * Reconnaissance attacks
  * Access attacks
  * Denial of Service attacks

* An IDS is a passive device because it analyzes copis of the traffic stream.
  * Only requires a promiscuous interface
  * Does not slow network traffic
  * Allows some malicious traffic into the network

* An IPS builds upon IDS technology to detect attacks.
  * However, it can also immediately address the threat.

* An IPS is an active device because all traffic must pass through it.
  * Refferd to as "inline-mode", it works inline in real time to monitor Layer 2 through Layer 7 traffic and content.
  * it can also stop single-packet attacks from reachting the target (IDS cannot)

* Both technologies are deployed as sensors.
* Both technologies use signatures to detect patterns of misuse in network traffic.
* Both can detect atomit patterns (single-packet) or composite patterns (multi-packet).

## Advantages and Disadvantages of IDS and IPS

<table>
<tr><th> </th> <th> Advantages </th> <th> Disadvantages </th> </tr>
<tr><td>

IDS 
(Promiscuous Mode)

</td><td>

* No Impact on network (latency, jitter)
* No network impact if there is a sensor failure
* No network impact if there is a sensor overload
 
</td><td>

* Reponse action cannot stop trigger packets
* Correct tuning require for response actions
* More vulnerable to network security evasion techniques

</td></tr>
<tr><td>

IPS 
(Inline Mode)

</td><td>

* Stops trigger packets
* Can use stream normalization techniques

</td><td>

* Sensoer issues might affect network traffic
* Sensor overloading impacts the network (latency, jitter)

</td></tr>
</table>

## Network IPS Sensors
* Implementation analyzes network-wide activity looking for malicious activity.
* Configured to monitor known signatures, but can also detect abnormal traffic patterns.
* Configured on: 
  * Dedicated IPS appliances
  * Catalyst 6500 network modules

<table>
<tr><th> </th> <th> Advantages </th> <th> Disadvantages </th> </tr>
<tr><td>

Network IPS

</td><td>

* is cost-effective
* Not visible on the network
* Operating system independent
* Lower level network events seen

</td><td>

* Cannot examine encrypted traffic
* Cannot determine whether an attack was successful

</td></tr>
</table>

## Signature Attributes
* Malicious traffic displays distinct characteristics or "signatures"
* These signatures uniquely identify specific worms, viruses, protocol anomalies, or malicious traffic.
* IPS sensors are tuned to look for matching signatures or abnormal traffic patterns.
* When a sensor matches a signature with a data flow, it takes action, such as logging the event or sending an alarm to IDS or IPS.
* Signatures have three distinctive attributes:
  * Type
  * Trigger (alarm)
  * Action

### Signature Types - Atomic Signature
* Signature types are ctaegorized as **atomic** or **composite**
* An atomic signature is the simplest type of signature. It consists of a **single packet**, activity, or event.
* Detecting atomic signatures consumes minimal resources. These signatures are easy to identify and understand because they are compared against a specific event or packet.

### Signature Types - Composite Signature
* A composite signature is also called a **stateful signature**
* A composite signature identifies a sequence of operations distributed across multiple hosts over an arbsitray period of time.
* An IPS uses a configured event horizon to determine how long it looks for a specific attack signature.

### Signature File
* As new threats are identified, new signatures must be created and uploaded to an IPS
* To make this process easier, all signatures are contained in a signature file and uploaded to an IPS on a regular basis.


## Signature Alaram
The hear of any IPS isngature is the signature alarm, often referred to as the **signature trigger*.


### Pattern Based Detection
Patern-based detections, also knows as signature-based detection, compares the network traffic to a database of known attacks and trigger an alarm, or prevents communication if a match is found.


### Anomaly-Based Detection
* Anomaly-based detection, also knows as profile-based detection, involves first defining a profile of what is considered normal for the network or host.
* The signature trigger an action if excessive activity occurs beyond a specified threashold that is not included int the normal profile.

### Policy-Based Detection
* Policy-based detection is also known as beavious-based detection.
* The administrator defines behaviours that are suspicious based on historical analysis
* Honeypot-based detection uses a dummy server to attract attacks.
  * The honeypot approach is to distract attacks away from real network devices.
  * Honeypot systems are rarely used in production environments.

### Trigger False Alarms
* Triggering mechanisms can generate alarms that are false positives or false negatives.
* These alarms must be addressed when implementing an IPS sensor.


### Tune Signature
* An administrator must balance the number of incorrect alarms that can be tolerated with the ability of the signature to detect actual intrusions.
* I f IPS systems use untuned signatures, they produce many false positive alarms.

## Signature Actions
* Whevenver a signature detect the actitivy for which it is configured, the signature triggers one or more actions.

* Several actions can be performed:
  * Generate an alert.
  * Log the activity.
  * Drop or prevent tha activity.
  * Reset a TCP connection.
  * Block future activity.
  * Allow the activity.
  
### Drop or Prevent the Activity
An IPS can be enabled to deny the attacks packets, deny the connection, or deny the specific packet.

# Manage and Monitor IPS
## Secure Device Event Exchange
* IPS sensors and Csico IOS IPS generate alarms when an enabled signature is triggered. These alarms are stored on the sensor and can be viewd locally, or through a management application.
* The Cisco IOS IPS feature can send a syslog message or an alarm in Secure Device Event Exchange (SDEE) format.
* CCP can monitor syslog and SDEE-generated events and keep track of alarms that are common in SDEE system message, including IPS signature alarms.
## IPS Configuaration Best Practices
* The need to upgrade sensors with the latest signature packs must be balanced with the momentary downtime during which the network becomes vulnerable to attack.
* Update signature packs automatically
* Download new signatures to a secure server within the management network.
* Place signature packs ona dedicated SFTP server within the management network.
* Configure the sensort to regularly check the SFTP server for new signature packs.
* Keep the signature levels that are supported on the management console synchronized with the singature packs on the sensors.