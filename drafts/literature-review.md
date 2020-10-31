# Literature Review

There are a few existing solutions and work done by researchers exploring the ways to construct a communication system for monitoring and controlling of solar panels. They can be separated into three categories: 

1. Wired Communication
2. Long Range Wireless Communication
3. Short Range Wireless Communication

The wired communication uses some types of physical cables to connect the components of the system together. The long range wireless communication employs cellular or satellite network, whereas short range wireless communication explores near field communication protocols such as ZigBee and Bluetooth. 

While many literatures explored different means of communication for solar power generation system, only a few of them addresses how the data from solar panels can be processed or handled remotely more timely and efficiently. 





The conventional method of monitoring a large scale solar farm is using wired cables. In this setup, a set of power converters read the current and voltage, then transmit the sensing data to the monitoring station over some physical cables. The benefits of using physical cables are (Reference):

1. Reliable, have been used for many years with proven track record.
2. High bandwidth, complicated sensing data with high sampling rate can be transmitted without fully saturating the link.

However, the researchers have found the lifespan of the system may be reduced due to the physical cables are exposed to constant sunlight and rain. (REFERENCE) Furthermore, the signals in the cables may attenuates over long distances and counter measures such as repeater may be required. 

https://www.sciencedirect.com/science/article/pii/S0957417414006307#b0035

https://www.sciencedirect.com/science/article/pii/S0960148108002097?via%3Dihub



A GSM based communication system for solar powered street light. In this system, each street light has a microcontroller monitoring the power generation, battery status, battery behaviours, and light behaviours. Each microcontroller communicates with a remote server through Short Message Service (SMS), that is, the underlying technology which enables mobile phone to send and receive text messages from or to other mobile phones. The SMS messages carries the sensing data from each street light to the remote server through a SMS gateway to be processed and stored in the database. Finally, a web console can be used to visualise the data. The use of SMS solves a big issue that other means of communication such as Bluetooth, ZigBee, and Wi-Fi has, the lack of range. With this setup, a large area of street lights can be connected to the SMS gateway thanks to the wide communication range of the underlaying GSM communication system. However, the major drawback of using SMS as the underlaying means of communication is the size of each SMS message must be within 160 characters. This limitation means the sensing data cannot be very complicated and detailed, which limits the capabilities of the system and its use cases. The remote server also plays an important role in the communication system. It is composed of a GSM gateway that is connected to a web server, and the web server is exposed to the internet so everyone can access the visualisation of the data over the internet. The web server is also connected to a database such that the sensing data is persistent even if the web server is down. Unfortunately, the cost estimate and the performance of such a system, and the underlaying architecture of the web server are not documented in the literature. It is hard to quantitatively compare this solution to other solutions in terms of price and performance. This system is also intended for used with street lights, which has much lower density than solar panels, and the behaviour of such a system is undocumented as the number of microcontroller increases. Therefore, it is uncertain that the GSM based communication system would adapt well in a more demanding situation such as solar farm. 



https://sydney.primo.exlibrisgroup.com/discovery/fulldisplay?docid=ieee_s6914078&context=PC&vid=61USYD_INST:sydney&lang=en&search_scope=MyInst_and_CI&adaptor=Primo%20Central&tab=Everything&query=any,contains,Solar%20panel%20and%20battery%20street%20light%20monitoring%20system%20using%20GSM%20wireless%20communication%20system&mode=basic

https://ieeexplore-ieee-org.ezproxy1.library.usyd.edu.au/document/6914078

https://www.etsi.org/deliver/etsi_gts/03/0338/05.00.00_60/gsmts_0338v050000p.pdf



A GPRS based communication system for solar panel monitoring and controlling. The system is designed around the concept of Internet of Things (IoT) in mind and it is separated into three layers, the sensing layer, network layer, and application layer. The sensing layer contains sensors monitoring the characteristics of the solar panel, the sensing data are then fetched into a microcontroller equipped with a GPRS modem, finally the sensing data is sent to the internet through the GPRS modem. The application layer contains advanced functionalities such as data analytics, fault monitoring, generation monitoring, and functionalities that leverage the powerful processing capabilities of the server. Between the sensing and application layer, the network layer bridge the two layers by providing internet access and hosting database for persistent data storage. The system utilises the GPRS cellular network, which is the primary means of communication between mobile phones in the 2000s. This technology have the benefit of covering a wide area and offers internet access with limited speed. That means, a single GPRS cellular tower are able to cover a significantly more solar panels comparing to other wireless technologies such as Bluetooth, ZigBee and Wi-Fi. Having direct internet access also means It doesn't have to translate the sensing data from one communication system to another like the GSM based system, where data being sent through SMS messages gets translated at the GSM gateway into HTTP messages. Unfortunately, GPRS is still very slow by today's standards with only 14kbps upload bandwidth. It imposes a substantial limit on the complexity and amount of data being sent to the server for processing. More importantly, countries worldwide had been planning on decommissioning this old means of communication before mid 2020s. Therefore a new carrier for the sensing data needs to be used. Similar to the previous literature, there is no cost estimation of such a system and no performance details are documented. 



