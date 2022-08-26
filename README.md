# travel-meet-app

The app would allow solo travelers to connect and explorer together their destinations.

# Setup

- Install all the dependencies by running:
  `pip install -r requirements.txt`

- Configure environment variables `DB_USER` and `DB_PASS` in config.py to store your database username and database password. <br/>

  ```
    export DB_USER='YOUR VALUE'
    export DB_PASS='YOUR VALUE'
  ```

- Using MySQL Workbench or any MySQL client, create the necessary database `CREATE DATABASE t_meet`
- Using Python Shell create tables </br>
  In terminal, go to the project directory and execute following commands

  ```
    flask shell
    from app import db
    db.create_all()
  ```

  In order to exit from the shell, enter `exit()`

- Run the flask server by running:
  `env=dev flask run`
  Note: If you want to run flask on specific port, use `env=dev flask run --port 9000`

# Running Test

- Use following command to run test: <br />
  ```
  env=test python3 -m unittest
  ```
