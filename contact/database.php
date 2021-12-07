CREATE TABLE visitors (
visitor_id int(11) AUTO_INCREMENT PRIMARY KEY not null,
visitor_subject text
visitor_name varchar(256) not null,
visitor_email varchar(256) not null
);

INSERT INTO visitors (visitor_id, visitor_subject, visitor_name, visitor_email)
