-- Student table
CREATE TABLE Students
(StudentId INT, StudentName VARCHAR(10));

INSERT INTO Students (StudentId, StudentName)
SELECT 1,'John'
UNION ALL
SELECT 2,'Matt'
UNION ALL 
SELECT 3,'James';

-- Class table
CREATE TABLE Classes
(ClassId INT, ClassName VARCHAR(10));

INSERT INTO Classes (ClassId, ClassName)
SELECT 1,'Math'
UNION ALL
SELECT 2,'Art'
UNION ALL 
SELECT 3,'History';

-- StudentClass
CREATE TABLE StudentClass
(StudentId INT, ClassId INT);

INSERT INTO StudentClass (StudentId, ClassId)
SELECT 1, 1
UNION ALL
SELECT 1,2
UNION ALL 
SELECT 3, 1
UNION ALL
SELECT 3, 2
UNION ALL
SELECT 3, 3;

SELECT *
FROM Students;

SELECT *
FROM Classes;

SELECT *
FROM StudentClass;

/* Question 1: What will be the best possible join if we want to retrieve all the students who have signed up
 for the classes  in the summer? */
 SELECT st.StudentName, cl.ClassName
 FROM StudentClass sc
 INNER JOIN Classes cl ON cl.ClassID = sc.ClassID
 INNER JOIN Students st ON st.StudentID = sc.StudentID


