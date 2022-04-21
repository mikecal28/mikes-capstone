CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    date_created TEXT NOT NULL,
    hire_date TEXT NOT NULL,
    user_type TEXT NOT NULL,
    active INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS Assessment_Results (
    results_id PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    assessment_id INTEGER,
    score TEXT NOT NULL,
    date_taken TEXT NOT NULL,
    manager_id INTEGER NOT NULL,
    active INTEGER DEFAULT 1,
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id),
    FOREIGN KEY (assessment_id)
        REFERENCES Assessments (assessment_id),
    FOREIGN KEY (manager_id)
        REFERENCES Users (user_id)
);

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    competency_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    date_created TEXT NOT NULL,
    active INTEGER DEFAULT 1,
    FOREIGN KEY (competency_id)
        REFERENCES Competencies (competency_id)
);

CREATE TABLE IF NOT EXISTS Competencies (
    competency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    active INTEGER DEFAULT 1
);
