# Video_Project

### API Documentation

#### Endpoints

1. **Create Video Project**
   - **URL:** `/api/`
   - **Method:** POST
   - **Description:** Create a new video project.
   - **Request Body:**
     ```json
     {
         "title": "Sample Title",
         "description": "Sample description for the video project.",
         "creation_date": "2024-05-15",
         "status": "active"
     }
     ```
   - **Response:**
     - **Status Code:** 201 Created
     - **Response Body:**
       ```json
       {
           "id": 1,
           "title": "Sample Title",
           "description": "Sample description for the video project.",
           "creation_date": "2024-05-15T00:00:00Z",
           "status": "active"
       }
       ```

2. **Retrieve Video Project**
   - **URL:** `/api/{id}/`
   - **Method:** GET
   - **Description:** Retrieve details of a specific video project.
   - **Response:**
     - **Status Code:** 200 OK
     - **Response Body:**
       ```json
       {
           "id": 1,
           "title": "Sample Title",
           "description": "Sample description for the video project.",
           "creation_date": "2024-05-15T00:00:00Z",
           "status": "active"
       }
       ```

3. **Update Video Project**
   - **URL:** `/api/{id}/`
   - **Method:** PUT
   - **Description:** Update an existing video project.
   - **Request Body:**
     ```json
     {
         "title": "Updated Title",
         "description": "Updated description for the video project.",
         "status": "inactive"
     }
     ```
   - **Response:**
     - **Status Code:** 200 OK
     - **Response Body:**
       ```json
       {
           "id": 1,
           "title": "Updated Title",
           "description": "Updated description for the video project.",
           "creation_date": "2024-05-15T00:00:00Z",
           "status": "inactive"
       }
       ```

4. **Delete Video Project**
   - **URL:** `/api/{id}/`
   - **Method:** DELETE
   - **Description:** Delete a specific video project.
   - **Response:**
     - **Status Code:** 204 No Content

### Setup Procedure

1. **Clone the Repository:**
   - Clone the repository containing the Django project from the Git repository.

2. **Install Dependencies:**
   - Navigate to the project directory and install the required dependencies using pip:
     ```
     pip install -r requirements.txt
     ```

3. **Database Setup:**
   - Configure the database settings in the `settings.py` file.
   - Run migrations to create database tables:
     ```
     python manage.py migrate
     ```

4. **Run the Development Server:**
   - Start the Django development server:
     ```
     python manage.py runserver
     ```

5. **Accessing the API:**
   - Access the API using a tool like Postman or curl.
   - Use the provided endpoints with appropriate request methods and parameters as documented above.
