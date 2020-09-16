# Company
Manage Employee Information.

This project has below modules:
#### Login
It allows users to login into the system. There are two types of user in the system, namely Admin and Staff. Staff users have read only access to the employees data, Admin users have full access. This module provides below functionalities:
* Obtain New Token
* Refresh Token

Please refer the the browsable API for details regarding API.

### Employee
This module provided APIs for CRUD operations for Employees. We are using the AbstractUser model for both User and Employees, because User are also employees. However, all employees are not allowed to login. Only staff and admin users can login to the system.

### DRF Browsable API
* Obtain Token: http://localhost:8000/api/token/
* Refresh Token: http://localhost:8000/api/token/refresh/
* List or Create Employees: http://localhost:8000/api/employees/
* Get, Update or Partial Update Employee: http://localhost:8000/api/employees/<id>


### Features
* DRF Browsable API
* Unit tests
* Docker
* Filtering
* Ordering
* Search
* JWT Auth

### How to run application
**Pre-Requisite**: docker and docker-compose must be installed and configured on the machine


Execute command: `docker-compose up` 
