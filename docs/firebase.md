# Intro to Backend Development
_Written by Curtis Lee, pictures by Ravi Patel._

## Slides

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRXBqF9I6MXXwBKcu45NoCoyln25HrDJi9zKSZkGfG9stEYkd0YLoFFBT-zdKhrTAxJbKU02XXR1s_t/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Fundamentals

### What is Full Stack?

It boils down to three (3) concepts:

1. **Frontend** software that the user sees and interacts with.
2. **Backend** software that can handle specific requests and dynamically sends/recieves information to/from the user.
3. **Database** that stores pretty much all information our app uses.

There are endless configurations depending on the application. Sometimes, these components may be combined or further seperated to varying degrees. 
Regardless, all components must work together to produce a web app. 

Imagine a trinity of cards: **Frontend**, **Backend**, and **Database**. A developer that holds all three cards is said to have the "**Full Stack**", and thus can build a complete web app.

### What is Backend?

In traditional web development, backend software runs the "business logic" of our app. For example, a basic workflow may be like this:

1. The user fills out a login form on our app.
2. The user's browser sends a login request + the credentials to the backend server.
3. The backend recieves this information.
4. The backend queries the database to see if the user exists.
5. If the user exists, see if username & password match.
6. If everything is correct, send our content back to the user. Otherwise, send an error message.

Setting up a backend server is usually not easy. We would need to have extensive knowledge of setting up servers, networking, operating systems, and software. And that's before we even write any code, which may also require mastering multiple programming languages!

This is not feasible without the proper expertise and lots of time. So we will not be doing that. 

Instead, we will leverage **Cloud Services** that do the hard work for us, so we can better focus on our ideas.

## Intro to Firebase

!!! quote
    Firebase is Backend as a Service ( BaaS ) by Google.

Firebase is Google's solution to the problem. Firebase has reduced the entire **Backend + Database** stack into simpler services that we can rent out. Essentially, we are outsourcing all the hard technical work to Google.

### Getting Started

Using Firebase is comparable to using any other Google cloud service like Gmail or Drive. First, we create a **Project** for our product. Then we can add different services such as **Realtime Database** or **Authentication** and create keys to be used by one or more **Apps** utilizng our Project's services.

#### Creating a Project

