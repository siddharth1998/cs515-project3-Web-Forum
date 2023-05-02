# cs515-project3-Web-Forum

### Made by Chetan Jain and Siddharth Jain

### cjain1, sjain70  

## URL : https://github.com/siddharth1998/cs515-project3-Web-Forum


## Estimated Man Hours : 30 hours ( combining both bandwidth )

We also worked in shifts in with majority of time in overlapping

## Documentation

 
This is a Flask application that provides RESTful APIs for managing users and posts in a MongoDB database.

We thought if we published our api documentation of the baseline and extensions, it would be better for the TA to run them as it would reduce their work. So here's the published links:


#### Reference:
##### Postman published documentation for the users api:
<span style="background-color: #FFFF00">https://documenter.getpostman.com/view/12623814/2s93eU2DzZ</span>

##### Postman documentation for the posts api:
<span style="background-color: #FFFF00">https://documenter.getpostman.com/view/12623814/2s93eU2EXX</span>



### Base Line 

## 1.  Creating a Post

METHOD :: <code> POST </code>

ENDPOINT :: <code>/post</code>

PURPOSE :: Create a endpoint in which by sending an msg you can store the data into database and return some meta data. Meta data contains : 
<ol>
<li><b>the ID of the post</b></li><li><b>timestamp</b></li><li> <b>key</b></li> 
</ol>
 <i>Request Body</i> :: <br>

 ``` 
{
    "msg":"Hi there, how are you , why are feeling so sad "
}
 ```

 <i>Response</i> :: <br>
 ```
{
    "id": 2,
    "key": "12da79bc97910de3f688227b38c2334d",
    "timestamp": "2023-05-02T00:34:23.292160+00:00"
}
 ```

<p>User part: Now the task was to add user ID and User key ( something like a private key ) into the request body check if it is valid and post into the database. Now there will be metadata attached to the data in the database. Which you can see in the <code>GET</code>.</p> For example <br>
<i>Request Body</i> :: <br>

 ``` 
{
  "msg":"hi there",
  "key":"{{ukey}}",
  "user_id":"{{uid}}"
}
 ```

 <i>Response</i> :: <br>
 ```
{
    "id": 3,
    "key": "711fb108e10920d24774d82bfe90674c",
    "timestamp": "2023-05-01T18:11:42.141700+00:00"
}
 ```

 
STATUS CODES :: <br>
<code>200</code> -- When having sent correct request body <br>
<code>400</code> -- When having sent wrongly formated request body <br>
<code>404</code> -- When the user dose not exists while sending the request

## 2.  Getting a post information

METHOD :: <code> GET </code>

ENDPOINT :: <code>/post/{{ id }}</code> <br>
Note :: <i> Here the {{ id }} is the post id </i>

PURPOSE :: Create a endpoint in which by sending a request to the endpoint, the data can be retrieved : 


 <i>Response</i> :: <br>
 ```
{
    "id": 3,
    "key": "cca880dad0966bcf2bff10f0af35fd27",
    "timestamp": "2023-05-02T01:21:12.537814+00:00",
    "user_id": "3ad1116b5e753a75",
    "username": "pikachu"
}
 ```


<p>User part: Now if the post contains user data, then reponse will contain the username and user ID <br>

 <i>Response</i> :: <br>
 ```
{
    "id": 3,
    "msg": "hi there",
    "timestamp": "2023-05-02T01:21:12.537814+00:00",
    "user_id": "3ad1116b5e753a75",
    "username": "pikachu"
}
 ```
As you can see if i post using a user and retrive the data of the post using the post id I will get back the information of the user who posted it. 

STATUS CODES :: <br>
<code>200</code> -- When having sent request for a exsisting post<br>
<code>404</code> -- When  sent a request for a non exsisting post <br>
<!-- <code>404</code> -- When the user dose not exists while sending the request -->


## 3.  Deleting a post

METHOD :: <code> DELETE </code>

ENDPOINT :: <code>localhost:5000/post/{{p_id}}/delete/{{p_key}}</code> <br>
Note :: <i> Here the {{ p_id }} is the post id and {{p_key}} is post key</i>

