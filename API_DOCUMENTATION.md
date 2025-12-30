# API Documentation

## Base URL
```
http://localhost:5000/api
```

## Authentication
Currently, no authentication is required. This can be added in future versions.

---

## Endpoints

### 1. Get All Movies
**Endpoint:** `GET /movies`

**Description:** Retrieve all movies or filter by language

**Query Parameters:**
- `language` (optional): Filter by language (`marathi`, `hindi`, `punjabi`)

**Example Requests:**
```bash
# Get all movies
GET http://localhost:5000/api/movies

# Get movies by language
GET http://localhost:5000/api/movies?language=marathi
GET http://localhost:5000/api/movies?language=hindi
GET http://localhost:5000/api/movies?language=punjabi
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Natrang",
    "language": "marathi",
    "url": "https://example.com/movie",
    "image_url": "https://example.com/image.jpg",
    "release_date": "2023-01-15T00:00:00"
  },
  {
    "id": 2,
    "title": "Laal Singh Chaddha",
    "language": "hindi",
    "url": "https://example.com/movie2",
    "image_url": "https://example.com/image2.jpg",
    "release_date": "2023-02-20T00:00:00"
  }
]
```

**Status Code:** 200 OK

---

### 2. Get Specific Movie
**Endpoint:** `GET /movies/<id>`

**Description:** Retrieve a specific movie by ID

**Path Parameters:**
- `id` (required): Movie ID (integer)

**Example Request:**
```bash
GET http://localhost:5000/api/movies/1
```

**Response:**
```json
{
  "id": 1,
  "title": "Natrang",
  "language": "marathi",
  "url": "https://example.com/movie",
  "image_url": "https://example.com/image.jpg",
  "release_date": "2023-01-15T00:00:00"
}
```

**Status Code:** 200 OK

**Error Response (404):**
```json
{
  "error": "Movie not found"
}
```

---

### 3. Create Movie
**Endpoint:** `POST /movies`

**Description:** Create a new movie

**Request Body:**
```json
{
  "title": "New Movie Title",
  "language": "marathi",
  "url": "https://example.com/movie",
  "image_url": "https://example.com/image.jpg",
  "release_date": "2024-01-15"
}
```

**Required Fields:**
- `title` (string): Movie title
- `language` (string): Language (`marathi`, `hindi`, `punjabi`)

**Optional Fields:**
- `url` (string): Movie URL/link
- `image_url` (string): Movie poster URL
- `release_date` (string): Release date in ISO format

**Example Request:**
```bash
curl -X POST http://localhost:5000/api/movies \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Marathi Movie",
    "language": "marathi",
    "url": "https://example.com/movie",
    "image_url": "https://example.com/poster.jpg",
    "release_date": "2024-01-15"
  }'
```

**Response:**
```json
{
  "id": 4,
  "title": "New Marathi Movie",
  "language": "marathi",
  "url": "https://example.com/movie",
  "image_url": "https://example.com/poster.jpg",
  "release_date": "2024-01-15T00:00:00"
}
```

**Status Code:** 201 Created

**Error Response (400):**
```json
{
  "error": "Title and language are required"
}
```

---

### 4. Update Movie
**Endpoint:** `PUT /movies/<id>`

**Description:** Update an existing movie

**Path Parameters:**
- `id` (required): Movie ID (integer)

**Request Body:**
```json
{
  "title": "Updated Title",
  "language": "hindi",
  "url": "https://example.com/new-url",
  "image_url": "https://example.com/new-image.jpg",
  "release_date": "2024-02-20"
}
```

**Note:** All fields are optional. Only include fields you want to update.

**Example Request:**
```bash
curl -X PUT http://localhost:5000/api/movies/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Movie Title",
    "language": "hindi"
  }'
```

**Response:**
```json
{
  "id": 1,
  "title": "Updated Movie Title",
  "language": "hindi",
  "url": "https://example.com/movie",
  "image_url": "https://example.com/image.jpg",
  "release_date": "2023-01-15T00:00:00"
}
```

**Status Code:** 200 OK

**Error Response (404):**
```json
{
  "error": "Movie not found"
}
```

---

### 5. Delete Movie
**Endpoint:** `DELETE /movies/<id>`

**Description:** Delete a movie

**Path Parameters:**
- `id` (required): Movie ID (integer)

**Example Request:**
```bash
curl -X DELETE http://localhost:5000/api/movies/1
```

**Response:**
```json
{
  "message": "Movie deleted successfully"
}
```

**Status Code:** 200 OK

**Error Response (404):**
```json
{
  "error": "Movie not found"
}
```

---

### 6. Health Check
**Endpoint:** `GET /health`

**Description:** Check if the API is running

**Example Request:**
```bash
GET http://localhost:5000/api/health
```

**Response:**
```json
{
  "status": "healthy"
}
```

**Status Code:** 200 OK

---

## Error Handling

### Common Error Codes

| Code | Description |
|------|-------------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid request data |
| 404 | Not Found - Resource not found |
| 500 | Internal Server Error - Server error |

### Error Response Format
```json
{
  "error": "Error message describing the issue"
}
```

---

## Testing with Postman

### Import Collection
1. Open Postman
2. Create a new collection: "Movie API"
3. Add requests for each endpoint

### Example Postman Variables
Set the following variable:
- `base_url`: `http://localhost:5000/api`

Then use `{{base_url}}/movies` in requests

---

## Testing with cURL

### Get All Movies
```bash
curl http://localhost:5000/api/movies
```

### Get Movies by Language
```bash
curl "http://localhost:5000/api/movies?language=marathi"
```

### Create Movie
```bash
curl -X POST http://localhost:5000/api/movies \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Movie",
    "language": "hindi",
    "url": "https://example.com/movie",
    "image_url": "https://example.com/image.jpg"
  }'
```

### Update Movie
```bash
curl -X PUT http://localhost:5000/api/movies/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title"}'
```

### Delete Movie
```bash
curl -X DELETE http://localhost:5000/api/movies/1
```

---

## Rate Limiting
Currently, no rate limiting is implemented. This can be added in future versions using Flask-Limiter.

---

## CORS Configuration
The API is configured to accept requests from `http://localhost:3000` (frontend).

To add more origins, update the CORS configuration in `app.py`:
```python
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "https://yourdomain.com"]
    }
})
```

---

## Versioning
Current API Version: `v1` (implicit in `/api` prefix)

Future versions: `/api/v2/movies`, etc.

---

## Data Validation

### Language Values
Valid language values:
- `marathi`
- `hindi`
- `punjabi`

### Date Format
Use ISO 8601 format: `YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SS`

### URL Format
Ensure URLs are valid and include protocol (`https://` or `http://`)

---

## Database Storage
Currently, the API uses in-memory storage. Data will be lost on server restart.

For production:
- Implement SQLAlchemy with PostgreSQL
- Add persistent storage
- Implement migrations

---

## Future Enhancements
- [ ] JWT Authentication
- [ ] Rate Limiting
- [ ] Pagination
- [ ] Search functionality
- [ ] Advanced filtering
- [ ] User ratings
- [ ] Comments and reviews
- [ ] Image upload
- [ ] Video streaming
