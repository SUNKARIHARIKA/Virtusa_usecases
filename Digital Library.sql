-- Create a DataBase
CREATE DATABASE Digital_Library;
USE Digital_Library;
-- Create  Table Books
CREATE TABLE Books(
Book_id INT PRIMARY KEY,
Title VARCHAR(40) NOT NULL,
Author VARCHAR(40),
ISBN_Num VARCHAR(40) UNIQUE,
Category VARCHAR(30) NOT NULL);
-- Create Table Students
CREATE TABLE Students(
Stud_id INT PRIMARY KEY,
Stud_name VARCHAR(40) NOT NULL,
Gender VARCHAR(10),
Age INT);
-- Create Table Issued_Books
CREATE TABLE Issued_Books(
Issue_id INT PRIMARY KEY,
Stud_id INT,
FOREIGN KEY(Stud_id) REFERENCES Students(Stud_id),
Book_id INT,
FOREIGN KEY(Book_id) REFERENCES Books(Book_id),
Issue_date DATE,
Return_date DATE);
-- Insert into Books Table
INSERT INTO Books (Book_id, Title, Author, ISBN_Num, Category) VALUES
(1, 'Database Systems', 'Navathe', 'ISBN001', 'Science'),
(2, 'Operating System Concepts', 'Silberschatz', 'ISBN002', 'Science'),
(3, 'The Great Gatsby', 'F. Scott Fitzgerald', 'ISBN003', 'Fiction'),
(4, 'A Brief History of Time', 'Stephen Hawking', 'ISBN004', 'Science'),
(5, 'World History', 'Norman Lowe', 'ISBN005', 'History'),
(6, 'C Programming', 'Dennis Ritchie', 'ISBN006', 'Technology'),
(7, 'Data Structures', 'Seymour Lipschutz', 'ISBN007', 'Technology'),
(8, 'Harry Potter', 'J.K. Rowling', 'ISBN008', 'Fiction'),
(9, 'Indian Economy', 'Ramesh Singh', 'ISBN009', 'Economics'),
(10, 'Artificial Intelligence', 'Stuart Russell', 'ISBN010', 'Technology');
-- Insert into Students Table
INSERT INTO Students ( Stud_id, Stud_name, Gender, Age) VALUES
(100, 'Harika Sunkari', 'Female', 21),
(102, 'Meghana Sunkari', 'Female', 23),
(103, 'Bhavani Thota', 'Female', 22),
(104, 'Hima Bindu', 'Female', 22),
(105, 'Sowmith Moola', 'Male', 17),
(106, 'Prashanth Rupireddy', 'Male', 20),
(107, 'Nitish Reddy', 'Male', 25),
(108, 'Rohit Sharma', 'Male', 19),
(109, 'Dhanush', 'Male', 18),
(110, 'Dedipya', 'Female', 21);
-- Insert into Issued_books Table
INSERT INTO Issued_Books( Issue_id, Stud_id, Book_id, Issue_date, Return_date) VALUES
(201, 100, 1, '2026-03-01', NULL),
(202, 102, 2, '2026-03-05', NULL),
(203, 103, 3, '2026-02-20', NULL),
(204, 104, 4, '2026-03-01', '2026-03-10'),
(205, 105, 5, '2026-03-10', '2026-03-18'),
(206, 106, 6, '2026-04-01', NULL),
(207, 107, 7, '2026-04-03', NULL),
(208, 100, 8, '2026-03-15', '2026-03-25'),
(209, 108, 5, '2026-03-20', NULL),
(210, 109, 9, '2026-03-18', NULL),
(211, 110, 10, '2026-03-22', NULL),
(212, 102, 1, '2022-01-10', '2022-01-20');
-- quries starts
SELECT * FROM Books;
SELECT * FROM Students;
SELECT * FROM Issued_Books;
-- Overdue Logic
-- To find all students who haven't returned a book where the IssueDate was more than 14 days ago and ReturnDate is NULL
SELECT s.Stud_id, s.Stud_name From
Students s JOIN Issued_Books i 
ON s.Stud_id = i.Stud_id
WHERE (i.Issue_date <= CURRENT_DATE - INTERVAL 14 DAY) AND (i.Return_date IS NULL);
-- Popularity Index
-- Use COUNT and GROUP BY on the Category column to show which genre (e.g., Fiction, Science, History) is borrowed the most.
SELECT COUNT(i.Book_id) AS Number_of_books, b.Category 
FROM Books b JOIN Issued_Books i 
ON b.Book_id = i.Book_id 
GROUP BY b.Category
ORDER BY Number_of_books DESC
LIMIT 1;
-- Data Cleanup
-- Write a DELETE or UPDATE statement to remove student records who haven't borrowed a book in over 3 years (Inactive accounts).
DELETE FROM Students
WHERE Stud_id IN (
    SELECT Stud_id
    FROM Issued_Books
    GROUP BY Stud_id
    HAVING MAX(Issue_date) < CURRENT_DATE - INTERVAL 3 YEAR
);
-- Books issued in last 30 days
SELECT * FROM Issued_Books 
WHERE Issue_date >= CURRENT_DATE - INTERVAL 30 DAY;
-- Last issued date per student
SELECT s.Stud_id, s.Stud_name, MAX(i.Issue_date) AS Last_issued
FROM Students s JOIN Issued_Books i 
ON s.Stud_id = i.Stud_id
GROUP BY i.Stud_id;


