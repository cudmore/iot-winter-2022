# Case Studies

## Ride Sharing

Like Uber and Lyft. What companies provide this in other contries?

### Network Structure

Basically, a smart-phone app connects a driver with a passsenger.

You have a phone with a cellular connection, you install an app and register with an email and credit-card.

All ride-share drivers have a phone with cellular and GPS. The location of the cars are transmitted to a cloud server.

You bring up the app and request a ride. Your phone GPS coordinates get sent to cloud server.

The cloud server determines the best car (maybe not the closest). It also determines the price. You see real-time price adjustments based on volume.

Once a driver accepts to passenger, the cloud server transmits this information to both the driver and the passenger phone (ride-share app)

The ride share app on the drivers phone give them directions to the passenger. Simultaneously, the ride-share app on the passengers phone provide name of driver, color and make of car and real-time updates of location of car with estimated time of arrival.

### Important points

- The driver is not given the passengers location or destination until they accept the ride.
- Real-time price adjustments are not really neccessary but are in place to maximize profit based on demand. If you have ever arrived at the Sac airport after 10p or 11p, ride-share prices can be 3-4 times normal. My tip is to take a traditional Taxi, they have fixed prices from the airport to a number of locations including Midtown Sac and Davis.

- The "best car" for you is arbitrarily complex. In the simplest case it wouldl be the closest car (via GPS). IT probably includes, driving time and complexity of the drive from car location to passenger. Could include the passengers rating (by drivers) and also a rating of the driver (from passengers). Could include the drivers logged hours they will work (when will they get off shift).

### Social and Economic Impact

It really depends on who you ask. Reports vary widely from really good to really bad.

When ride share was started in SF, the Taxis companies had $xxx profit. Once ride share was established, the taxi revenue went down to $yyy. IS the ride-share revenue just the diffferenc in taxi profit? No! The ride-share profits greatly outperform this difference, basically, more people than ever are using IOT ride-share over traditional taxis.

This has of course reduced the profits of the taxi companies but has larger economic, social, and environmental impact. Including: less traffic on the rode and potentially less environmental impact, less revenue from paid parking spaces and garages.

There has been major issues with ride-share drivers as workers and their rights. Many reports conclude they make below minimum wage.

Ride sharing has created a new class of worker, the Gig worker. See https://en.wikipedia.org/wiki/Gig_worker

The gig economy is defined as:
```
a labor market characterized by the prevalence of short-term contracts or freelance work as opposed to permanent jobs.
"working in the gig economy means constantly being subjected to last-minute scheduling"
```

### Future of ride-share

- Similar to data collected by companies like FB, Google, Amazon (etc) as users click links in their web-browser. Car-share companies are collecting orders of magnitude more driver and passenger information. Things like GPS location of passenger, frequency of ride-requests, willingness of passenger to pay a low or high price. The future of IOT may be when ride-share companies start to sell this information to other businesses. 

### Additional reading

- The Social, Economic, and Environmental Impacts of Ridesourcing Services: A Literature Review (2021).

- The Economics of Ride-Sharing Applications (2020).

- Measuring the Benefits of Ridesharing Services to Urban Travelers (2020), from Hutchins Center, Brookings. Conclude that Uber should not be regulated as it has provided biollions of dollars of saving for San Francisco residents.


## Scooter and Bike Sharing

Companies such as Lime, xxx

### Network structure

The company sets up a fleet of vehicles that have sensors to transmit (usually over cellular networks) back to a cloud server. These vehicles transmit GPS coordinates, battery level, presumably other parameters such as miles travelled and sensor data on the "health" of the motor and vehicle in general.

The rider has a cell phone, installs an app, and registers with email and credit card.

The rider is given a map of location of bikes/scooters/cars. On arrival within proximity of vehicle, ride usually scan a QR code into thecell phone app. Their account is verified and that vehicle is unlocked and the ride can begin

### Important points

With the fleeet of IOT vehicles and data on rider usage (when and where were rides initiated, what route did they take, where was the destination, how long was the ride), these companies cloud computing can give employees feedback on probability of a breakdown, as well as optimal location of the vehicles. They physically drive out with a van and move the vehicles to more optimal locations.

In Marseille France, on the Medditerranean, all sharwed scooter and bikes ended up at the beach (rider would opt for ride-share to get home). The cost of constantly moving their scooter/bikes back to where people would initiate a new ride (to the beach) prompted these companies to cancel their service to Marseille!