1.  Sign in to [firebase.google.com](https://firebase.google.com/) (feel free to use your UCSD account)

2.  Click **Go to Console** in the top right corner.

3.  Click **Add Project**.

4.  Fill out the forms and continue.
    1. Any name is ok. I recommend _ECE196-Fall2020-IOT-YourName_.
    2. Google Analytics is optional. We won't be using it, but it could be nice to have if we further develop the app later.
    3. Accept terms and conditions.

5.  Once everything is set up, it should look something similar to this.

![](https://lh6.googleusercontent.com/Uk1D4WbEufLgK8wvS6Tpr2DyEW_lRnUAVz8vUy_P80Wc-BtX3rKisuyLvin_Pn8x50vzD7RSbpG-Sg47NMkKr1smTg29LbO-BaTKHuuv8_cVPeFHmv1WT3JGLH5ye0KmZi_P5cFL)

#### Adding Collaborators

1.  To add collaborators to the project, click on the **Settings** icon located on the top left. 
2.  Select **Users and permissions**.
3.  Click the **Add member** button.
4.  As for roles, select either **Owner** or **Editor**. This can always be changed later.
5.  Once the member is added, they should receive an email invitation to join.

### Realtime Database

#### Choosing a Database

Firebase offers two different products for our Database needs. 

For the Free Plan as of 2020, here are the key similarities and differences:

Spec | Realtime | Firestore
---------|----------|---------
Type| NoSQL| NoSQL
Structure|Basic JSON| Documents & Collections
Storage| 10 GB| 10 GB |
Bandwidth| 10GiB/month | 10GiB/month
Simultaneous Connections| 100 max| No limit
Document writes | No limit | 20K/day
Document reads | No limit| 50K/day
Document deletes | No limit| 20K/day

!!! info "Read More"
    * [Cloud Firestore vs Realtime Database](https://firebase.google.com/docs/database/rtdb-vs-firestore)
    * [Firebase Pricing plans](https://firebase.google.com/pricing)
    * [SQL vs NoSQL](https://www.mongodb.com/nosql-explained/nosql-vs-sql)

For our application, we will pick **Realtime Database**, for these reasons:

* Basic JSON structure is easy to learn
* Not many users, but document I/O adds up fast.

#### Creating a Database

1. Open the **Realtime Database** service on the sidebar:

    ![](realtime-db-sidenav.png)

2.  Start in **Test Mode**.

    ![](https://lh5.googleusercontent.com/kOvoPWYkoMVs0Dn9kkAwimnZ8TScdBc_R54oLHmhbGXQ0MrrLlhmIop1qC-vMwQoTb5LtrB-0AgAaIDlSDZnAhgoKEnmFPTggTAx5PXvFrizy-8m4ygPedXT3a-RR5SU-zCTQ-Bv)

3.  Click on the **Rules** tab and verify read and write access is set to `true`.
   
    ![](https://lh3.googleusercontent.com/p0bQm-l1TuitaagDSDMB6n1V_M950JddpQQ7L7YHUNxv8lpHazUmkW3JIThI18o4DWp8smniKnj8CWeFhvf4yvdsn7-qcVgOw6Q2V-WB7J-VeVzN4XK5nUts-vWf2Rz5LQyJHLN0)

### Obtaining Keys

#### Adding a Service Account

To connect our Raspberry Pi to Firebase, we need to generate a Service Account key to use Firebase Admin SDK. 

1. Click on the project's **Settings** icon and click on **Project Settings**
2. Navigate to the **Service Accounts** tab.
3. Click **Generate new Private Key**.
    ![](https://lh5.googleusercontent.com/0iqy0J5bxSS5JDrDVZf9Iv6F3p0MyTAHkYqbAIMUhUMA7gii5wNjQAxKas5dmpJ_YH83Yf2rMGPijlMt6UOTiSMedqF7UgsFMQQxuNCY2CI6zP6knESJYJuVSJ4jA5cFS0_1_fIU)
4. Save this project key somewhere where we can later copy it to the Raspberry Pi.

!!! Warning
    Your private key gives access to your project's Firebase services. Keep it confidential and never store it in a public repository. Store this file securely, because your new key can't be recovered if lost.

    If using Git, always add the name of this file to the project's .gitignore.

#### Adding an App

1. Also in **Settings**, under **General** tab and **Your Apps** section, click **Add App**. Select the **Web** platform.
2. Fill out the form
    1. Any name is ok. I recommend _Web App_.
    2. We won't be using Firebase Hosting for now. (instead we'll use GitHub Pages later on)
3. It should now spit out some info under **Add Firebase SDK**. The important part we care about is the `var firebaseConfig` dictionary. We can always come back to view this information anytime. 

        const firebaseConfig = {
            apiKey: ...
            authDomain: ...
            databaseURL: ...
            projectId: ...
            storageBucket: ...
            messagingSenderId: ...
            appId: ...
            measurementId: ...
        };

We won't need this App key until the Frontend portion.

!!! info
    Technically, none of the `var firebaseConfig` fields are sensitive information. In fact, this information will later be necessary for the end user to access our app. It is OK to commit this to the Git repository.

## Connecting to Firebase
To send data to the cloud, our Raspberry Pi needs to connect to Firebase.

We first import the libraries and initialize Firebase Admin:

    import firebase_admin
    from firebase_admin import credentials
    cred = credentials.Certificate( 'PATH_TO_FIREBASE_KEY' )
    firebase_admin.initialize_app( cred, { 'databaseURL':  'LINK_TO_DATABASE_URL' } )

* **replace PATH_TO_FIREBASE_KEY** with the appropriate path
* **replace LINK_TO_DATABASE_URL** with the appropriate URL

We also need to import the library for database and get a Reference.

    from firebase_admin import db
    db_ref = db.reference( "PATH_TO_REFERENCE" )
    db_ref.set( VALUE )
    data = db_ref.get()

* **replace PATH_TO_REFERENCE** with the appropriate path
* **replace VALUE** with the appropriate value

#### Complete Code

Should look similar to this:

    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import adafruit_dht
    import board
    import time

    dht_pin = board.D4
    dht_sensor = adafruit_dht.DHT22(dht_pin)

    cred = credentials.Certificate( 'PATH_TO_FIREBASE_KEY' )
    firebase_admin.initialize_app( cred, { 'databaseURL':  'LINK_TO_DATABASE_URL' } )

    while True:
        temp = dht_sensor.temperature
        hum = dht_sensor.humidity

        print("Temperature =", temp, 'C')
        print("Humidity =", hum, '%')

        temp_ref = db.reference( "sensor/temperature" )
        temp_ref.set( temp )
        hum_ref = db.reference( "sensor/humidity" )
        hum_ref.set( hum )

        time.sleep( 10 )