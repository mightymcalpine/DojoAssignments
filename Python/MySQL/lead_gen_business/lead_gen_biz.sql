#Q1
#total revenue for March of 2012?
SELECT MONTHNAME(charged_datetime) AS month, SUM(amount) AS revenue
FROM billing
WHERE charged_datetime >= "2012-03-01" AND "2012-03-31";

#Q2
#total revenue collected from the client with an id of 2
SELECT client_id, SUM(amount) AS revenue
FROM billing
WHERE client_id = 2;

#Q3
#all the sites that client=10 owns?
SELECT clients.client_id, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 10;

#Q3 refactored
SELECT domain_name, client_id
FROM sites
WHERE client_id = 10;

#Q4
#total # of sites created per month per year for the client with an id of 1? What about for client=20

#SELECT sites.client_id, MONTH(sites.created_datetime) AS mnth, COUNT(sites.domain_name), YEAR(sites.created_datetime) AS yr
#FROM sites
#WHERE sites.client_id = 1
#GROUP BY sites.domain_name, mnth, yr;

#Q4 refactored
SELECT client_id, COUNT(domain_name) AS number_of_sites, MONTHNAME(created_datetime) AS month, YEAR(created_datetime) AS year
FROM sites
WHERE client_id = 1
GROUP BY MONTH(created_datetime), YEAR(created_datetime)
ORDER BY created_datetime;

#Q5
#total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011

#SELECT leads.leads_id, sites.domain_name, leads.registered_datetime
#FROM sites
#LEFT JOIN leads ON sites.site_id = leads.site_id
#WHERE leads.registered_datetime > '2011-01-01' AND leads.registered_datetime < '2011-02-16';

#Q5 refactored
SELECT sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, "%M %D %Y")
FROM sites
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-02-15"
GROUP BY sites.site_id;

#Q6
#a list of client names and the total # of leads we've generated for each of our clients
#between January 1, 2011 to December 31, 2011

#SELECT clients.first_name, clients.last_name, SUM(leads.leads_id), leads.registered_datetime
#FROM clients
#LEFT JOIN sites ON clients.client_id = sites.client_id
#LEFT JOIN leads ON sites.site_id = leads.site_id
#WHERE leads.registered_datetime = '2011';

#Q6 refactored
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-12-31"
GROUP BY clients.client_id;