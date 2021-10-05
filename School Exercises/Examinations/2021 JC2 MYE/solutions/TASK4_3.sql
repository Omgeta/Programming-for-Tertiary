SELECT Subject.Name
FROM School
INNER JOIN Subject ON School.SchoolID = Subject.SchoolID
WHERE School.Name = 'NANYANG JUNIOR COLLEGE';