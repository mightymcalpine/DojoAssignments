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

#Q4 refactored
SELECT client_id, COUNT(domain_name) AS number_of_sites, MONTHNAME(created_datetime) AS month, YEAR(created_datetime) AS year
FROM sites
WHERE client_id = 1
GROUP BY MONTH(created_datetime), YEAR(created_datetime)
ORDER BY created_datetime;

#Q5 refactored
SELECT sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, "%M %D %Y")
FROM sites
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-02-15"
GROUP BY sites.site_id;

#Q6 refactored
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-12-31"
GROUP BY clients.client_id;

#Q7
#a list of client names and the total # of leads we've generated for each client
#each month between months 1 - 6 of Year 2011
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS client_name, COUNT(leads.leads_id) AS num_of_leads, DATE_FORMAT(leads.registered_datetime, "%M") AS month
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
GROUP BY clients.client_id;

#Q8
#list of client names and the total num of leads we've generated for each of our clients' sites between January 1, 2011
#to December 31, 2011? Order this query by client id. 
#Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated
#from each site for all time
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id)
AS num_of_leads, DATE_FORMAT(leads.registered_datetime, "%M, %D, %Y") AS date_generated 
FROM clients
JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY sites.domain_name
ORDER BY clients.client_id;

SELECT CONCAT(clients.first_name, " ", clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id)
AS num_of_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
#WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY clients.client_id;

#Q9
#retrieves total revenue collected from each client for each month of the year. Order it by client id
SELECT client_id,  SUM(amount) AS revenue, DATE_FORMAT(charged_datetime, "%M") AS month,
DATE_FORMAT(charged_datetime, "%Y") AS year
FROM billing
GROUP BY client_id, MONTH(charged_datetime), YEAR(charged_datetime)
ORDER BY client_id;

#Q10
#retrieves all the sites that each client owns. Group the results so that each row shows a new client.
#It will become clearer when you add a new field called 'sites' that has all the sites that the client owns
#(HINT: use GROUP_CONCAT)
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name) AS sites
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id