https://sydney.primo.exlibrisgroup.com/discovery/fulldisplay?docid=ieee_s7513793&context=PC&vid=61USYD_INST:sydney&lang=en&search_scope=MyInst_and_CI&adaptor=Primo%20Central&tab=Everything&query=any,contains,An%20IoT%20based%20smart%20solar%20photovoltaic%20remote%20monitoring%20and%20control%20unit&offset=0

https://ieeexplore-ieee-org.ezproxy1.library.usyd.edu.au/document/7513793

https://www.3gpp.org/technologies/keywords-acronyms/102-gprs-edge#:~:text=GPRS%20adds%20packet%2Dswitched%20functionality,time%20slots%20into%20one%20bearer.



A short range communication method that are evolving around the IoT concept is ZigBee which is explored over the recent years. Like many other communication systems, there needs to be a ZigBee gateway with internet access to forward data from the solar panels to the server and persistent data store using HTTP protocols. Furthermore, the limited communication range of ZigBee allows the the power consumption to be is very low. The researchers claim a ZigBee module can be powered by non-rechargeable battery for two to three years and it can connect up to 65000 ZigBee modules.  (REFERENCE) Since ZigBee is designed for modern IoT applications, it has more than sufficient bandwidth of up to 250kbps for complicated data exchange over the network. The problem with ZigBee is its limited range of around 1500 meters with direct line of sight and the range may be reduced significantly if there are obstructions. (REFERENCE) To combat this issue, ZigBee modules have the capability to form a cluster of connected ZigBee network which allows it to cover a much wider area. The supported network topologies of ZigBee modules are Star, Cluster Tree, and Mesh Network. (Reference) 

The star topology has a primary ZigBee module that are directly connected to all secondary ZigBee modules. Since they are directly connected to the primary module, the resources of the secondary modules such as bandwidth are completely reserved for its own communication with minimal latency. This topology doesn't increase the coverage of a ZigBee Network but it is suitable for a small cluster of solar panels to communicate with the gateway that has internet access such as roof top solar systems.

The cluster tree topology is formed by connecting many networks with star topology. The sensing data from each module are sent and forwarded to the gateway through arbitrary number of ZigBee modules assuming there exists at least one gateway within the network that are directly or indirectly reachable from the originating module. This topology enables arbitrary coverage of the communication system. The problem with this topology is some ZigBee modules that needs to forward many other modules' sensing data may easily overwhelm its available bandwidth, leading to performance degradation.

Finally, the mesh topology allows each ZigBee module having more than two directly connected modules, which allowing them to form a mesh network. Similar to the cluster tree topology where the coverage is arbitrary, it also has the benefit of reducing the potential to reach bottleneck as the sensing data can be sent through many different path. 

https://www.sciencedirect.com/topics/engineering/zigbee-protocol#:~:text=ZigBee%20Gateways&text=2.4%20GHz%20802.15.,to%20communicate%20at%20250%20kbps.

https://www.sciencedirect.com/science/article/pii/S2352864818300051?via%3Dihub#bib7

https://www.sciencedirect.com/science/article/pii/S0957417414006307



Since the lack of studies with regards to the computer system architecture used in the communication system for solar panels. System architectures for communication systems that requires similar capabilities are reviewed instead. One of the proposed system is designed for monitoring automotive manufacturing processes using IoT devices, and it incorporates Kafka, Apache Storm, and MongoDB to process, monitor, and store data in real-time. In this architecture, Kafka is being used as a message queue for asynchronous communication between components of the system and it employs the publisher subscriber design pattern. The pattern separates the responsibility of the system into producer and consumer where a producer generates data, assign it with a topic that consumer can subscribe to, and consumers will be notified when a new data of their subscribed topic is available. The Apache Storm is used for real-time processing. It is subscribed to the topics in the Kafka and react to those new data depending on the type of sensor. In general, it stores the new data into MongoDB, a persistent data storage, and publish new data to the user so data is available as soon as it is generated and processed. The advantage of this architecture is the user can view the data in real-time whenever it is ready, whereas many other simple architectures consists of a single HTTP web server requires the user to refresh the website constantly to download new data. This enables the user to make timely decisions, and reduces the workload of the server as it only processes the data when it is available and the user doesn't querying for data constantly.



https://www.mdpi.com/1424-8220/18/9/2946