PURPOSE :: Create a endpoint in which by sending a request to the endpoint, the deletion will occur on the basis of correct p_id and p_key pair: 


 <i>Response</i> :: <br>
 ```
{
    "id": 3,
    "key": "cca880dad0966bcf2bff10f0af35fd27",
    "timestamp": "2023-05-02T01:21:12.537814+00:00",
    "user_id": "3ad1116b5e753a75",
    "username": "pikachu"
}
 ```

ENDPOINT :: <code>localhost:5000/post/{{p_id}}/delete/{{u_key}}</code> <br>


<p>User part: When you send the correct {{p_id}} ( post id ) and correct {{u_key}} ( user key ) you will be able to get the information of the post with userdetails  <br>

 <i>Response</i> :: <br>
 ```
{
    "id": 4,
    "key": "45728255a0dd5b3ad3244ec1f40f1043",
    "timestamp": "2023-05-02T02:20:26.899674+00:00",
    "user_id": "3ad1116b5e753a75",
    "username": "pikachu"
}
 ```
As you can see if i post using a user and retrive the data of the post using the post id I will get back the information of the user who posted it. 

STATUS CODES :: <br>
<code>200</code> -- When having sent request for a exsisting post<br>
<code>404</code> -- When sent a request for a non exsisting post <br>
<code>403</code> -- When sent a request for a wrong key pair <br>

<!-- <code>404</code> -- When the user dose not exists while sending the request -->



### Extension:  

#### 1. Users and users keys

Endpoint: /user

HTTP Method: POST

Description: This API is used to create a new user with a unique username.

Request Body:

This API expects a JSON payload with the following keys:

username: A string representing the username of the user. It should be unique and have a length between 5 and 30 characters.

Example Request:
POST /user HTTP/1.1
Host: localhost:5000
Content-Type: application/json
{
"username": "johndoe"
}

Success Response:
If the request is successful, this API returns a JSON response with the following keys:

key: A unique token in hexadecimal format.
id: A unique token in hexadecimal format.
username: The username of the user.

Example Response:
HTTP/1.1 200 OK
Content-Type: application/json
{
"key": "3e47b3d3b4c9b2cc4d25ba68",
"id": "f7a0a72d23888d84",
"username": "johndoe"
}

Error Response:
This API returns an error response in the following cases:
The username is already taken.
The username is not valid.

In case of error, this API returns a JSON response with the following keys:

{
message: A string describing the error message.
}

Example Error Response:
HTTP/1.1 400 Bad Request
Content-Type: application/json
{
"message": "username needs a minimum length of 5 to 30 characters",
}

Implementation Details:

This API creates a new user by generating a unique key and id, and inserting the user data into a MongoDB collection. Before inserting the user data, it validates the username to check whether it is unique and has a valid format. If there is any error during the validation or the database operation, it returns an appropriate error response with an error message.

### 2. User profile

Update User, update an existing user's metadata.

Request - PUT /user

Request Body
{
"key": "<string>",
"username": "<string>",
"firstName": "<string>",
"lastName": "<string>"
}

key: Unique identifier of the user to be updated. Required.
username: New username for the user. Optional.
firstName: New first name for the user. Optional.
lastName: New last name for the user. Optional.

Response Body
{
"message": "Updated user metadata successfully"
}

Response Codes
200 OK: The user metadata was updated successfully.
400 Bad Request: The request is invalid or malformed.
404 Not Found: The user with the specified key does not exist.
500 Internal Server Error: An error occurred while processing the request.

Errors
ValidationError: The request is invalid or malformed.
InternalError: An error occurred while processing the request.

Get User and it's metadata.

Request - GET /user/{id}

This API endpoint returns the user object for the provided user ID.

id (required): The unique identifier for the user. It should be a 16-character string.

Response
200 OK: Returns the user object for the provided ID.
400 Bad Request: If the provided user ID is not valid.
404 Not Found: If the user does not exist with the provided ID.

