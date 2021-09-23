SELECT Subject.Name
FROM School
LEFT JOIN Subject ON School.SchoolID = Subject.SchoolID
WHERE School.Name = "NANYANG JUNIOR COLLEGE";