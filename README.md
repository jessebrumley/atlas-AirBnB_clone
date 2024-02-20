# AirBnb Clone - The Console

## Table of Contents
- [Usage](#usage)
- [Models](#models)
- [Engine](#engine)
- [Authors](#authors)

### Usage

To run the console you can execute the following command:  
python console.py  

You should see the console open, and be greeted by the prompt:  
(hbnb)  

After this, you can run the following included commands:  
- create <class_name> (creates a new instance of BaseModel and saves it to storage)  
Example: <em>create BaseModel</em>
- show <class_name> <instance_id> (prints string representation of given instance)  
Example: <em>show BaseModel 123</em>
- destroy <class_name> <instance_id> (deletes an instance)  
Example: <em>destroy BaseModel 123</em>
- all <class_name> (prints string representation of all existing instances)  
Example: <em>all BaseModel</em>
- update <class_name> <instance_id> <attribute_name> "<attribute_value>" (updates a given instance's given attribute with given value)  
Example: <em>update Basemodel 123 name "New Name"</em>
- quit (exits the program)
- EOF (handles EOF and exits)

### Models

Our console is built around several models that represent aspects of the AirBnB site. Each model inherits from the BaseModel class. Here is a brief description of each model:

<strong>BaseModel</strong>  
- The BaseModel class is the foundation for all the other models in our console. It includes the attributes <em>created_at</em> and <em>updated_at</em>, which track the creation and last modification times of instances.
- BaseModel also ensures that each instance has a unique identifier(id) upon instantiation.
- It also includes methods for saving the state of an instance to storage, using <em>save()</em>, and for converting an instance to a dictionary, using <em>to_dict()</em>.

<strong>User</strong>  
- The user model represents a user of the AirBnB platform.
- This model contains fields for user email, user password, along with a first name and a last name.

<strong>State</strong>  
- The state model represents the geographical state where cities are located.
- This model currently contains a field for the name of the state that the BnB would be located in.

<strong>City</strong>  
- The city model represents the city that the BnB would be located in.
- This model contains fields for the state_id (which will show what state its located in) and the name of the city.

<strong>Place</strong>  
- The place model represents the physical location that users could stay at / rent.
- This model contains fields for the city_id and state_id (to show the geographical location of the BnB).
- This model also has fields for the name and description of the place entity.
- The fields for number of rooms, number of bathrooms, max guests and price by night are included further down.
- Longitude and latitiude fields are included for precise location.
 - Finally amenity_ids is a list field to contain available amenities (to be set as amenity.id)

<strong>Amenity</strong>  
- The amenity model represents features and services available at a given location.
- This model has a field for the name of the amenities available.

<strong>Review</strong>  
- The review model represents user feedback about places.
- This model has fields for place_id (the place the user stayed at), user_id (the user who stayed there), and text (the actual content of the user's review)

### Engine
![Alt text](AirBnB_storage_flowchart.jpg?raw=true)

<strong>FileStorage</strong>
The FileStorage engine is an incredibly important part of our console, and is responsible for managing the persistent storage of our data models. It operates in the background, enabling the console to create, retrieve, update, and delete instances without direct interaction.  
  
  <strong>Key Features</strong>
   - Persistence: This engine stores data in a file-based system, ensuring that information is retained between sessions.
   - Serialization: It allows complex data types to be converted into JSON format, suitable for storage.
   - Deserialization: Converts stored JSON data back into usable Python objects when needed.

<strong>Implementation</strong>  
FileStorage uses a combination of Python's built-in file handling abilities and custom logic to manage our data. It uses the <em>UUID</em> module to generate unique id's for each model instance.

<strong>Usage</strong>  
To use the File Storage Engine, simply call the relevant methods provided by the engine. For example, to save a new instance to the file system, you would use the <em>save()</em> method, which serializes the instance and writes it to the appropriate file. Similarly, to retrieve all instances of a particular class, you would use the <em>all()</em> method, which reads the corresponding file and deserializes the data into Python objects.

### Authors

Clay Jones - https://github.com/clay-creates  
Jesse Brumley - https://github.com/jessebrumley