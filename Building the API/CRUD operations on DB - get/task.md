## DAL: GET

CRUD stands for Create, Read/Retrieve, Update and Delete and these are the four basic operations that can be performed 
on persistence storage (database). HTTP methods can 
work as CRUD operations. The standard ones are as follows:

- POST: Creates a new resource
- GET: Reads/Retrieve a resource
- PUT: Updates an existing resource
- DELETE: Deletes a resource

In this task, we are going to add a simple function to our DAL, which will be retrieving data from the shelve database. 
This function will be called from the API by the `get` method of the `DeviceInventory` Resource.

1. Implement the `get` method that will take all the data from the shelf and return a dictionary of devices (its structure should be the same as in the 
first task of this lesson). Remember that shelve objects can be accessed like a dictionary.