CREATE DATABASE student_management;

USE student_management;

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    class_section VARCHAR(50),
    admission_no VARCHAR(50),
    dob DATE,
    mother_name VARCHAR(100),
    father_name VARCHAR(100),
    phone_no VARCHAR(15),
    address TEXT
);