Example Request

GET /user/1234567890123456
Example Response
{
"username": "johndoe",
"firstName": "John",
"lastName": "Doe",
"id": "1234567890123456"
}

Request Example
GET /user/1234567890123456

Response Example
{
"username": "johndoe",
"firstName": "John",
"lastName": "Doe",
"id": "1234567890123456",
}

### 3. Endpoint: POST /user/search

This endpoint allows you to search for a user in the database based on certain criteria such as username, first name or last name.

Request Body:
{
"username": "example_username",
"firstName": "example_first_name",
"lastName": "example_last_name"
}

Note: At least one of the fields (key, id, username, firstName, lastName) is required in the request body.

Responses:
200 OK: Returns the details of the user(s) matching the search criteria.
{
"id": "example id",
"key": "example key",
"username": "example_username",
"firstName": "example_first_name",
"lastName": "example_last_name"
}

400 Bad Request: Returned if the request body is invalid. It may contain the following messages:

'key is invalid'
'id is invalid
'username needs a minimum length of 5 to 30 characters'
'username can have only letters, digits, underscore, . or - characters'
'firstName needs to be between the length of 5 to 30 characters'
'firstName can have only letters, digits, underscore, . or - characters'
'lastName needs to be between the length of 5 to 30 characters'
'lastName can have only letters, digits, underscore, . or - characters'

404 Not Found: Returned if the user(s) matching the search criteria are not found in the database. It may contain the following message: 'User does not exist'

500 Internal Server Error: Returned if any internal error occurs. It may contain the following message: 'Internal server error'

 4. Date range base queries

This API endpoint accepts HTTP GET requests with a JSON payload containing a date range filter. The endpoint returns a list of posts that fall within the specified date range.

Method: GET - /post/date-range
Body:
{
"startDatetime": "YYYY-MM-DDTHH:mm:ss.sssZ",
"endDatetime": "YYYY-MM-DDTHH:mm:ss.sssZ"
}

startDatetime and endDatetime are ISO formatted timestamps representing the start and end of the date range respectively.

Response:
Status Code: 200 OK
Body:
{
"posts": [{
"title": "post_title",
"content": "post_content",
"timestamp": "YYYY-MM-DDTHH:mm:ss.sssZ",
},
...
]
}

The response body contains a list of posts that fall within the specified date range. Each post contains its title, content, timestamp, and author details.

Errors:
400 Bad Request: The request is malformed or missing a required parameter.
{
"message": "error message"
}

500 Internal Server Error: An unexpected error occurred.
{
"message": "Internal server error"
}

  

## 5. Persistence

The Persistence Extension is designed to add persistence to the baseline behaviour. With this extension, the server becomes persistent, which means that it will hold onto posts between restarts.

#### Requirements:
Python 3.6 or higher
Flask 2.0 or higher

With persistence, your server becomes much more robust and reliable.

  
## Test cases:

Running the Tests

To run users api test - ``newman users_collection.json``
To run posts api test - ``newman cs515.postman_collection.json``

### User - POST - Create user
  
##### Test Case 1: Create User - Username Length is Lesser Than 5 Characters

This test case verifies that creating a user with a username that is less than 5 characters in length results in a 400 Bad Request response.

Steps:
Send a POST request to the /user endpoint with a JSON payload containing a username that is less than 5 characters long. Assert that the response status code is 400.

##### Test Case 2: Create User - Username Contains Invalid Characters

This test case verifies that creating a user with a username that contains characters other than letters, digits, underscore, period, or hyphen results in a 400 Bad Request response.

Steps:
Send a POST request to the /user endpoint with a JSON payload containing a username that contains an invalid character. Assert that the response status code is 400.

##### Test Case 3: Create User - Creates a User Record

This test case verifies that creating a user with a valid username results in a 200 OK response and returns the created user's record.

Steps:
Send a POST request to the /user endpoint with a JSON payload containing a valid username. Assert that the response status code is 200. Assert that the response body is an object. Assert that the response body contains the id, key, and username fields. Extract the key field from the response body and save it to the environment variable userKey.

