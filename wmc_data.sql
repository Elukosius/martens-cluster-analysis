USE wmc_data;
SET GLOBAL local_infile = 1;

CREATE TABLE theme_counts (
    theme VARCHAR(60) PRIMARY KEY,
    paper_count INT
);

LOAD DATA LOCAL INFILE '/Users/elukosius/PycharmProjects/WMCdata/data/theme_counts.csv'
INTO TABLE theme_counts
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

