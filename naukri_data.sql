
==========Problem 3==================

C:\xampp\mysql\bin> mysql -u root -p

create database edulab;

use edulab;

create table DataAnalyst_ncr(
   job_title VARCHAR(100) NOT NULL,
   experience_req VARCHAR(40) NOT NULL,
   company_name VARCHAR(40) NOT NULL
   link VARCHAR(100),
   keyskills VARCHAR(100),
   job_description VARCHAR(100),
   salary VARCHAR(100),
   job_id INT NOT NULL AUTO_INCREMENT,
   last_updated_on TIMESTAMP,
   PRIMARY KEY ( job_id )
);

==========Problem 4================

create table location_jobs(  
   job_id INT NOT NULL AUTO_INCREMENT,
   locn_id INT NOT NULL AUTO_INCREMENT,
   location VARCHAR(40) NOT NULL,
   PRIMARY KEY ( job_id,locn_id ),
   FOREIGN KEY (job_id) REFERENCES DataAnalyst_ncr(job_id)
);

#splitting multiple location
SELECT *
FROM location_jobs
CROSS APPLY STRING_SPLIT(location, ',');
===========================================================