### Social and economic impact

The impacts of Scooter sharing are generally positive. Yet, they are limited to short distance trips within a city, neighborhood, or town. What are the pros and cons of this limited distance of trips?

See: https://www.ridefatdaddy.com/the-economic-impact-from-electric-scooter-sharing/

Using data collected in the July 2019 Global Rider Survey by Lime, we find that US riders that fall into lower income brackets are more likely to choose Lime because it is an affordable travel option, whereas higher income riders are more likely to ride Lime for convenience.

Scooter sharing increases local mobility, not sure if it produces more spending $ for people.

Scooter sharing increases consumer spending (for those that can afford it), resulting in increased revenue at local lesure activities such as cafes, restaurants, and bars

What are the similarities and differences of scooter and bike sharing compared to car sharing such as zip car?

### Future

By collecting both vehicle and user data, the companies now have large datasets to infer or predict many new parameters. This includes rider safety, what are the current sensor conditions when a rider either crashes the vehicle or is in an accident? How long had they been riding? What time of day? Weather conditions? Light-levels? GPS location of incident? Route taken to the incident? 

This can be used to give riders feddback on their current riding: location, weather, speed, traffick congestion, etc. This could also be used to remotely modify the driving features of the vehicle itself, such as limiting it speed.

### Additional Reading

The Economic Impact From Electric Scooter Sharing( year xxx)
https://www.ridefatdaddy.com/the-economic-impact-from-electric-scooter-sharing/

Research Reveals Shared E-Scooter Systems Can Generate Significant Positive Economic Spillover(2021)
https://www.emorybusiness.com/2021/03/11/research-reveals-shared-e-scooter-systems-can-generate-significant-positive-economic-spillover/

The Role of Shared E-Scooter Systems in Urban Sustainability and Resilience during the Covid-19 Mobility Restrictions (2021). See Dias_et_al_2021.pdf

## IOT on the davis campus

We have a number of IOT systems implemented here and you might interact with them most every day.

Think about the architecture of each. 

### Parking

- Install app, authenticate with license plate, email and credit card

- When you park you login and specify amount of time you want. Phone GPS may be sent to cloud server, not sure?

- When parking attendant drives around, they check all parked cars license plates are paying, if not they issue a ticket. 

- This system could use a camera to autorecognize plates and check the paying database. The camera could be mounted on a car driven by attendant. Why not have a fleet of droones to do the same thing?

- Tickets could be issued electronically after verification by attendant.

### Daily symptom check and Covid testing

- Authenticate on a website and answer survey

- Auto receive email with confirmation or denial, depends on your covid testing status (generally within the last two weeks)

### Door locks

- Uses cell phone app and close proximity blue tooth

## Industrial IO

Probably the biggest area of development and speculation.

Give concrete example of (i) assembly line and (ii) machine maintenance

## Agricultural IOT

    Agricultural IOT is a critical endeavor. It is needed because we need to optimize our food production to ensure a healthy world population.

    Optimizing a farm with water, nutrients, pest control and output is critical to the livelihood of a farmer. Has broader economic impact for the cost of food. As our population grows, we need more efficient farming to feed a growing population.

    Agriculture IOT is actively developed and evolving. Main bottleneck are maintaining a sensor network, how to transmit data of long distances, how to react to observations in the data. Sensor network are now being replaced by automated drones.

### Network structure

    - Microcontrollers with sensors are placed in a grid covering some density of a farm.
    - These transmit data to local servers where data is analyzed
    - This presents a unique technical challenge because the distance of data transmission is beyond wifi (and cellular might be expensive). Thus, the development of long-range LAN (LoRaWan)

### Future network structure

    More recently, a mesh of nodes in the network is being replaced by autonomous drones.

    This is due to the fact that the mesh network is hard to maintain, can be costly, requires constant mainenance.

    Drones can be programmed to automatically fly a preset path and collect a range of data from video (in the air) to landing and taking soil samples.

    This is an example of 'edge computing' where the drone is more computationaly powerful than a simple sensor. It can process and store data and then download once landing at a remote gateway.

### LoRa and LoRaWan

Wi-fi is trademarked. Any manufacturerer satisfying the technical requirements can brand their product as Wi-Fi.

Wi‑Fi is a trademark of the non-profit Wi-Fi Alliance, which restricts the use of the term Wi-Fi Certified to products that successfully complete interoperability certification testing.

