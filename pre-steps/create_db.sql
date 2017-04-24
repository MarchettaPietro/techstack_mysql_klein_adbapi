CREATE DATABASE IF NOT EXISTS dummy_sportsbook;
use dummy_sportsbook;

CREATE TABLE event (
     id INT(11) auto_increment primary key,
     name VARCHAR(255) not null,
     active TINYINT(1) not null default 1,
     schedule_time DATETIME not null
);

CREATE TABLE market (
     id INT(11) auto_increment primary key,
     name VARCHAR(255) not null
);

CREATE TABLE selection (
     id INT(11) auto_increment primary key,
     name VARCHAR(255) not null,
     market_id INT(11) not null,
     event_id INT(11) not null,
     FOREIGN KEY (market_id) REFERENCES market(id),
     FOREIGN KEY (event_id) REFERENCES event(id)
);


INSERT INTO event values
(1, 'e1', 1, '2017-01-01 12:00:00'),
(2, 'e2', 1, '2017-01-01 12:00:00'),
(3, 'e3', 1, '2017-01-01 12:00:00');


INSERT INTO market values
(1, 'm1'),
(2, 'm2'),
(3, 'm3');

INSERT INTO selection values
(1, 's1', 1, 1),
(2, 's2', 1, 1),
(3, 's3', 2, 1),
(4, 's4', 2, 1),
(5, 's5', 2, 2),
(6, 's6', 2, 2),
(7, 's7', 2, 3),
(8, 's8', 3, 3),
(9, 's9', 3, 3);

