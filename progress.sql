USE FlipDeck;
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