.# Car_Service_App
<h2 align="center">Introduction</h2>
Car service app with internal application for mechanics and receivers and official site where customer may register, add their cars and follow the progress with their car repairing.



<h1 align="center">Instalation Steps</h1>
<ol>
  <li>
    <h3>Clone the source code</h3>
    git clone "repo link"</li>
  <li>
    <h3>Download the pre-builded services</h3>
    docker pull cvstoilov/car_service</li>
  <li>
    <h3>Create your .env.prod file and fill it with your PROD environment variables in root directory</h3>
  </li>
  <li>
    <h3>Run the DB and application</h3>
    docker compose -f docker-compose.production.yml  up -d web
  </li>
  <li>
    <h3>Collect all static files</h3>
    docker compose -f docker-compose.production.yml exec web python manage.py collectstatic
  </li>
  <li>
    <h3>Start the Nginx</h3>
    docker compose -f docker-compose.production.yml up nginx -d
  </li>
</ol>

