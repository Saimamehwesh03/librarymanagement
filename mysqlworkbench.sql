create database python_mysql;

USE python_mysql; 
CREATE TABLE user (
  id INT NOT NULL,
  user_name VARCHAR(45) NULL,
  contact_info VARCHAR(45) NULL,
  PRIMARY KEY (id)) 
  ENGINE = InnoDB DEFAULT CHARSET=latin1;
INSERT INTO user (id,user_name,contact_info) 
VALUES (1,'Isabelle','9976029854'),(2,'Abigail Jose','9271649205763'),(3,'William McHawken','82739401648');
CREATE TABLE books (
  id_book INT NOT NULL,
  book_name VARCHAR(45) NULL,
  author VARCHAR(45) NULL,
  publisher VARCHAR(45) NULL,
  rented_user VARCHAR(45) NULL,
  rented_date DATE NULL,
  PRIMARY KEY (id_book))
ENGINE = InnoDB DEFAULT CHARSET=latin1;
INSERT INTO books (id_book,book_name,author,publisher,rented_user,rented_date) 
VALUES (1,'Crime and Punishment','Fyodor Dostoevsky','The Russian Messenger','Isabelle','2022-05-01'),(2,'The Master and Margarita ','Mikhail Bulgakov','YMCA Press','Abigail Jose','2022-09-01'),(3,'Buddenbrooks','Thomas Mann',' S. Fischer Verlag','William McHawken','2022-11-01');
CREATE TABLE librarian (
  books_idbook INT NOT NULL,
  user_id INT NOT NULL,
  new_username VARCHAR(45) NOT NULL,
  user_contactinfo INT NOT NULL,
   KEY books_idbook (books_idbook),
  KEY user_id (user_id),
  CONSTRAINT fk_librarian_books FOREIGN KEY (books_idbook) REFERENCES books (id_book)
    ON DELETE CASCADE,
  CONSTRAINT fk_librarian_user1 FOREIGN KEY (user_id)
    REFERENCES user (id)
    ON DELETE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET=latin1;