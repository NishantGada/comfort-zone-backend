use ComfortZone;

CREATE TABLE toilets (
    toilet_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    toilet_name VARCHAR(255) NOT NULL,
    toilet_description TEXT,
    toilet_address_line_1 VARCHAR(255),
    toilet_address_line_2 VARCHAR(255),
    toilet_city VARCHAR(100),
    toilet_state VARCHAR(100),
    toilet_zipcode VARCHAR(20),
    toilet_gender ENUM('Male', 'Female', 'All'),
    toilet_charges DECIMAL(5,2) DEFAULT 0.00,
    toilet_build_date DATE,
    toilet_registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    toilet_operation_hours VARCHAR(100)
);

CREATE TABLE toilet_comments (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id CHAR(36),
    toilet_id CHAR(36),
    comment_text TEXT NOT NULL,
    commented_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (toilet_id) REFERENCES toilets(toilet_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

CREATE TABLE toilet_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    toilet_id CHAR(36),
    image_url TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (toilet_id) REFERENCES toilets(toilet_id) ON DELETE CASCADE
);

CREATE TABLE toilet_features (
    feature_id INT AUTO_INCREMENT PRIMARY KEY,
    toilet_id CHAR(36),
    feature_name VARCHAR(100),
    is_available BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (toilet_id) REFERENCES toilets(toilet_id) ON DELETE CASCADE
);

CREATE TABLE toilet_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    toilet_id CHAR(36),
    user_id CHAR(36),
    rating INT CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (toilet_id) REFERENCES toilets(toilet_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

ALTER TABLE toilet_features
    DROP is_available;

ALTER TABLE toilet_features
    ADD COLUMN feature_id CHAR(36) PRIMARY KEY;

    

