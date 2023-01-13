# Postgres service

Look how we're spinning up mysql in the private cloud
- are we using a custom docker-compose.yml?
- are we pushing a newly-generated docker image to our registry?

---

Before we use our db-handler software, we must:
- create the db instance
- create users with credentials
	- have a process to store credentials in vault
- create databases
	- create tables per database
