drop database cfg;
create database cfg;
use cfg;
CREATE TABLE User (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50),
    classid INT,
    bio VARCHAR(2000),
    picture VARCHAR(50)
);

CREATE TABLE Journey (
    journeyid Int PRIMARY KEY,
    event VARCHAR(200)
);

CREATE TABLE Reactions (
    type VARCHAR(20),
    username VARCHAR(50),
    journeyid Int PRIMARY KEY,
    reactiondata VARCHAR(2000),
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Reflection (
    journeyid Int,
    text VARCHAR(5000),
    username VARCHAR(50),
    public Int,
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Feedback (
    journeyid Int,
    apiurl VARCHAR(400),
    username VARCHAR(50),
    public Int,
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Class (
    classid INT AUTO_INCREMENT PRIMARY KEY,
    schoolname VARCHAR(200),
    gradyear Int
);

CREATE TABLE ClassJourney (
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    classid INT,
    journeyid Int
)

INSERT INTO Journey(journeyid, event)
VALUES (10, "boi");

INSERT INTO User(username, password, classid, bio, picture)
VALUES ("sidharth", "hunter2", 2020, "i don't know flask", "test.jpg");

INSERT INTO User(username, password, classid, bio, picture)
VALUES ("kevin", "hunter2", 2020, "working on flask", "new.jpg");
