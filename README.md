# vernacularAssignment


Creation of a Django app runnable via Docker.

# Assignment Description:
  1. POST API to validate a slot with a finite set of values.
  2. POST API to validate a slot with a numeric value extracted and constraints on the value extracted.
  3. Creating a Dockerfile
  4. Hosting the code on GitHub and sharing the same
  
  # Assignment Execution:
  1. Given Input of the API is valid request
  2. Here while validating "values" data weare only checking value of each object entry
    "values": [
    {
      "entity_type": "id",
      "value": "college"
    }
    ]
  3. In case both support_multiple and pick_first are set to True or set to False, support_multiple will be prioritized.
  4. pick_first will pick the first valid value in the values list as a String, ignoring the invalid values in the list.
  5. support_multiple will pick all the valid values in the list as a List, ignoring the invalid values in the list.
  6. invalid_trigger is raised in the response even if there is one invalid value or no values in the values list.
      
# Build & Run Image:

  1. Build image.
    Use the below command to build the application image from GitHub repository.
    docker build -t vernacularassignment_app:latest https://github.com/chinmoysihi/vernacularAssignment.git#main:.
     The ImageName is vernacularassignment_app and TagName is latest as per the above command.

  2) Run image.
    Use the below command to run the docker image once it is built
    docker run -p 8000:8000 vernacularassignment_app:latest

Note: In case of any permission issues in linux, please run the above commands with sudo.

# Making Post Requests

## 1. POST API to validate a slot with a finite set of values.
URL : http://localhost:8000/validate/finite_set/
![image](https://user-images.githubusercontent.com/33445883/97799091-b7696b00-1c51-11eb-93ad-f3e50c15abcb.png)

## 2. POST API to validate a slot with a numeric value extracted and constraints on the value extracted.
URL : http://localhost:8000/validate/numeric_set/
![image](https://user-images.githubusercontent.com/33445883/97799129-07e0c880-1c52-11eb-95de-c655fe1a9f7a.png)




# Image of Docker
Size of the image : 84.6MB
![image](https://user-images.githubusercontent.com/33445883/97798976-ef23e300-1c50-11eb-83d2-2f5f021590f6.png)



