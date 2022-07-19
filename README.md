# 30_Days_on_Otmoor

This is the repository for my environmental media lab piece
it will be a low-tech web artwork inspired by the rebellion to enclosure on otmoor in the mid-1800s
The piece will comprise of a set of scenes that will refresh every cycle of the moon

scene 1:    
    names of places of commons (with a central point at otmoor*) in the shape of tools (trowels, spaces, gloves, hoes, etc.). The names will be gathered from shared assets website, users can add names of locations via an input box
scene 2:    
    images from the locations wrapped around knots
scene3:     
    somehow deals with abolition and the relationship between enclosure and commons
    ideas: programmatically scrubbing out military and police sites from map/images

links will be available to all locations

Ideally, this website is as low power as possible and could run of solar power

setup idea: 
    hardware
        raspberry pi - preferably a pizero
        e-ink screen
        18650 battery
        solar panel
        wifi connection

    software
        3D software - 3JS or GLSLViewer (this would be lower power I reckon)
        image-processing software - python PIL/wand or Javascript Sharp
        website - nodejs + HTML + CSS + Js
        fetching images from api
        storing locations (this could be a really simple server like a )
        30 day timer running on the server

    1. nodejs server handling fetching images from Place API, could handle glslviewer?
    2. website displaying three scene


*ie. I'll start at otmoor and work out
don't follow national lines


How to use Google Place Photo API
1. make a places search request
return a place id
2. make a places details request
this requires some parameter
get back a photoreference id



Initial list:
from here https://www.farmgarden.org.uk/your-area/london
Angell Terrace Residential Communal Garden
Arbor Projects London
Arcadian Gardens Surgery Community Wellbeing Centre
Archbishop's Park Gardening Club
Bankside Open Spaces Trust
Barn Hill Conservation Group
Barnet Community Garden
Belmont Childrens Farm
Besson Street Community Garden
Billets Hart Allotment Association	
Birchmere Good Life Garden
Brockwell Park Community Greenhouses	London
Brooks Farm	London
Cable Street Community Garden	London
Calthorpe Community Garden	London
Camden Disability Action	London
Castlehaven Horticultural Hub and Nature Garden	London
Cecil Sharp House Permaculture Garden	London
Chelsea Physic Garden	London
Cherry Orchard	London
Chingford Hall Community Garden	London
Chiswick House Walled Garden	London
Cob in the Community & Forrest School Collective
Coco Collective - Ital Community Gardens	London
Colville School Garden	London
Common Resource Ltd	London
Community Green Space	London
Companion Gardening	London
Coram's Fields	London
Core Landscapes a Core Arts project	London
Culpeper Community Garden	LONDON
Cultivate London Salopian Garden	London
D'Eynsford TMO Secret Garden	London
Deen City Farm	LONDON
Dig It
Doddington and Rollo Community Roof Garden	London
Dorset Road Allotments	London
ecoActive	London
Edible Garden	London
Edible Rotherhithe C.I.O.	London
Elm Village Community Garden	London
Elsley Primary School	London
Enviroble	London
FEAST With Us (FEAST)	London
First Fruits Environmental Services C.I.C.	London
Fitzhugh Grove Community Garden	London
Foodscape
Forest Farm Peace Garden	Hainault, Essex
Forest Gate Community Garden	London
FOSH - Friends of Stamford Hill Estate	London
Freightliners Farm	London
Friends of Abbey Gardens	London
Friends of Grenville Gardens (FROGG)	London
Friends of Harlesden Town Gardens	London
Friends of Myatts Field South	London
Garden of Earthly Delights	London
Glengall Wharf Garden	London
Global Generation	London
Grass Roots Forest School C.I.C (Community Interest Company)
Green Lane Primary and Nursery School	Old Malden
Growing Communities	London
Growing in Haringey (GiH)	London
Gurdwara Siri Guru Singh Sabha Hounslow	Hounslow
Hackney City Farm	London
Hackney Herbal CIC	London
Hammersmith Academy Garden	London
Hammersmith Community Gardens Association - Godolphin Road	London
Harris Academy Bermondsey	London
Hawksmoor Growing Club	London
Heathbrook Primary School	London
Hen Corner

Heston Action Group	London
Holly Lodge Centre	Richmond, Surrey
Incredible Edible Barnet	London
John Evelyn Community Garden	London
Jupiter Woods	London
Just FACT blueprint architect group coordinated by London Leap	Bethnal Green
Katherine Buchan Meadow Trust	London
Kentish Town City Farm	London
Kew Community Horticultural Learning Programme	Richmond
King Henry's Walk Garden	London
Kingsbury High School	London
Kipling Estate Community Garden