##### Test Case 4: Get User By ID - Returns the User Record

This test case verifies that retrieving a user by ID returns the correct user record.

Steps:
Send a GET request to the /user/{{userId}} endpoint, where {{userId}} is the ID of a previously created user. Assert that the response status code is 200. Assert that the response body is an object. Assert that the response body contains the id, key, and username fields. Assert that the key field in the response body matches the userKey environment variable.

##### Test Case 5: Delete User By ID - Deletes the User Record
This test case verifies that deleting a user by ID removes the user record from the database.

Steps:
Send a DELETE request to the /user/{{userId}} endpoint, where {{userId}} is the ID of a previously created user. Assert that the response status code is 204.

Send a GET request to the /user/{{userId}} endpoint to verify that the user record has been deleted. Assert that the response status code is 404.

 
### User - PUT - Update user

##### Test #1 - Test if user metadata can be updated based on a key.

Steps:
Send a PUT request to the endpoint 127.0.0.1:5000/user with a valid user key and updated user metadata in the request body. Check if the response status code is 200. Check if the response contains a JSON object. Check if the response contains a message property of type string.

Expected Result: User metadata should be updated based on the provided key.

  
##### Test #1.1 - Test if the API returns an error message if a username is already in use.

Steps:
Send a PUT request to the endpoint 127.0.0.1:5000/user with a user key and updated user metadata, where the username is already in use by another user.
Check if the response status code is 400. 

Expected Result: API should return an error message indicating that the username is already in use.

##### Test #2 - Test if the API returns an error message when user key is not provided.
Steps: 
Send a PUT request to the endpoint 127.0.0.1:5000/user with updated user metadata, where the user key is not provided in the request body.
Check if the response status code is 400.

Expected Result: API should return an error message indicating that the user key is required.

##### Test #3: Test if the API returns an error message when an invalid user key is provided.
Steps:
Send a PUT request to the endpoint 127.0.0.1:5000/user with updated user metadata and an invalid user key.
Check if the response status code is 400.

Expected Result: API should return an error message indicating that the user key is invalid.

##### Test #4 - This test case verifies that the username should have a minimum length of 5 and a maximum length of 30 characters.

Steps:
Send a PUT request to the URL 127.0.0.1:5000/user.
Set the Request Body to: {
"key": "140969aecf6cbaa638321b4a",
"firstName": "john d",
"lastName": "senior",
"username": "john"
}
Verify that the Response Status Code is 400.
Verify that the Response Body contains the following message: "Update User: Username needs a minimum length of 5 to 30 characters".

##### Test #5 - This test case verifies that the username can only have letters, digits, underscore, . or - characters.

Steps:
Send a PUT request to the URL 127.0.0.1:5000/user.
Set the Request Body to: {
"key": "140969aecf6cbaa638321b4a",
"firstName": "john d",
"lastName": "senior",
"username": "john?"
}

Verify that the Response Status Code is 400.
Verify that the Response Body contains the following message: "Update User: username can have only letters, digits, underscore, . or - characters".

##### Test #6 - This test case verifies that the firstName should have a minimum length of 5 and a maximum length of 30 characters.

Steps:
Send a PUT request to the URL 127.0.0.1:5000/user.
Set the Request Body to: {
"key": "140969aecf6cbaa638321b4a",
"firstName": "j",
"lastName": "senior",
"username": "john-jr"
}

Verify that the Response Status Code is 400.
Verify that the Response Body contains the following message: "Update User: firstName needs to be between the length of 5 to 30 characters".

##### Test #7 - This test case verifies that the firstName can only have letters, digits, underscore, . or - characters.

Steps:
Send a PUT request to the URL 127.0.0.1:5000/user.
Set the Request Body to: {
"key": "140969aecf6cbaa638321b4a",
"firstName": "john d*",
"lastName": "senior",
"username": "john-jr"
}
Verify that the Response Status Code is 400.

Verify that the Response Body contains the following message: "Update User: firstName can have only letters, digits, underscore, . or - characters".

