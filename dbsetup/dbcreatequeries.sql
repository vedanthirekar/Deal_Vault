DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS user_profile;
DROP TABLE IF EXISTS deals;
DROP TABLE IF EXISTS stores;
DROP TABLE IF EXISTS categories;

CREATE TABLE users (
	user_id Serial PRIMARY KEY,
    email varchar(100) NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL UNIQUE,
    user_password VARCHAR(225) NOT NULL 
);

INSERT INTO users (email, username, user_password) VALUES ('tanvig22@gmail.com', 'tanvig22', 'p@S5wOrD!9');
INSERT INTO users (email, username, user_password) VALUES ('devik78@gmail.com', 'devik78', 'T#e8xAmPlE2');
INSERT INTO users (email, username, user_password) VALUES ('dhruvilj92@gmail.com', 'dhruvilj92', 'M@rKeT1nG!Z');
INSERT INTO users (email, username, user_password) VALUES ('naishalsh50@gmail.com', 'naishalsh50', 'L0g!N#PaSs7');
INSERT INTO users (email, username, user_password) VALUES ('yashwip26@gmail.com', 'yashwip26', 'h@Ck3R#MiNd');
INSERT INTO users (email, username, user_password) VALUES ('harshgp99@gmail.com', 'harshgp99', 'SeCuR3!tY2#');
INSERT INTO users (email, username, user_password) VALUES ('rakshitrr17@gmail.com', 'rakshitrr17', 'F@cE2bO0K!z');
INSERT INTO users (email, username, user_password) VALUES ('pranaybh66@gmail.com', 'pranaybh66', 'p@S5wOrD!9');
INSERT INTO users (email, username, user_password) VALUES ('harshpt18@gmail.com', 'harshpt18', 'C#0d!nG$FuN');
INSERT INTO users (email, username, user_password) VALUES ('mihirpa25@gmail.com', 'mihirpa25', 'D@tA7#ScI!x');
INSERT INTO users (email, username, user_password) VALUES ('durgesht27@gmail.com', 'durgesht27', 'nE@t#5WoRk$');
INSERT INTO users (email, username, user_password) VALUES ('porterh63@gmail.com', 'porterh63', 'X!yZ1#CoOl9');
INSERT INTO users (email, username, user_password) VALUES ('sriram07@gmail.com', 'sriram07', 'jUmP@3#sHoT');
INSERT INTO users (email, username, user_password) VALUES ('sathya32@gmail.com', 'sathya32', 'ReDd!T#9p@gE');
INSERT INTO users (email, username, user_password) VALUES ('palaksh12@gmail.com', 'palaksh12', 'Y0Lo#LiFe!7');
INSERT INTO users (email, username, user_password) VALUES ('advita08@gmail.com', 'advita08', 'tWiT@#123X!');
INSERT INTO users (email, username, user_password) VALUES ('atharvad18@gmail.com', 'atharvad18', 'V!Ru$5#Tr@cK');
INSERT INTO users (email, username, user_password) VALUES ('rugvedch04@gmail.com', 'rugvedch04', 'Q#uIzZy!8@bC');
INSERT INTO users (email, username, user_password) VALUES ('adhishthica21@gmail.com', 'adhishthica21', 'G@Me0vEr#99!');
INSERT INTO users (email, username, user_password) VALUES ('sandeepda11@gmail.com', 'sandeepda11', 'p@$$W0rD#2o2!');

CREATE TABLE stores (
    store_id Serial PRIMARY KEY,
    store_name TEXT NOT NULL
);

INSERT INTO stores (store_name) VALUES ('Tech World');
INSERT INTO stores (store_name) VALUES ('Fashion Fiesta');
INSERT INTO stores (store_name) VALUES ('Grocery Hub');
INSERT INTO stores (store_name) VALUES ('Book Bazaar');
INSERT INTO stores (store_name) VALUES ('Home Essentials');
INSERT INTO stores (store_name) VALUES ('Toy Town');
INSERT INTO stores (store_name) VALUES ('SportX');
INSERT INTO stores (store_name) VALUES ('Daily Deals');
INSERT INTO stores (store_name) VALUES ('Beauty Bliss');
INSERT INTO stores (store_name) VALUES ('Kitchen King');


CREATE TABLE categories (
    category_id Serial PRIMARY KEY,
    category_name TEXT NOT NULL,
    category_desc TEXT
);


INSERT INTO categories (category_name, category_desc) VALUES 
('Grocery', 'Everyday grocery and household items'),
('Retail Shopping', 'Clothes, accessories, electronics, and general retail'),
('Food & Dining', 'Restaurants, cafes, and food delivery deals'),
('Healthcare', 'Medicines, diagnostics, and wellness products'),
('Miscellaneous', 'Other category offers');


