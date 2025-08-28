<p align="center">
  <img src="https://github.com/abdevvv/Spotly/blob/main/SPOTLY.png" alt="Spotly Logo" width="200" />
</p>

<h1 align="center">Spotly</h1>

<p align="center">
  <strong>Geo-powered business directory built with Django & PostGIS</strong><br/>
  Featuring location-based search, category filtering, ratings & reviews.
</p>

<p align="center">
  <a href="https://github.com/abdevvv/Spotly/stargazers">
    <img src="https://img.shields.io/github/stars/abdevvv/Spotly?style=social" alt="GitHub stars"/>
  </a>
  <a href="https://github.com/abdevvv/Spotly/network/members">
    <img src="https://img.shields.io/github/forks/abdevvv/Spotly?style=social" alt="GitHub forks"/>
  </a>
  <a href="https://github.com/abdevvv/Spotly/issues">
    <img src="https://img.shields.io/github/issues/abdevvv/Spotly" alt="GitHub issues"/>
  </a>
  <a href="https://github.com/abdevvv/Spotly/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/abdevvv/Spotly" alt="License"/>
  </a>
</p>

---

## Table of Contents

- [Features](#features)  
- [Demo / Highlight](#demo--highlight)  
- [Installation (Docker)](#installation-docker)  
- [Postman Collection](#postman-collection)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- **Location-Based Search**: Find businesses based on proximity to the user’s location and within a specified radius.  
- **Category Filtering**: Narrow down searches to specific categories (e.g., restaurants, shops, services).  
- **Ratings & Reviews**: Users can rate and leave reviews—helping others make informed decisions.  
- Built with **PostGIS**, enabling performant geospatial queries.  
- **RESTful API** powered by Django REST Framework—ideal for frontend clients.  

---

## Demo / Highlight

 **Filter Businesses** by your nearest location and radius:

1. Send a request to the search endpoint with `latitude`, `longitude`, and `radius` parameters (e.g., in kilometers or meters).  
2. The backend leverages PostGIS spatial queries—such as `ST_DWithin`—to efficiently return businesses within that radius.  
3. Results can be further refined by category and optionally sorted by rating or distance.

---

## Installation (Docker)

**Requirements**: Docker, Docker Compose

```bash
git clone https://github.com/abdevvv/Spotly.git
cd Spotly
```

Create a `.env.prod` with your configuration (e.g., `POSTGRES_USER`, `POSTGRES_PASSWORD`, etc.), then run:

```bash
docker compose up -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```



Finally, access the API at `http://localhost:8000/api/` and the admin at `http://localhost:8000/admin/`.

---


### **Filtering Example**

Request: `GET /api/businesses/?lat=30.0&lng=31.0&radius=5000&category=coffee`

The backend would use PostGIS spatial lookups—like `distance_lte` or `ST_DWithin`—to return relevant businesses.

---

## Postman Collection

Explore and test the API with the provided Postman collection:

**Collection**: [Spotly.postman_collection.json](https://github.com/abdevvv/Spotly/blob/main/Spotly.postman_collection.json)

Import this into Postman to quickly interact with every endpoint—great for QA, demos, or documentation.

---

## Contributing

We welcome contributions! Here's how to help:

1. Fork the repository  
2. Create a feature branch: `git checkout -b feature/your-feature`  
3. Develop and test your changes (especially geo-related functionality)  
4. Ensure all tests pass and coding style is consistent  
5. Submit a pull request with clear descriptions and rationale  

Please open issues for bugs, enhancement requests, or questions.

---

## License

Distributed under the **[MIT License](https://opensource.org/licenses/MIT)** — feel free to use, modify, and distribute as permitted by the license.

---

## Acknowledgements

- Built on **Django**, * and **PostGIS**  
- Spatial searches and docker setup inspired by modern best practices  

---

Thank you for checking out **Spotly**! We hope it serves as a powerful foundation or inspiration for your geo‑powered directories.