##### Test #8: Update User: lastName needs to be between the length of 5 to 30 characters

Steps:
Send request body: {
"key": "140969aecf6cbaa638321b4a",
"firstName": "john d",
"lastName": "s",
"username": "john-jr"
}

Expected Response: Status Code: 400

Error message and status in response:
lastName needs to be between the length of 5 to 30 characters
status: 400

##### Test #9: Update User: lastName can have only letters, digits, underscore, . or - characters

Steps:
Send request body: {
"key": "140969aecf6cbaa638321b4a",
"firstName": "john d",
"lastName": "senior%",
"username": "john-jr"
}

Expected Response:
Status Code: 400

Error message and status in response:
lastName can have only letters, digits, underscore, . or - characters
status: 400

##### Test #10: Update User: User does not exist with the given key

Steps:
Send request body: {
"key": "140969aecf6cbaa638321b4a",
"firstName": "john d",
"lastName": "senior",
"username": "john-jr"
}

Expected Response: Status Code: 404

Error message and status in response:
User does not exist with the given key
Status is 404

  
### User - POST - Search user by key

##### Test #1 - This test case verifies the ability of the API to search for a user by key.

Steps: 
Send a POST request to the URL localhost:5000/user/search with the key parameter set to {{userKey}}.
Verify that the response status code is 200 OK.
Verify that the response is an object and contains the following fields:

id: a string representing the unique identifier of the user.
key: a string representing the key of the user.
username: a string representing the username of the user.
firstName: a string representing the first name of the user.
lastName: a string representing the last name of the user.

Store the id, firstName, and lastName values from the response in environment variables.

### User - POST - Search user by Id 

##### Test #2 - This test case verifies the ability of the API to search for a user by ID.

Steps:
Send a POST request to the URL localhost:5000/user/search with the id parameter set to the value stored in the userId environment variable.
Verify that the response status code is 200 OK.
Verify that the response is an object and contains the following fields:

id: a string representing the unique identifier of the user.
key: a string representing the key of the user.
username: a string representing the username of the user.
firstName: a string representing the first name of the user.
lastName: a string representing the last name of the user.

### User - POST - Search user by 2 non-unique attributes 

##### Test #3 - This test case verifies the ability of the API to search for a user by their first and last name.

Steps:
Send a POST request to the URL localhost:5000/user/search with the firstName parameter set to the value stored in the userFirstName environment variable and the lastName parameter set to the value stored in the userLastName environment variable.
Verify that the response status code is 200 OK.

### User - POST - Search user by 1 non-unique attributes

##### Test #4 - This test case verifies the ability of the API to search for a user by their username.

Steps:
Send a POST request to the URL localhost:5000/user/search with the username parameter set to a non-unique value.
Verify that the response status code is 200 OK.
Verify that the response is an object and contains the following fields:

id: a string representing the unique identifier of the user.
key: a string representing the key of the user.
username: a string representing the username of the user.
firstName: a string representing the first name of the user.
lastName: a string representing the last name of the user.

#### User - POST - Search non-existent user 

##### Test #5

Steps: 
Send a POST request to "localhost:5000/user/search" with request body {"firstName": "not exist"}.
Verify that the response has a status code of 404.

#### Posts - POST - Search by date range

##### Test #1 - Invalid startDatetime

Steps:
Send a GET request to "localhost:5000/post/date-range" with request body {"startDatetime": "not exist"}.
Verify that the response has a status code of 400.

##### Test #2 - All posts after the startDatetime
Steps:
Send a GET request to "localhost:5000/post/date-range" with request body {"startDatetime": "2023-05-01T05:00:12.649Z"}.
Verify that the response has a status code of 200.
Verify the response contains posts that has timestamp 

##### Test #3 - All posts before the endDatetime
Steps:
Send a GET request to "localhost:5000/post/date-range" with request body {"endDatetime": "2023-04-28T06:11:38.001Z"}.
Verify that the response has a status code of 200.

