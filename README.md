## Ex04 Places Around Me
# Date: 7.12.2024
# AIM
To develop a website to display details about the places around my house.

## DESIGN STEPS
# STEP 1
Create a Django admin interface.

# STEP 2
Download your city map from Google.

# STEP 3
Using tag name the map.

# STEP 4
Create clickable regions in the image using tag.

# STEP 5
Write HTML programs for all the regions identified.

# STEP 6
Execute the programs and publish them.

# CODE
# 1.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Map with 5 Locations</title>
</head>
<style>
.no-scroll {overflow:hidden;}
</style>
<body>
    <img src="img1.png" usemap="#gmap">

    <map name="gmap">
        <area coords="374,620,237,520" shape="rect" href="loc2.html" alt="kal">
        <area coords="761,580,991,618" shape="rect" href="loc1.html" alt="marina">
        <area coords="1141,298,1276,357" shape="rect" href="loc4.html" alt="Rockpoint">
        <area coords="542,233,518,341,719,403,805,465,863,509,912,346,764,279" shape="poly" href="loc3.html" alt="river">
        <area coords="531,744,721,832" shape="rect" href="loc5.html" alt="memorial">
    </map>
</body>
</html>
```
# 2.
``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marina Beach</title>
</head>
<body>
    <h1>Marina Beach</h1>
    <img src="marina (1).png" alt="View of Marina Beach" style="width:100%; max-width:600px;">
    <p>Marina Beach is located in Chennai, Tamil Nadu, India. It is one of the longest urban beaches in the world, stretching along the Bay of Bengal. It is a popular destination for both locals and tourists.</p>
    <h2>Highlights</h2>
    <p>
        - Length: Approximately 13 km (8 miles). <br>
        - Known for its stunning sunrises and vibrant atmosphere. <br>
        - Features attractions like the Marina Lighthouse and local food stalls. <br>
        - Perfect for walking, jogging, and relaxing.
    </p>
    <h2>Visit</h2>
    <p>The best time to visit Marina Beach is early morning or evening to enjoy the cool breeze. It is easily accessible by public transport in Chennai.</p>
</body>
</html>
```
# 3.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>University of Madras</title>
</head>
<body>
    <h1>University of Madras</h1>
    <img src="uofm.jpeg" alt="University of Madras Building" style="width:100%; max-width:600px;">
    <p>
        The University of Madras, established in 1857, is one of India's oldest and most prestigious universities. 
        Located in Chennai, Tamil Nadu, the university has a rich legacy of academic excellence and cultural heritage.
    </p>
    
    <h2>Key Features</h2>
    <p>
        The university is renowned for:<br>
        - A wide range of undergraduate, postgraduate, and doctoral programs.<br>
        - Distinguished alumni who have excelled in various fields such as science, literature, and public service.<br>
        - A beautiful campus featuring historic buildings and state-of-the-art facilities.<br>
        - Research contributions in diverse disciplines.
    </p>
    
    <h2>Visitor Information</h2>
    <p>
        The main campus is situated near Marina Beach in Chennai, Tamil Nadu. Visitors are welcome to explore the historic architecture and the university’s library. 
        Timings for visits may vary, and prior permission may be required for specific areas.
    </p>
    
    <h2>Significance</h2>
    <p>
        The University of Madras is a symbol of academic heritage and progress in Tamil Nadu. It continues to play a pivotal role in shaping the intellectual and cultural landscape of the region.
    </p>