LoRa is patended, the technology is ownded by a company.

LoRaWan specifies the higher level protocols and is run by a non-profit consortium of companies and other not-for-profits.

### Additional Reading

LoRa: https://en.wikipedia.org/wiki/LoRa


## Smart home

No discussion of the IOT would be complete without talking about the smart home

xxx

### Additional reading

Defines the term domotics (e.g. smart home)
https://www.t3.com/features/the-smart-home-guide


## IOT for individuals with disabilities

**Opinion**. There does not seem to be a lot of talk about this. This may be because of lower profit margins. I think it is an area of great opportunity. Including improving elderly lifestyles.

Using a smart home can help individuals with disabilities.

**Opinion**. Many IOT systems, in particular the smart home are ready to help those with disabilities. Work needs to be done to address the actual needs of these individuals and promote adoption.

Smart homes including connected speakers, refrigerators, ovens, and thermostats help disabled individuals have more control of their daily actions, and can be programmed to suit a specific user’s needs. IoT technology also provides for wearables like smartwatches that translate content including emails and texts into Braille or read the same aloud. By improving autonomy, IoT is helping disabled individuals overcome both social barriers and attitudinal barriers, and allowing them to improve their general quality of life through the provision of accessible and useful equipment.

- Example. Smart lights that change color when certain sounds are present such as a knock at the door, a phone call, a fire alarm, or a babies cry.

- Example. Haptic feeback IOT. Sad that this "Toe-Tickling" is a mapping of google maps to haptics (pun intended). This is an example (IMHO) of an IOT fail, it is just the proof of concept without any follow through. There is very little though in how this might benefit those with disabilities. Allowing them to use IOT maps.

An earlier example is the "Lechal" shoe meaning "take me there" in Hindi. But these seem to be not available.

### Additional reading

The Internet of Things (IoT) and Persons with Disabilities:
Exploring Benefits, Challenges, and Privacy Tensions

- see pdf

Toe-Tickling Shoes Let You Navigate The City By Touch (2014).
https://www.popsci.com/article/gadgets/toe-tickling-shoes-let-you-navigate-city-touch/

Note, it is sad that these topics are not more thought about as this is from 2014! This is basically a GPS smart-phone app that gives you direction with "haptic" feedback. Haptic feedback is used in most macintosh laptops where the main mouse-pad is not longer a button but a 'vibrator' that gives the impression of a button. If you use a mac laptop, ask yourslef if this feedback is intuitive.

## Smart power

On a consumer level, this is intimately related to smart homes.

Electrical power. Its production and thus cost changes as a function of time of day and season. If you run your washing machine, heating, or cooling at peak usage times it is not only more expensive for you but it puts a strain on the system. The idea is to enable home appliances to use this energy availability and only run during off peak times.

Energy hungry smart home applicances need to only run during off peak hours. This includes heating, cooling, washing machines, clothes dryers, and dishwashers.

### Network architecture

An IOT appliance check the grid for available power and only runs when it is easy.


## Smart cities

    There is a lot of speculation on how the IOT can create the new smart city.

From the Guardian (2017)

With sensors and smartphones to make roads more flexible, Tilburg (Netherlands) is addressing the question: how can a city become safer for less able residents?

A cell phone app that allows the user to alter traffic light pattern based on proximty.

  - Allowing them to more safely cross and to give them more time.
  - Another version detects visually impaired pedestrians and activates the ticking sounds that tell them whether the light is red or green.

A system like this could also:
  - detect if there is one person waiting or say 10 people and having traffic lights respond appropriately.
  - Teachers could be given access so the light would not turn green until all children are safely across.
  - Turn lights green to allow emergency vehicles such as ambulances, fire-trucks, and police through
  - Allow delivery vehicles easier access with fewer stops and starts

See ... The slow lane: Dutch app allows elderly to 'hack' traffic lights.
https://www.theguardian.com/cities/2017/jul/12/dutch-app-elderly-hack-pedestrian-crossings

The network architecture here is a smart phone connects to a traffic light via bluetooth and with the correct credentials, can later the pattern of the traffic light.

