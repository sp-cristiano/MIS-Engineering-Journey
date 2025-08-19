# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a **12-month MIS Engineering Journey** repository documenting a complete transformation from beginner to professional software engineer and data analyst. The journey runs from August 19, 2025 to August 19, 2026, following a structured 3-phase learning approach.

## Architecture & Structure

### Phase-Based Learning Architecture
The repository follows a 3-phase progression structure:
- **Phase 1 (Months 1-3)**: Foundation - Python, Git, Web Basics, SQL
- **Phase 2 (Months 4-6)**: Core Skills - OOP, Flask/Django, Data Analytics, PowerBI  
- **Phase 3 (Months 7-9)**: Integration - Full-stack, Cloud, Machine Learning

### Directory Structure
```
MIS-Engineering-Journey/
├── Daily-Progress/           # Daily learning logs and progress tracking
├── Phase1-Foundation/        # Phase 1 code and projects
├── Projects/                # Project planning and portfolio roadmaps
├── Resources/               # Learning guides and documentation
└── README.md               # Main project overview
```

### Key Files
- `README.md` - Main project overview with learning phases and success metrics
- `Resources/Complete-Learning-Guide.md` - Comprehensive 12-month learning curriculum
- `Projects/Portfolio-Roadmap.md` - Professional portfolio development strategy
- `Daily-Progress/` - Contains daily logs and weekly trackers for accountability

## Development Workflow

### Daily Development Pattern
The learner follows a consistent daily schedule:
- **Morning Session (08:50-11:50)**: 3-hour deep work coding sessions
- **Evening Session (21:46-22:00)**: Git commits, progress tracking, next-day planning

### Version Control Strategy
- Daily GitHub commits are a core requirement (target: 300+ commits over 12 months)
- Each day's work should be committed with meaningful messages
- Repository serves as both learning portfolio and professional showcase

### Common Commands

#### Running Python Code
```bash
# Run Python scripts from Phase1-Foundation
python3 Phase1-Foundation/day001_hello_world.py

# For future phases, run from respective directories
cd Phase1-Foundation && python3 <script_name>.py
```

#### Progress Tracking
```bash
# View daily progress logs
ls Daily-Progress/
cat Daily-Progress/2025-08-19-Day001.md

# Check weekly trackers
cat Daily-Progress/Week01-Tracker.md
```

#### Project Development
```bash
# Navigate to current phase
cd Phase1-Foundation/  # Currently in Phase 1

# For web projects (future phases)
# Will likely use Flask development server:
# python3 -m flask run

# For data analysis projects (future phases)
# Will likely use Jupyter notebooks:
# jupyter notebook
```

### Learning Progression Tracking

#### Success Metrics Monitoring
The repository tracks specific metrics by phase:

**Month 1-3 (Foundation):**
- 50+ Python scripts written
- 90+ GitHub commits 
- Portfolio website deployed
- SQL database queries mastered

**Month 4-6 (Core Skills):**
- Flask/Django applications built
- Interactive dashboards created
- RESTful APIs developed

**Month 7-9 (Integration):**
- Full-stack application deployed to cloud
- Machine learning model implemented
- Professional-grade project portfolio

### Project Portfolio Strategy

The repository will contain 12+ substantial projects following this progression:
1. **Foundation Projects**: Personal calculator, grade manager, web scraper
2. **Core Skills Projects**: Task manager web app, e-commerce platform, BI dashboard
3. **Professional Projects**: Microservices architecture, AI analytics platform, capstone MIS solution

Each project follows this structure:
- Clean, documented code
- Comprehensive README with setup instructions
- Live demo deployment
- Case study documentation

### Technology Stack Evolution

**Current Stack (Month 1):**
- Python 3 (primary language)
- VS Code (development environment)
- Git/GitHub (version control)
- Linux/Fedora (development platform)

**Upcoming Stack (by completion):**
- Backend: Python, Flask/Django, FastAPI, Node.js
- Frontend: HTML/CSS/JavaScript, React
- Databases: SQLite, PostgreSQL
- Cloud: AWS/GCP, Docker
- Data: Pandas, NumPy, Matplotlib, PowerBI
- ML: Scikit-learn, TensorFlow

### Development Environment

#### Required Setup
- Python 3.x with standard libraries
- VS Code with Python extension
- Git configured for daily commits
- Linux development environment (Fedora)

#### VS Code Extensions (Recommended)
- Python official extension
- Pylint for code quality
- GitLens for Git integration
- Live Server for web development (future phases)

### Testing Strategy

As projects grow in complexity:
- Unit tests for utility functions
- Integration tests for web applications
- Documentation of test coverage
- Automated testing in CI/CD (Phase 3)

### Deployment Strategy

**Phase 1**: Local development and GitHub Pages
**Phase 2**: Heroku/Netlify for web applications  
**Phase 3**: AWS/GCP with Docker containers and CI/CD pipelines

### Learning Resources Integration

The repository integrates with external learning platforms:
- Python.org official documentation
- Real Python tutorials
- Flask Mega-Tutorial
- Kaggle Learn (data science)
- AWS/GCP documentation (cloud deployment)

### Professional Development Focus

This is not just a learning repository but a professional portfolio demonstrating:
- Consistent daily coding practice
- Progressive skill building
- Real-world project development
- Clean code and documentation practices
- Version control proficiency
- Problem-solving capabilities

The repository serves as evidence of a complete transformation journey from complete beginner to industry-ready MIS Engineer specializing in software development and data analytics.