##### Test #4 - All posts between the startDatetime and endDatetime
Steps:
Send a GET request to "localhost:5000/post/date-range" with request body {"startDatetime": "2023-05-01T05:00:12.649Z", "endDatetime": "2023-05-01T05:00:12.649Z"}.
Verify that the response has a status code of 200.

 
 ## Create Posts - /post

##### Test #1 
This test case tests if the POST request to create a new post is successful and returns a 200 status code. It also extracts the id and key values from the response and sets them as environment variables.

Steps:
Send a POST request to http://127.0.0.1:5000/post with the request body:
{
"msg":"hi there"
}
Check if the response has a status code of 200.

Delete - DELETE - Valid post key - /post/{{p_id}}/delete/{{key}} - Deleting created post

This test case tests if the DELETE request to delete a created post is successful and returns a 200 status code.


Test Steps:
Send a DELETE request to localhost:5000/post/{{p_id}}/delete/{{p_key}}.

Check if the response has a status code of 200.

User - POST - Create user - Test #2

This test case tests if the POST request to create a new user is successful and returns a 200 status code. It also extracts the id and key values from the response and sets them as environment variables.

 
Test Steps:
Send a POST request to 127.0.0.1:5000/user with the request body:
{
"username": "godfather1"
}
Check if the response has a status code of 200.

Posts - POST - User Post without the key - /post - Test #3

This test case tests if the POST request to create a new post without a key is unsuccessful and returns a 400 status code.

  

Test Steps:

  

Send a POST request to http://127.0.0.1:5000/post with the request body:


{

"msg":"hi there",

"user_id": {{uid}}

}

Check if the response has a status code of 400.

  

Test case 1: Posts - POST - User Post without the id - /post - Test #4

This test case tests whether a user can post a message to the API without specifying an ID. The test expects a response with a status code of 400, indicating a bad request.

  

Test case 2: Posts - POST - User sending the post - /post - Test #5

This test case tests whether a user can post a message to the API with the required fields. The test expects a response with a status code of 200, indicating a successful request. Additionally, the test extracts the ID and key fields from the response and saves them to the Postman environment for use in subsequent requests.

  

Test case 3: Posts - POST - User Post without body - /post - Test #2

This test case tests whether a user can post a message to the API without specifying any fields. The test expects a response with a status code of 400, indicating a bad request.

  

Test case 4: Posts - POST - Post with integer - /post - Test #2

This test case tests whether a user can post a message to the API with an integer value in the message field. The test expects a response with a status code of 400 and an error message indicating that the message value should be a string.

  

Test #1: Viewing an existing post

  

Set up the environment by assigning a valid post ID to p_id.

Send a GET request to /post/{{p_id}}.

Expect the response to have a status code of 200.

Expect the response JSON data's id field to match the value of p_id.

  

Test #2: Viewing a non-existent post

  

Set up the environment by assigning a non-existent post ID to p_id (e.g., 100000000).

Send a GET request to /post/{{p_id}}.

Expect the response to have a status code of 404.

Expect the response JSON data's err field to be equal to "id not found".

Test Plan for Endpoint: GET /search/{{query}}

  

Test #1: Searching for a non-existent key

  

Send a GET request to /search/```@.

Expect the response to have a status code of 200.

Expect the response JSON data's result field to be an empty array.

  

Test #2: Searching for an existing key

  

Send a GET request to /search/hi.

Expect the response to have a status code of 200.

Expect the response JSON data's result field to be an array with a length greater than zero.

Test Plan for Endpoint: DELETE /post/{{p_id}}/delete/{{key}}

  

Test #1: Deleting a post with an invalid key

  

Set up the environment by assigning a valid post ID to p_id.

Send a DELETE request to /post/{{p_id}}/delete/invalid_key.

Expect the response to have a status code of 400.

Expect the response JSON data's err field to be equal to "invalid key".

  

#### Reference:
##### Postman published documentation for the users api:
https://documenter.getpostman.com/view/12623814/2s93eU2DzZ

##### Postman documentation for the posts api:
https://documenter.getpostman.com/view/12623814/2s93eU2EXX