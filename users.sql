use ComfortZone;

CREATE TABLE users (
    user_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    dob DATE,
    gender ENUM('Male', 'Female', 'Other'),
    age INT,
    address_line_1 VARCHAR(255),
    address_line_2 VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    zipcode VARCHAR(20),

    -- Suggested additions:
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    -- is_active BOOLEAN DEFAULT TRUE,
    -- is_verified BOOLEAN DEFAULT FALSE
);

desc Users;

INSERT INTO users (
    user_id,
    email,
    password,
    phone,
    dob,
    gender,
    address_line_1,
    address_line_2,
    city,
    state,
    zipcode,
    first_name,
    last_name,
) VALUES (
    UUID(),
    'test1@gmail.com',
    'asdasd',
    '+11234567890',
    '1995-06-15',
    'Male',
    '123 Main Street',
    'Apt 4B',
    'New York',
    'NY',
    '10001',
    'Nishant',
    'Gada',
);

select * from users;

