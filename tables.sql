-- create usa states database
CREATE DATABASE IF NOT EXISTS FlipDeck;
-- create states table
USE FlipDeck;
CREATE TABLE IF NOT EXISTS Users (
    user_id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    password_hash VARCHAR(256),
    email VARCHAR(256),
    created_at DATETIME,
    Updated_at DATETIME
);
CREATE TABLE IF NOT EXISTS Deck (
    deck_id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title VARCHAR(256),
    description VARCHAR(256),
    created_at DATETIME,
    updated_at DATETIME,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
CREATE TABLE IF NOT EXISTS Flashcards (
    flashcard_id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    front_text VARCHAR(256),
    back_text VARCHAR(256),
    created_at DATETIME,
    updated_at DATETIME,
    deck_id INT,
    FOREIGN KEY (deck_id) REFERENCES Deck(deck_id)
);
CREATE TABLE IF NOT EXISTS Progress (
    progress_id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    password_hash VARCHAR(256),
    email VARCHAR(256),
    last_viewed DATETIME,
    completed BOOLEAN,
    user_id INT,
    flashcard_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (flashcard_id) REFERENCES Flashcards(flashcard_id)
);