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
    journeyid Int PRIMARY KEY AUTO_INCREMENT,
    event VARCHAR(200)
);

CREATE TABLE Reactions (
    type VARCHAR(20),
    username VARCHAR(50),
    journeyid Int,
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

CREATE TABLE UserJourney (
    username VARCHAR(50),
    journeyid INT
);

CREATE TABLE ClassJourney (
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    classid INT,
    journeyid Int
);

INSERT INTO Journey(journeyid, event)
VALUES (1, "Bowling");
INSERT INTO Journey(journeyid, event)
VALUES (2, "Rock Climbing");
INSERT INTO Journey(journeyid, event)
VALUES (3, "Ping Pong");

INSERT INTO User(username, password, classid, bio, picture)
VALUES ("Sidharth", "hunter2", 1, "my name is sid", "test.jpg");
INSERT INTO User(username, password, classid, bio, picture)
VALUES ("Kevin", "hunter2", 1, "my name is kevin", "new.jpg");
INSERT INTO User(username, password, classid, bio, picture)
VALUES ("Zi", "hunter2", 2, "my name is zi", "test.jpg");
INSERT INTO User(username, password, classid, bio, picture)
VALUES ("Trent", "hunter2", 3, "my name is trent", "new.jpg");

INSERT INTO UserJourney(username, journeyid)
VALUES ("Kevin", 1);
INSERT INTO UserJourney(username, journeyid)
VALUES ("Kevin", 2);
INSERT INTO UserJourney(username, journeyid)
VALUES ("Kevin", 3);
INSERT INTO UserJourney(username, journeyid)
VALUES ("Sidharth", 2);
INSERT INTO UserJourney(username, journeyid)
VALUES ("Zi", 1);
INSERT INTO UserJourney(username, journeyid)
VALUES ("Zi", 3);
INSERT INTO UserJourney(username, journeyid)
VALUES ("Trent", 1);

INSERT INTO Reactions(type, username, journeyid, reactiondata)
VALUES ("text", "Kevin", 1, "Stubbed my big toe Bowling");
INSERT INTO Reactions(type, username, journeyid, reactiondata)
VALUES ("text", "Sidharth", 2, "Had a great time");
INSERT INTO Reactions(type, username, journeyid, reactiondata)
VALUES ("text", "Trent", 1, "Stubbed my little toe Bowling");

INSERT INTO Reflection(journeyid, text, username, public)
VALUES (1, "I had so much fun!@@@!!#$!#!", "Kevin", 1);

INSERT INTO Class(schoolname, gradyear)
VALUES ("Chicago's best", 2019);
INSERT INTO Class(schoolname, gradyear)
VALUES ("Chicago's second best", 2019);
INSERT INTO Class(schoolname, gradyear)
VALUES ("Chicago's second best", 2020);

INSERT INTO ClassJourney(classid, journeyid)
VALUES (1,1);
INSERT INTO ClassJourney(classid, journeyid)
VALUES (1,2);
INSERT INTO ClassJourney(classid, journeyid)
VALUES (2,1);