CREATE TABLE user_profile (
	user_id Serial,
    DOB DATE,
    gender CHAR(1),
    num_likes INT DEFAULT 0,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO user_profile (DOB, gender, num_likes)
VALUES ( '1995-08-14', 'F', 87);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ('1988-11-03', 'F', 45);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ( '2001-06-27', 'M', 66);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ('1990-01-19', 'M', 92);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ('1985-12-05', 'F', 53);

INSERT INTO user_profile (DOB, gender, num_likes)
VALUES ('2000-03-09', 'F', 78);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ('1992-07-22', 'M', 39);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ('1998-10-10', 'F', 24);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ( '1996-04-30', 'M', 88);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ('1983-09-15', 'F', 71);

INSERT INTO user_profile (DOB, gender, num_likes)
VALUES ('1993-05-11', 'M', 33);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ( '2002-02-18', 'M', 95);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ('1991-06-01', 'F', 47);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ('1997-08-08', 'F', 60);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ('1989-03-25', 'M', 19);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ('2003-12-29', 'F', 82);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ( '1994-07-03', 'M', 58);

INSERT INTO user_profile (DOB, gender, num_likes)
VALUES ( '1986-11-20', 'M', 26);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ( '1999-04-17', 'F', 74);

INSERT INTO user_profile ( DOB, gender, num_likes)
VALUES ( '1990-09-06', 'M', 49);

CREATE TABLE deals (
    deal_id serial PRIMARY KEY,
    store_id INT NOT NULL,
    category_id INT NOT NULL,
    deal_desc TEXT,
    deal_amount DECIMAL,
    deal_entered DATE,
    deal_validity DATE,
    user_id INT NOT NULL,
    deal_likes INT DEFAULT 0,
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (9, 1, 'Free shipping on orders over $50', 10.59,
        '2025-04-08', '2025-05-21', 15, 78);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (6, 5, 'Free shipping on orders over $50', 97.5,
        '2025-04-13', '2025-05-31', 3, 98);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (2, 2, 'Refer and earn offer', 92.33,
        '2025-04-12', '2025-05-28', 19, 62);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (3, 4, 'Clearance sale on fashion', 30.85,
        '2025-03-30', '2025-05-02', 1, 77);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (3, 4, 'Clearance sale on fashion', 160.7,
        '2025-03-21', '2025-06-04', 11, 28);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (1, 3, 'Buy 1 Get 1 Free', 82.93,
        '2025-03-28', '2025-05-31', 4, 54);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (2, 3, 'Free shipping on orders over $50', 123.28,
        '2025-03-19', '2025-06-05', 14, 98);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (4, 2, '20% discount on groceries', 174.89,
        '2025-03-18', '2025-06-10', 12, 75);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (1, 3, 'New user discount', 146.17,
        '2025-03-16', '2025-06-05', 17, 93);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (2, 4, 'Clearance sale on fashion', 163.02,
        '2025-04-04', '2025-04-18', 9, 45);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (6, 2, '20% discount on groceries', 139.93,
        '2025-04-11', '2025-04-24', 9, 65);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (10, 3, 'Back to school offer', 15.45,
        '2025-04-07', '2025-06-11', 8, 61);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (8, 1, 'Clearance sale on fashion', 183.36,
        '2025-04-05', '2025-05-19', 16, 4);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (5, 2, '50% off on all electronics', 77.08,
        '2025-03-30', '2025-06-06', 6, 56);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (10, 1, '20% discount on groceries', 43.31,
        '2025-03-17', '2025-04-24', 20, 19);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (1, 4, 'Back to school offer', 193.5,
        '2025-03-21', '2025-06-01', 12, 99);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (10, 4, '20% discount on groceries', 185.32,
        '2025-03-16', '2025-06-01', 18, 3);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (7, 2, 'New user discount', 155.51,
        '2025-04-07', '2025-04-28', 16, 93);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (4, 5, 'Back to school offer', 197.68,
        '2025-03-28', '2025-04-22', 7, 77);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (6, 4, 'Seasonal clearance event', 51.62,
        '2025-04-04', '2025-04-21', 2, 89);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (5, 2, 'Back to school offer', 189.66,
        '2025-04-11', '2025-04-28', 10, 91);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (9, 1, 'Buy 1 Get 1 Free', 44.01,
        '2025-04-01', '2025-04-24', 15, 29);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (4, 1, 'Holiday special deals', 185.44,
        '2025-04-02', '2025-06-08', 19, 55);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (4, 4, 'Refer and earn offer', 187.38,
        '2025-03-22', '2025-04-16', 2, 11);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (4, 5, '20% discount on groceries', 93.91,
        '2025-03-22', '2025-04-20', 18, 28);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (1, 1, '50% off on all electronics', 175.46,
        '2025-04-10', '2025-05-19', 7, 60);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (10, 2, 'Clearance sale on fashion', 139.32,
        '2025-03-27', '2025-05-16', 1, 63);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (6, 3, 'Buy 1 Get 1 Free', 77.81,
        '2025-04-09', '2025-05-16', 14, 31);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (5, 5, 'Back to school offer', 57.65,
        '2025-03-20', '2025-04-29', 17, 60);

INSERT INTO deals (store_id, category_id, deal_desc, deal_amount, deal_entered, deal_validity, user_id, deal_likes)
VALUES (8, 2, '20% discount on groceries', 86.0,
        '2025-03-22', '2025-06-08', 4, 86);
 






