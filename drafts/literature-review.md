# Literature Review

// Overview of existing systems that I am going to talk about.



// Introduction to Conventional Wired System.



A GSM based communication system for solar powered street light. In this system, each street light has a microcontroller monitoring the power generation, battery status, battery behaviours, and light behaviours. Each microcontroller communicates with a remote server through Short Message Service (SMS), that is, the underlying technology which enables mobile phone to send and receive text messages from or to other mobile phones. The SMS messages carries the sensing data from each street light to the remote server through a SMS gateway to be processed and stored in the database. Finally, a web console can be used to visualise the data. The use of SMS solves a big issue that other means of communication such as Bluetooth, ZigBee, and Wi-Fi has, the lack of range. With this setup, a large area of street lights can be connected to the SMS gateway thanks to the wide communication range of the underlaying GSM communication system. However, the major drawback of using SMS as the underlaying means of communication is the size of each SMS message must be within 160 characters. This limitation means the sensing data cannot be very complicated and detailed, which limits the capabilities of the system and its use cases. The remote server also plays an important role in the communication system. It is composed of a GSM gateway that is connected to a web server, and the web server is exposed to the internet so everyone can access the visualisation of the data over the internet. The web server is also connected to a database such that the sensing data is persistent even if the web server is down. Unfortunately, the cost estimate and the performance of such a system, and the underlaying architecture of the web server are not documented in the literature. It is hard to quantitatively compare this solution to other solutions in terms of price and performance. This system is also intended for used with street lights, which has much lower density than solar panels, and the behaviour of such a system is undocumented as the number of microcontroller increases. Therefore, it is uncertain that the GSM based communication system would adapt well in a more demanding situation such as solar farm. 



https://sydney.primo.exlibrisgroup.com/discovery/fulldisplay?docid=ieee_s6914078&context=PC&vid=61USYD_INST:sydney&lang=en&search_scope=MyInst_and_CI&adaptor=Primo%20Central&tab=Everything&query=any,contains,Solar%20panel%20and%20battery%20street%20light%20monitoring%20system%20using%20GSM%20wireless%20communication%20system&mode=basic

https://ieeexplore-ieee-org.ezproxy1.library.usyd.edu.au/document/6914078

https://www.etsi.org/deliver/etsi_gts/03/0338/05.00.00_60/gsmts_0338v050000p.pdf



A GPRS based communication system for solar panel monitoring and controlling. The system is designed around the concept of Internet of Things (IoT) in mind and it is separated into three layers, the sensing layer, network layer, and application layer. The sensing layer contains sensors monitoring the characteristics of the solar panel, the sensing data are then fetched into a microcontroller equipped with a GPRS modem, finally the sensing data is sent to the internet through the GPRS modem. The application layer contains advanced functionalities such as data analytics, fault monitoring, generation monitoring, and functionalities that leverage the powerful processing capabilities of the server. Between the sensing and application layer, the network layer bridge the two layers by providing internet access and hosting database for persistent data storage. The system utilises the GPRS cellular network, which is the primary means of communication between mobile phones in the 2000s. This technology have the benefit of covering a wide area and offers internet access with limited speed. That means, a single GPRS cellular tower are able to cover a significantly more solar panels comparing to other wireless technologies such as Bluetooth, ZigBee and Wi-Fi. Having direct internet access also means It doesn't have to translate the sensing data from one communication system to another like the GSM based system, where data being sent through SMS messages gets translated at the GSM gateway into HTTP messages. Unfortunately, GPRS is still very slow by today's standards with only 14Kbps upload bandwidth. It imposes a substantial limit on the complexity and amount of data being sent to the server for processing. More importantly, countries worldwide had been planning on decommissioning this old means of communication before mid 2020s. Therefore a new carrier for the sensing data needs to be used. Similar to the previous literature, there is no cost estimation of such a system and no performance details are documented. 



https://sydney.primo.exlibrisgroup.com/discovery/fulldisplay?docid=ieee_s7513793&context=PC&vid=61USYD_INST:sydney&lang=en&search_scope=MyInst_and_CI&adaptor=Primo%20Central&tab=Everything&query=any,contains,An%20IoT%20based%20smart%20solar%20photovoltaic%20remote%20monitoring%20and%20control%20unit&offset=0

https://ieeexplore-ieee-org.ezproxy1.library.usyd.edu.au/document/7513793

https://www.3gpp.org/technologies/keywords-acronyms/102-gprs-edge#:~:text=GPRS%20adds%20packet%2Dswitched%20functionality,time%20slots%20into%20one%20bearer.





ZigBee

Wifi

Satellite

RF





https://sydney.primo.exlibrisgroup.com/discovery/fulldisplay?docid=elsevier_sdoi_10_1016_j_dcan_2018_11_002&context=PC&vid=61USYD_INST:sydney&lang=en&search_scope=MyInst_and_CI&adaptor=Primo%20Central&tab=Everything&query=any,contains,Wireless%20sensing%20for%20a%20solar%20power%20system&offset=0

https://www.sciencedirect.com/science/article/pii/S2352864818300051?via%3Dihub



https://sydney.primo.exlibrisgroup.com/discovery/fulldisplay?docid=ieee_s8855749&context=PC&vid=61USYD_INST:sydney&lang=en&search_scope=MyInst_and_CI&adaptor=Primo%20Central&tab=Everything&query=any,contains,A%20LOW-COST%20SOLAR%20FARM%20MONITORING%20SYSTEM%20BASED%20ON%20CLOUD%20DATABASE&offset=0

https://ieeexplore-ieee-org.ezproxy1.library.usyd.edu.au/document/8855749



https://sydney.primo.exlibrisgroup.com/discovery/fulldisplay?docid=proquest2081623274&context=PC&vid=61USYD_INST:sydney&lang=en&search_scope=MyInst_and_CI&adaptor=Primo%20Central&tab=Everything&query=any,contains,An%20Open-Source%20Monitoring%20System%20for%20Remote%20Solar%20Power%20Applications.&offset=0

https://arxiv.org/abs/1502.03780