-- Create additional roles/users
CREATE USER app_user WITH PASSWORD 'secure_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE django_db TO app_user;

-- Create a table
CREATE TABLE IF NOT EXISTS to_do_list (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each task
    task_name VARCHAR(100) NOT NULL,         -- Name or description of the task
    status VARCHAR(50) DEFAULT 'Pending',    -- Current status of the task (e.g., Pending, In Progress, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the task was created
    due_date TIMESTAMP DEFAULT NULL          -- Optional due date for the task
);


-- Insert initial data
INSERT INTO to_do_list (task_name, status, due_date) VALUES
('Create user app_user', 'Completed', NULL),
('Grant privileges to app_user', 'Completed', NULL),
('Create example_table', 'Completed', NULL),
('Insert initial data into example_table', 'Completed', NULL),
('Write documentation for database setup', 'Pending', '2024-12-01');