# Rick and Morty test task
## Requirements:
- Endpoint, which return random character from the world of Rick and Morty series.
- Endpoint get search_string as an argument and return list of all characters, who contains the search_string in the name.
- On regular basis, app downloads data from external service to inner DB.
- Requests of implemented API should work with local DB (Take data from DB not from Rick & Morty API).
## Technologies to use:
- Public API: https://rickandmortyapi.com/documentation.
- Use Celery as task scheduler for data synchronization for Rick & Morty API.
- Python, Django/Flask/FastAPI, ORM, PostgreSQL, Git.
- All endpoints should be documented via Swagger.
### How to run:
- Copy .env.sample -> .env and populate with all required data
- docker-compose up --build
- Create admin user & Create schedule for running sync in DB  