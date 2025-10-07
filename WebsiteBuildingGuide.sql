DROP DATABASE IF EXISTS web_building_guide;
CREATE DATABASE IF NOT EXISTS web_building_guide;
use web_building_guide;

-- Create Tables
-- WebHostingService(serviceName, isCodable, hasPreBuilt, hasFreeTier, description)
CREATE TABLE WebHostingService( 
  serviceName VARCHAR(30), 
  isCodable BOOLEAN, 
  hasPreBuilt BOOLEAN, 
  hasFreeTier BOOLEAN, 
  description VARCHAR(500), 
  PRIMARY KEY(serviceName)
); 

-- ProgrammingLanguage(languageName, type, needsServerCom)
CREATE TABLE ProgrammingLanguage( 
  languageName VARCHAR(20), 
  type VARCHAR(30), 
  needsServerCom BOOLEAN, 
  PRIMARY KEY (languageName)
); 

-- Tier(serviceName, tierName, cost, costUnit, features)
CREATE TABLE Tier( 
  serviceName VARCHAR(30), 
  tierName VARCHAR(30), 
  cost DECIMAL(4,2), 
  costUnit VARCHAR(30), 
  features VARCHAR(300),
  PRIMARY KEY(serviceName, tierName), 
  FOREIGN KEY(serviceName) REFERENCES WebHostingService(serviceName)
); 

-- ServiceSupports(serviceName, languageName)
 CREATE TABLE ServiceSupports( 
   serviceName VARCHAR(30), 
   languageName VARCHAR(20),
   PRIMARY KEY (serviceName, languageName), 
   FOREIGN KEY(serviceName) REFERENCES WebHostingService(serviceName), 
   FOREIGN KEY(languageName) REFERENCES ProgrammingLanguage(languageName)
 );


 -- Insert Statements
INSERT INTO WebHostingService VALUES
  ('GitHub Pages', TRUE, FALSE, TRUE, 'Creates a static website using JavaScript, HTML, and CSS on a repository to build the website'), 
  ('Hostinger', TRUE, TRUE, FALSE,  'Can host small to medium websites and can host through WordPress'), 
  ('WordPress', TRUE, TRUE, TRUE, 'Can pick a domain name and host a website with it'), 
  ('Pixieset', FALSE, TRUE, TRUE, 'Can host a website'), 
  ('Squarespace', TRUE, TRUE, FALSE, 'Gives template and tools to build website, get a domain name, and then publish it'); 

INSERT INTO ProgrammingLanguage VALUES
  ('JavaScript', 'Dynamic', FALSE), 
  ('HTML', 'Markup', FALSE), 
  ('PHP', 'Scripting', TRUE), 
  ('CSS', 'Markup', FALSE), 
  ('SQL', 'Query', TRUE); 

INSERT INTO Tier VALUES 
  ('Hostinger', 'Premium', 2.49, 'per month', '100 websites, hosting for WordPress, 25,000 visits monthly, 100 GB SSD storage, 400,000 files and directories, automatic website migration, unlimited SSL, an email, weekly backups, WordPress vulnerabilities scanner, standard WordPress acceleration, unlimited bandwidth'), 
  ('Hostinger', 'Business', 3.49, 'per month', '100,000 visits monthly, 200 GB NVMe storage, 600,000 files and directories, daily and on-demand backups, advanced WordPress acceleration, CDN, WordPress AI tools, WordPress staging tool'), 
  ('Hostinger', 'Cloud Startup', 7.59, 'per month', '300 websites, 200,000 visits monthly, 2,000,000 files and directories, dedicated IP address, priority support'), 
  ('Pixieset', 'Free', 0, 'per month', '3 GB photo storage, unlimited galleries'), 
  ('Pixieset', 'Basic', 8, 'per month', 'Free plan features along with 10 GB photo storage, 30 min of video support'),
  ('Squarespace', 'Basic', 16, 'per month', 'templates, free custome domain, Squarespace AI, up to 2 contributors, ability to sell products/services/content/members and send invoices'),
  ('Squarespace', 'Core', 23, 'per month', 'Basic features along with unlimited contributors, website analytics, enables CSS and Javascript, receive a professional email from Google Workspace, sales funnel analytics'),
  ('Squarespace', 'Plus', 39, 'per month', 'Core features along with 50 hours of video hosting and storage and decrease in transaction fees'),
  ('Squarespace', 'Advanced', 99, 'per month', 'Plus features along with no commerce transaction fee, no digital product fee, and unlimited video sotrage');


INSERT INTO ServiceSupports VALUES 
  ('GitHub Pages', 'JavaScript'), 
  ('GitHub Pages', 'HTML'), 
  ('GitHub Pages', 'CSS'), 
  ('WordPress', 'PHP'), 
  ('Hostinger', 'JavaScript');  
