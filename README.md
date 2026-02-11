# Task Management System with AI Integration

A full-stack web application for task management with AI-powered features built using Flask, SQLAlchemy, and Ollama. The system provides comprehensive task tracking capabilities enhanced with artificial intelligence for automatic task description generation, categorization, effort estimation, and risk analysis.

## Overview

This project demonstrates proficiency in full-stack web development, RESTful API design, database modeling, user authentication, and AI integration. Built as a comprehensive task management solution, it showcases modern software engineering practices including secure authentication, role-based access control, and clean separation of concerns.

## Key Features

### Core Functionality
- User authentication and authorization with secure password hashing
- Role-based access control (Admin and Standard User roles)
- Full CRUD operations for tasks and users
- Task assignment and tracking with multiple status levels
- Responsive web interface with real-time status updates
- Dashboard with task statistics and analytics

### Task Management
- Priority levels: Low, Medium, High, Blocking
- Status tracking: Pending, In Progress, In Review, Completed
- Effort estimation in decimal hours
- Task categorization (Frontend, Backend, Testing, Infrastructure, etc.)
- Risk analysis and mitigation planning
- Team member assignment

### AI-Powered Features
- Automatic task description generation based on title
- Intelligent task categorization
- AI-driven effort estimation
- Risk analysis with mitigation plan generation
- Integration with Ollama for local LLM inference

### API
- RESTful API with JSON responses
- Session-based authentication
- Comprehensive error handling
- Permission-based access control

## Tech Stack

### Backend
- **Framework:** Flask 3.0.0
- **ORM:** SQLAlchemy 3.1.1
- **Authentication:** Flask-Login 0.6.3
- **Database:** SQLite (development), PostgreSQL-ready for production
- **Password Security:** Werkzeug 3.0.1 (bcrypt hashing)

### Frontend
- **Template Engine:** Jinja2
- **Styling:** Custom CSS with responsive design
- **JavaScript:** Vanilla JS for dynamic interactions

### AI Integration
- **LLM Platform:** Ollama
- **Models:** Compatible with Llama, Gemma, and other Ollama-supported models
- **API Integration:** REST API communication with local Ollama instance

### Additional Technologies
- **HTTP Client:** Requests 2.31.0
- **Database Migrations:** Custom migration scripts
- **Version Control:** Git

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Ollama (for AI features)

### Setup Instructions

1. Clone the repository

```bash
git clone <repository-url>
cd Integracion-de-Endponits
```

2. Install Python dependencies

```bash
pip install -r requirements.txt
```

3. Install and configure Ollama (optional, required for AI features)

```bash
# Visit https://ollama.ai to download and install Ollama
# Then pull a model:
ollama pull llama3.2
```

4. Initialize the database

```bash
python app.py
```

The database will be created automatically on first run.

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### First-Time Setup
- Navigate to the registration page
- Create your account (first user becomes admin automatically)
- Log in with your credentials

## Usage Examples

### Web Interface

#### Creating a Task
1. Log in to the dashboard
2. Click "New Task"
3. Fill in the task details:
   - Title (required)
   - Description
   - Priority level
   - Estimated effort in hours
   - Status
   - Team member assignment
4. Submit to create the task

#### Using AI Features
The AI endpoints can be accessed via the REST API to enhance task creation:

```bash
# Generate task description
curl -X POST http://localhost:5000/ai/tasks/describe \
  -H "Content-Type: application/json" \
  -H "Cookie: session=YOUR_SESSION" \
  -d '{
    "title": "Implement user authentication",
    "priority": "high"
  }'

# Categorize task
curl -X POST http://localhost:5000/ai/tasks/categorize \
  -H "Content-Type: application/json" \
  -H "Cookie: session=YOUR_SESSION" \
  -d '{
    "title": "Create login component",
    "description": "Build login form with validation"
  }'

# Estimate effort
curl -X POST http://localhost:5000/ai/tasks/estimate \
  -H "Content-Type: application/json" \
  -H "Cookie: session=YOUR_SESSION" \
  -d '{
    "title": "Implement notification system",
    "description": "Build push notification service",
    "category": "Backend"
  }'

# Risk analysis and mitigation
curl -X POST http://localhost:5000/ai/tasks/audit \
  -H "Content-Type: application/json" \
  -H "Cookie: session=YOUR_SESSION" \
  -d '{
    "title": "Database migration to PostgreSQL",
    "description": "Migrate from SQLite to PostgreSQL",
    "category": "Database",
    "priority": "high",
    "effort_hours": 16.0
  }'
```