## Biometric IOT

    Wide range of use cases including
        - in hospital patient monitoring
        - remote patient monitoring
        - new health data from study participants

        - large scale biometric data collection (wearable biometrics)

    Smart Enhalers

        QIoT’s smart inhaler connects with an AI platform that can account for seasonal triggers and pollen counts as well as individuals’ medical histories, and could potentially identify dangerous clusters of people with conditions such as Covid-19. The new device will be trialled initially with NHS Scotland.

    Monitoring diabetic patients
    
    Smart Watch

        Although not originally designed for biometric monitoring, smart watch technology is evolving to do just this. There is huge possibility for health monitoring and treatments, but, not without some risks.
            
            - Sensors are noisy and may produce false-positives and false-negatives
            - USers may over/under treat
            - Users may not seek proper clinical care
            - Personal mediacal data is at risk

        Possible benefits are immense
            - Blood oxygen measure
            - Echocardiogram (ECK)

### Additional reading

7 examples of how the internet of things is facilitating healthcare.
https://econsultancy.com/internet-of-things-healthcare/

Wearable Biosensors Can Quantify, Monitor MS in Clinic and Free-Living Settings (2021).
https://www.neurologyadvisor.com/topics/multiple-sclerosis/wearable-biosensors-can-quantify-monitor-ms-in-clinic-and-free-living-settings/

Cleveland Clinic Studies Accuracy of Apple Watch 4 for Atrial Fibrillation Detection
Watch display only picked up 41% of AFib occurrences in hospitalized patients, additional waveform PDF detected 98% of occurrences.
https://newsroom.clevelandclinic.org/2020/02/25/cleveland-clinic-studies-accuracy-of-apple-watch-4-for-atrial-fibrillation-detection/

Heart monitoring in young healthy people might not be necessary at all (2019). Very good article, lets discuss.
https://www.cnet.com/health/apple-watch-ecg-app-what-cardiologists-want-you-to-know/


## Netowrk security

    A critical component is network security and personal information. The initial IOT devices were not designed with network security in mind. This has resulted in some case examples of IOT failure:

    1. 10,000 refrigerators hijacted to send spam email
    2. 

## Personal Privacy

Of course personal health/biometric data needs to be protected.

What about other cases of personal privacy where IOT sensors can collect data that can be used against you in a criminal case?

Here is a string of logic from the UCLU

 1) It is a significant thing to allow a microphone into your private space
 2) People have a need for ironclad assurance their devices cannot betray them

The ACLU says "it’s a significant thing to allow a live microphone into your private space,” and that the chilling effects of surveillance give people a need for “ironclad assurance that their devices will not — cannot — betray them.”

But then the argument is, well, we already do that because we carry a phone.

For example "The CEO of Shotspotter — the company that puts microphones around cities to listen for gunshots — had made the same argument to me about that company’s microphones and their potential repurposing for surveillance. If you’re worried about government spies, he told me, “they’re not going to be using our sensors, they’ll be using your phone. It’s in your pocket and has a better microphone.”

The ACLU logic continues as "It’s a fair point that there is nothing unique about smart assistants or televisions or refrigerators or any other IoT devices (or microphones on telephone poles). But, we at the ACLU are not going to ignore certain privacy vulnerabilities just because there are other, potentially bigger vulnerabilities out there as well."

Finally, from the UUCLU, "What the CIA documents confirm is that the government follows that same logic in reverse: just because cell phones are available to hack, does not mean the government is not engaged in figuring out how to hack every other available device. The documents suggest that the CIA not only has the ability to hijack widely used Apple and Android phones, but can invisibly turn on the microphone in smart televisions, and that it has been targeting the computer systems in cars."

### Addiitonal reading

2017, General article from UCLU. Mentions FBI warants to retreive Alexa void recordings. Also cover "Shot Detector" and questionable data collection and niterpretation ethics.

Title: CIA Documents Highlight Privacy Issues of the 'Internet of Things'

https://www.aclu.org/blog/privacy-technology/internet-privacy/cia-documents-highlight-privacy-issues-internet-things

The EFF on "EFF vs IoT DRM, OMG!"

https://www.eff.org/deeplinks/2018/02/eff-vs-iot-drm-omg


## Is the IOT always good?

Answer: No, it is not always good.

**Opinion** Detatch yourself from the IOT for a minute, hour, day or week.

 - Walk around without an IOT map telling you which way to go or the distance to your destination
 - Explore your environment on your own. IF you want a slice a pizza or a bite-to-eat with friends, just walk around and see what you find.
 - When driving to a destination, try not to use maps
 - Don't look up the reviews of a restaurant before going, just give it a shot.