</body>
</html>
```
# 4.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coovam River</title>
</head>
<body>
    <h1>Coovam River</h1>
    <img src="cooo.jpg" alt="View of Marina Beach" style="width:100%; max-width:600px;">
    <p>The Coovam River, also known as the Kuem River, is a seasonal river that flows through the city of Chennai, Tamil Nadu. It plays a significant role in the city's water system, but over time, it has become highly polluted due to industrial waste and untreated sewage.</p>
    
    <h2>Key Features</h2>
    <p>Some of the notable features of the Coovam River are:</p>
    <p>
        - Length: Approximately 72 kilometers (45 miles).<br>
        - Originates from the Poonamallee area, flowing through the heart of Chennai before emptying into the Bay of Bengal.<br>
        - Historically used for irrigation and as a source of water for Chennai.<br>
        - Over the yAears, its water quality has been significantly impacted by urbanization and pollution.
    </p>
    
    <h2>Environmental Impact</h2>
    <p>The Coovam River has faced severe pollution issues due to the growth of industrial zones along its banks. The river receives untreated sewage and industrial effluents, which have led to a decline in its ecological health. Efforts to clean and restore the river have been ongoing in recent years to improve water quality and mitigate environmental damage.</p>

    <h2>Significance</h2>
    <p>Despite its current state, the Coovam River remains an important geographical and historical feature in Chennai. The river was once an important waterway, and its revival could contribute significantly to the city's environmental and water management systems.</p>
</body>
</html>
```
# 5.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rockpoint</title>
</head>
<body>
    <h1>Rockpoint</h1>
    <img src="rock.jpg" alt="View of Marina Beach" style="width:100%; max-width:600px;">
    <p>Rockpoint is a scenic and popular location known for its natural beauty and panoramic views. Whether it’s a hilltop, a coastal view, or a historic landmark, Rockpoint has become a favorite destination for travelers and nature enthusiasts alike.</p>
    
    <h2>Key Features</h2>
    <p>Some of the key highlights of Rockpoint include:</p>
    <p>
        - Breathtaking views of the surrounding landscape or sea.<br>
        - A great spot for photography, nature walks, and sightseeing.<br>
        - A rich history or folklore associated with the site.<br>
        - Popular with tourists, hikers, and those seeking a peaceful retreat.
    </p>
    
    <h2>Visitor Information</h2>
    <p>Rockpoint is easily accessible by car, bus, or even on foot for those looking to enjoy a hike. The best time to visit is during the cooler months, making it perfect for outdoor activities.</p>

    <h2>Significance</h2>
    <p>Rockpoint holds cultural, historical, or ecological importance depending on its location. It provides a glimpse into the region’s natural beauty and heritage, making it a must-visit destination for anyone exploring the area.</p>
</body>
</html>
```
# 6,
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puratji Thaivi Dr. J. Jaya Memorial</title>
</head>
<body>
    <h1>Puratji Thaivi Dr. J. Jaya Memorial</h1>
    <img src="Jayalalitha_Memorial.jpg" alt="View of Marina Beach" style="width:100%; max-width:600px;">
    <p>The Puratji Thaivi Dr. J. Jaya Memorial is a memorial dedicated to Dr. J. Jayalalithaa, the former Chief Minister of Tamil Nadu. The memorial honors her contributions to the state of Tamil Nadu and her legacy as a beloved leader, often referred to as "Amma" by her supporters.</p>

    <h2>About Dr. J. Jayalalithaa</h2>
    <p>Dr. J. Jayalalithaa was a prominent Indian politician, actress, and the Chief Minister of Tamil Nadu for several terms. She was known for her dynamic leadership, social welfare initiatives, and efforts to improve the lives of the people in Tamil Nadu. Her leadership transformed the state's social and economic landscape.</p>

    <h2>Key Features of the Memorial</h2>
    <p>The Puratji Thaivi Dr. J. Jaya Memorial includes:</p>
    <p>
        - A statue of Dr. Jayalalithaa, depicting her as a symbol of strength and leadership.<br>
        - A place for her supporters and the public to pay tribute.<br>
        - A museum section showcasing her life, achievements, and political career.<br>
        - Gardens and spaces for public gatherings and cultural events.
    </p>

    <h2>Visitor Information</h2>
    <p>The memorial is located in Chennai, Tamil Nadu, and is open to the public. It is a place of remembrance and reflection for those who admire Dr. Jayalalithaa's legacy. Visitors can explore the various sections of the memorial, learn about her life, and pay their respects.</p>

    <h2>Significance</h2>
    <p>Dr. Jayalalithaa's memorial stands as a testament to her remarkable career and the deep connection she had with the people of Tamil Nadu. The memorial is a place where her supporters and others can come together to honor her contributions and remember her leadership.</p>
</body>
</html>
```

# OUTPUT 
# 1
![Screenshot 2024-12-06 131656](https://github.com/user-attachments/assets/95a83230-ce79-46ed-b831-feb1ef86d0c5)
# 2
![Screenshot 2024-12-06 131755](https://github.com/user-attachments/assets/baf7919b-34f9-435a-a2d0-b2291611bbea)
# 3
![Screenshot 2024-12-06 131905](https://github.com/user-attachments/assets/b708a722-f2a1-4c86-ab77-6a8371b101d4)
# 4
![Screenshot 2024-12-06 131921](https://github.com/user-attachments/assets/5b18d549-7e3a-48de-aa1d-2d90ec0a9c9f)
# 5
![Screenshot 2024-12-06 131940](https://github.com/user-attachments/assets/0bcc5bd2-99f8-477b-bea3-8a1c8ee72b6e)
# 6
![Screenshot 2024-12-06 131955](https://github.com/user-attachments/assets/ab44eb18-a8b9-47f5-80d7-86998424a14e)

## RESULT

# The program for implementing image maps using HTML is executed successfully.
