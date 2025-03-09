# Random Attendee Selector 🎟️

This is a FastAPI-based application designed to randomly select attendees for theater events based on prioritized logic, authentication via OAuth2 Bearer tokens, and advanced selection criteria.

## 📦 Project Structure

```
random-attendee-selector/
├── app/
│   ├── api/
│   ├── core/
│   ├── enums/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── scripts/
│   └── populate_dummy.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Features

- **OAuth2 Authentication:**
  - Secure endpoints with JWT tokens.
  - Tokens have a validity period (2 hours).

- **Priority-Based Selection:**
  - Prioritizes attendees based on multiple factors:
    - Nearest location (simplified).
    - Number of previous losses.
    - Theater popularity (number of applicants).
    - Matching favorite members performing in the theater.

- **Special Event Handling:**
  - Increased verification probability for:
    - Attendees who've lost ≥10 times.
    - Attendees favoring members having birthdays or last shows.

- **Two distinct selection endpoints:**
  - OFC attendees.
  - General attendees (balanced percentage-based selection).

## 🔧 Installation

1. Clone the repository:

```bash
git clone your_repo_url
cd random-attendee-selector
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create `.env` file:

```env
APP_NAME="Random Attendee Selector"
DEBUG=True
DATABASE_URL="sqlite:///./attendees.db"
SECRET_KEY="your_generated_secret_key"
ALGORITHM="HS256"
```

4. Run the application:

```bash
uvicorn app.main:app --reload
```

## 🔐 Authentication

- Obtain JWT token via:

```bash
POST /api/token
Content-Type: application/x-www-form-urlencoded

username=admin&password=password
```

- Access secured endpoints:

```bash
Authorization: Bearer your_access_token
```

## 📚 API Endpoints

- Select OFC attendees:

```http
POST /api/select_attendees/ofc
```

- Select General attendees:

```http
POST /api/select_attendees/general
```

## 📝 Example Request

```json
{
  "theater_id": 1,
  "maximum_attendees": 100
}
```

## 🛠️ Future Improvements

- Implement real geolocation logic.
- Add proper user management and secure database storage.
- Enhance reporting and analytics features.

---

Enjoy your automated attendee selection process! 🎭