Lakeside Centre Garden	London
Lambourne End Centre	Abridge, Essex
Lee Manor Community Garden	London
Lee Valley Regional Park Authority Youth and Schools Service	Enfield
Lewisham Urban Farms	London
Living Under One Sun	London
Loughborough Farm	London
Magnolia Community Garden	London
Maiden Lane Community Centre Garden Project	London
Manor Farm Nature Space	London
Manor Junior School Ecogarden	London
Manorfield Primary School
Meadow Orchard Project	London
Meanwhile Gardens Community Association	London
MHA Communities South London	Croydon
MHA The Wilderness Garden	Croydon
MIND in Haringey	London
MindFood	London
Mitcham Orchard (part of Sustainable Merton)	London
Mobile Garden City	London
Mountford Growing Community	London
Mudchute Park and Farm	London
Museum of the Order of St John	London
my AFK Edible Garden Project
Myatt's Fields Park Project	London
MyYard	Bushey
Nightingale Community Academy (Tom's Farm)	London
Notting Hill Adventure Playground (Venture Centre)	London
Oasis Community Centre and Gardens (London)	London
Old Tidemill Wildlife Garden	London
Olden Community Garden	London
OrganicLea	London
Our Barn Community	Middlesex
Parents and Communities Together (PACT)	London
Parkfields Community Garden	Kingston upon Thames
Parkside Gardening Project
Peabody	Thamesmead
Phoenix Community Farm	London
Poets Corner Community Garden (Acton)	London
Ponders End Falcon Fields Allotments	Enfield
Priory Court Food Garden	London
Pritchard's Road Gardening Project	London
Putting Down Roots	London
Rainbow Grow	London
Refreshing Minds	London
Regent's Park Allotment Garden	London
Rhyl Kitchen Classroom C.I.C.	London
Roots4Life
Rosendale Gardens Tenant and Resident Association	London
Royal Foundation of St. Katharine	London
Save Newham City Farm	London
School Food Matters	London
Seeds for Growth	London
Slade Green Big Local	London
Social Orchards	Carshalton
South London Botanical Institute	London
Southwark Park Galleries (managed by the Bermondsey Artists' Group)	London
Sowing Seeds Allotment Project	London
Spa Hill Allotment Society Limited	London
Spitalfields City Farm	London
Spitalfields Crypt Trust	London
Springhallow School	London
Spurgeon Estate Communal Garden	London
St George The Martyr Church	London
St John's Churchyard/ St John's Waterloo	London
St Luke's Community Centre	London
St Mary's Secret Garden	London
Streatham Common Community Garden	London
Sufra NW London	London
Sufra NW London - St Raphaels Edible Garden	London
Sunnyside Community Gardens Association	London
Surrey Docks Farm	London
Sustainable Nutrition Academy	London
Sutton community farm	Wallington
Sweet Tree Farming For All	Mill Hill
Sydenham Garden	London
The Boiler House Community Space	London
The Bridge at Waterloo	London
The Deptford People Project	London
The Friends of Horsenden Hill	Perivale
The Friends of Park Hill Park	Croydon
The Grow Club - Company Drinks CIC	Barking and Dagenham
The London Horseplay Centre	London
The Paradise Cooperative	London
The Phoenix Garden	London
The Priory Farm	London
The Royal Parks	London
The Seeds Project and Seedling Gardening Group, Positively UK	London
The Triangle Adventure Playground Association	London
The Woodlands Farm Trust	London
Tower Hamlets Food Growing Network (Women's Environmental Network)	London
Trees for Cities (Edible Playgrounds)	London
Ubele	London
Union of Hackney Gardens	London
Urban Edible Gardens	London
Urban Growth Learning Gardens	LONDON
Vauxhall City Farm	London
Walpole Park Walled Garden	London
Walworth Garden	London
We Are Grow	London
We are Grow	London
Weirhall Road Community Open Space N17	London
Wellgate Community Farm	Essex
Wendelsworth Community Garden & Orchard	London
Whetstone Stray Allotments Community Plot	London
Wild Cat Wilderness	London
Wild Green E13	London
Wild Rangers	London
William Hobbayne Community Gardens Association	London
Wolves Lane Horticultural Centre	London
World Peace Garden Camden	
Yellow Qube CIC	London
Zaccheaus Project - Gardening Group	London