### REST API

#### Authentication
All API endpoints require authentication via Flask session cookies.

#### Task Endpoints

**Create Task**
```http
POST /tasks
Content-Type: application/json

{
  "title": "Implement search feature",
  "description": "Add full-text search to task list",
  "priority": "medium",
  "effort_hours": 8.5,
  "status": "pending",
  "assigned_to": "John Doe",
  "category": "Backend"
}
```

**Get All Tasks**
```http
GET /tasks
```

**Get Specific Task**
```http
GET /tasks/1
```

**Update Task**
```http
PUT /tasks/1
Content-Type: application/json

{
  "status": "in_progress",
  "effort_hours": 10.0
}
```

**Delete Task**
```http
DELETE /tasks/1
```

## Project Structure

```
.
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── migrate_db.py              # Database migration script
├── services/
│   ├── __init__.py
│   └── ai_service.py          # AI/LLM integration service
├── templates/                  # Jinja2 HTML templates
│   ├── base.html              # Base template
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   ├── dashboard.html         # Main dashboard
│   ├── nueva_tarea.html       # Create task form
│   ├── editar_tarea.html      # Edit task form
│   ├── usuarios.html          # User management (admin)
│   └── nuevo_usuario.html     # Create user form (admin)
├── static/
│   ├── css/
│   │   └── style.css          # Custom styles
│   └── js/
│       └── main.js            # Client-side JavaScript
└── tareas.db                  # SQLite database (generated)
```

## Database Schema

### User Model
- `id`: Integer, Primary Key
- `nombre`: String(100), User's full name
- `email`: String(100), Unique, Email address
- `password_hash`: String(255), Hashed password
- `es_admin`: Boolean, Admin flag
- `fecha_creacion`: DateTime, Account creation timestamp

### Task Model
- `id`: Integer, Primary Key
- `title`: String(200), Task title
- `description`: Text, Detailed description
- `priority`: String(20), Priority level (low, medium, high, blocking)
- `effort_hours`: Numeric(10,2), Estimated hours
- `status`: String(20), Current status
- `assigned_to`: String(100), Assigned team member
- `category`: String(50), Task category
- `risk_analysis`: Text, AI-generated risk analysis
- `risk_mitigation`: Text, AI-generated mitigation plan
- `creador_id`: Integer, Foreign Key to User
- `fecha_creacion`: DateTime, Creation timestamp

## Security Features

- Password hashing using Werkzeug's security utilities
- Session-based authentication with Flask-Login
- CSRF protection (built into Flask)
- Role-based access control for administrative functions
- Input validation and sanitization
- SQL injection prevention through SQLAlchemy ORM

## API Permissions

- **Create Task:** Any authenticated user
- **View Tasks:** Admins see all tasks; users see only assigned tasks
- **Update/Delete Task:** Admins or task creator only
- **User Management:** Admins only

## Development Considerations

### Current Implementation
- SQLite database for development simplicity
- Local file-based sessions
- Hardcoded secret key (for development only)

### Production Recommendations
- Migrate to PostgreSQL or MySQL for production
- Implement environment-based configuration
- Use secure secret key from environment variables
- Add rate limiting for API endpoints
- Implement API key authentication for external access
- Add comprehensive logging and monitoring
- Deploy behind HTTPS with proper SSL certificates

## Future Improvements

- Task dependencies and subtasks
- File attachments for tasks
- Comment system for task collaboration
- Email notifications for task updates
- Calendar view and deadline tracking
- Task templates for common workflows
- Advanced filtering and search capabilities
- Export functionality (PDF, CSV)
- Mobile responsive improvements
- Websocket integration for real-time updates
- OAuth integration (Google, GitHub)
- API rate limiting and throttling
- Comprehensive test suite (unit and integration tests)
- CI/CD pipeline integration
- Docker containerization
- Kubernetes deployment configuration

## Skills Demonstrated

This project showcases the following technical competencies:

- Full-stack web development with Python and Flask
- RESTful API design and implementation
- Database design and ORM usage
- User authentication and authorization
- Secure password handling
- Frontend development with HTML, CSS, and JavaScript
- Integration with third-party APIs and services
- AI/ML integration for practical applications
- Clean code architecture and separation of concerns
- Version control with Git
- Documentation and technical writing

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built with Flask, SQLAlchemy, and Ollama. Designed as a demonstration of modern web development practices and AI integration capabilities.
