import streamlit as st
import pandas as pd
import sqlite3
import os


# Set page config
st.set_page_config(page_title="Argenis Portfolio", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
tab = st.sidebar.radio("Go to", ["👨‍💼 Bio", "🛠️ SQL Code", "📊 Dashboard"])

# --- BIO ---
if tab == "👨‍💼 Bio":
    st.title("Data Analyst Professional Portfolio")
    st.image("images/me.jpg", caption="Argenis Cruz-Gonzalez", width=150)
    st.markdown("""
    ### About Me
    I’m a data analyst with 6+ years of experience turning messy datasets into actionable insights using SQL, Tableau, and Excel. 
    I specialize in creating clean, intuitive dashboards that drive smarter decisions and tell compelling stories with data.

    - 🎓 MBA Graduate from Tulane University
    - 💼 Past roles in data analytics
    - 🧠 Passionate about automation, data-based insights, and data storytelling

    ### Skills
    - **SQL** (SSMS, Snowflake)
    - **Tableau**, **Power BI**
    - **Excel (Advanced), VBA (Intermediate)**
    """)

# --- SQL CODE ---
elif tab == "🛠️ SQL Code":
    st.title("🛠️ SQL Snippets by Argenis")

    sql_code = """
--Argenis Cruz-Gonzalez
USE Tulane_IT;

--Table Creation (Client)
CREATE TABLE Client(
ClientID INT PRIMARY KEY,
[Name] NVARCHAR(40),
TypeID SMALLINT,
City NVARCHAR(25),
Region NVARCHAR(6),
Pricing SMALLINT
);

--Data Import (Client)
BULK INSERT Client
FROM 'H:\Downloads\Client.csv'
WITH (	FIELDTERMINATOR = ',', --Comma separated between records
		ROWTERMINATOR = '\n', --end of line, new data record starts
		FIRSTROW = 2		); --skipping first row header

--Table Creation (View)
CREATE TABLE [View](
ViewID INT PRIMARY KEY,
ViewDate DATETIME,
ID INT,
Device NVARCHAR(25),
Browser NVARCHAR(30),
Host VARCHAR(15)
);

--Data Import (View)
BULK INSERT [dbo].[View]
FROM 'H:\Downloads\View.txt'
WITH (	FIELDTERMINATOR = '\t', --tab separated between records
		ROWTERMINATOR = '\n', --end of line, new data record starts
		FIRSTROW = 2		); --skipping first row header


--Retrieve top 10 client with the highest number of views
SELECT TOP (10) c.ClientID
	, c.[Name]
	, COUNT(v.ViewID) AS [Number of Views]
FROM Client c INNER JOIN [View] v ON c.ClientID = v.ID
GROUP BY c.ClientID, c.[Name]
ORDER BY [Number of Views] DESC;

--FR3.Q1: Top five (and bottom five) Spas & Salons f names, regions, and the number of views, with the highest (and the lowest) views. You must use a set operator.
SELECT * FROM (SELECT TOP 5 cl.[Name]
	, Count(v.ViewID) AS [Number of Views]
	, ct.TypeName
FROM [App].[ClientType] ct JOIN [App].[Client] cl ON ct.TypeID = cl.TypeID
	JOIN [App].[View] v ON cl.ClientID = v.ID
WHERE ct.TypeID = 14
GROUP BY cl.[Name], ct.TypeName, cl.Region
ORDER BY [Number of Views] DESC
) a
UNION
SELECT * FROM (SELECT TOP 5 cl.[Name]
	, Count(v.ViewID) AS [Number of Views]
	, ct.TypeName
FROM [App].[ClientType] ct JOIN [App].[Client] cl ON ct.TypeID = cl.TypeID
	JOIN [App].[View] v ON cl.ClientID = v.ID
WHERE ct.TypeID = 14
GROUP BY cl.[Name], ct.TypeName, cl.Region
ORDER BY [Number of Views] ASC
) b
ORDER BY [Number of Views] DESC;

--FR3.Q2: All clients whose names start OR end with the text  eGrill f, along with their cities, subscription fees**, and number of views.
SELECT cl.[Name]
	, cl.City
	, FORMAT(pr.Monthly, 'c', 'en-US') AS [Subscription Fee]
	, COUNT(v.ViewID) AS [Number of Views]
FROM [App].[Client] cl JOIN [App].[Pricing] pr ON cl.Pricing = pr.PlanNo
	JOIN [App].[View] v ON cl.ClientID = v.ID
WHERE cl.[Name] LIKE 'grill%'
	OR cl.[Name] LIKE '%grill'
GROUP BY cl.[Name], cl.City, pr.Monthly
ORDER BY [Number of Views] DESC;

--FR3.Q3: Count of client types (Arts & Entertainment, Bakery, etc.) with their average views per client* and average subscription fees per client** sorted with 
--respect to average views per client in descending order.
SELECT ClientViews.ClientID
	, ClientViews.[Name]
	, COUNT(ct.TypeID) AS [Count of Client Types]
	, CONVERT(DECIMAL(10,2),AVG(ClientViews.ViewCount)) AS [Average Views Per Client]
	, FORMAT(AVG(pr.Monthly), 'c', 'en-US') AS [Average Subscription Fee]
FROM 
	(SELECT cl.ClientID
	, cl.[Name]
	, cl.TypeID
	, cl.Pricing
	, COUNT(v.ViewID) AS ViewCount
	FROM [App].[Client] cl JOIN [App].[View] v ON cl.ClientID = v.ID
	GROUP BY cl.ClientID, cl.[Name], cl.TypeID, cl.Pricing) AS ClientViews
	JOIN [App].[ClientType] ct ON ClientViews.TypeID = ct.TypeID
	JOIN [App].[Pricing] pr ON ClientViews.Pricing = pr.PlanNo
GROUP BY ClientViews.ClientID, ClientViews.[Name]
ORDER BY [Average Views Per Client] DESC;

--FR3.Q4: Cities (along with their regions) for which the total number of views for non-restaurant clients is more than 15.
SELECT cl.City
	, cl.Region
	, COUNT(v.ViewID) AS [Number of Views]
FROM [App].[Client] cl JOIN [App].[View] v ON cl.ClientID = v.ID
	JOIN [App].[ClientType] ct ON cl.TypeID = ct.TypeID
WHERE ct.TypeID <> '13'
GROUP BY cl.City, cl.Region
HAVING COUNT(v.ViewID) > 15;

--FR3.Q5: States (regions) with number of clients and number of coffee customers for those states (regions) in which there are both types of customers.
--(IT and Coffee Customers)
SELECT IT_Clients.Region AS [State]
	, [IT Clients]
	, [Coffee Customers]
	FROM (SELECT cl.Region
			, COUNT(cl.ClientID) AS [IT Clients]
			FROM [App].[Client] cl
			GROUP BY cl.Region) AS IT_Clients
JOIN
	(SELECT cu.[State]
			, COUNT(cu.CustomerNum) AS [Coffee Customers]
			FROM [Restaurant].[Customer] cu
			GROUP BY cu.State) AS Coffee_Customers
	ON IT_Clients.Region = Coffee_Customers.[State];

--FR3.Q6: Number of clients, their total fees**, total views, and average fees per view** with respect to regions, sorted in descending order of average fees per view.
SELECT ClientViews.Region
	, COUNT(ClientViews.ClientID) AS [Number of Clients]
	, FORMAT(SUM(ClientViews.Monthly), 'C', 'en-US') AS [Total Fees]
	, COUNT(ClientViews.ViewID) AS [Total Views]
	, FORMAT(AVG(ClientViews.Monthly), 'C', 'en-US') AS [Average Fees Per View]
FROM
	(SELECT cl.ClientID
		, COUNT(v.ViewID) AS [Total Views]
		, p.Monthly
		, cl.Region
		, v.ViewID
		FROM [App].[Client] cl JOIN [App].[Pricing] p ON cl.Pricing = p.PlanNo
		JOIN [App].[View] v ON cl.ClientID = v.ID
		GROUP BY cl.ClientID, p.Monthly, cl.Region, v.ViewID) AS ClientViews
GROUP BY ClientViews.Region
ORDER BY AVG(ClientViews.Monthly) DESC;

--FR3.Q7: All views (all columns) that took place after October 15th, by Kindle devices, hosted by Yelp from cities where there are more than 20 clients. Also add the 
--name and the city of the client as last columns for each view.
SELECT v.ViewID
	, v.ViewDate
	, v.ID
	, v.Device
	, v.Browser
	, v.Host
	, cl.[Name]
	, cl.City
FROM [App].[View] v JOIN [App].[Client] cl ON v.ID = cl.ClientID
WHERE v.Host = 'yelp' 
	AND v.Device LIKE '%kindle%'
	AND v.ViewDate > '10/15/2022'
    AND cl.City IN 
		(SELECT cl.City
        FROM [App].[Client] cl
        GROUP BY cl.City
        HAVING COUNT(cl.ClientID) > 20);

--FR3.Q8: All non-executive employee full names, number of their regions, number of their clients, number of views for those clients, number of distinct coffee customers, 
--and total coffee sales**. If there is no coffee sale for an employee, write  gNot a coffee agent h instead of NULL values. (Hint: you can use CASE statements.)

SELECT EmployeesByRegion.EmployeeID
	, EmployeesByRegion.FirstName + ' ' + EmployeesByRegion.LastName AS FullName
	, COUNT(DISTINCT EmployeesByRegion.Region) AS [Number of Regions]
	, COUNT(DISTINCT EmployeesByRegion.ClientID) AS [Number of Clients]
	, COUNT(DISTINCT EmployeesByRegion.ViewID) AS [Number of Views]
	, COUNT(DISTINCT CustomersByRegion.CustomerNum) AS [Coffee Customers]
	, CASE
		WHEN SUM(DISTINCT CustomersByRegion.[Coffee Sales]) IS NULL THEN 'Not a Coffee Agent'
		ELSE FORMAT(SUM(DISTINCT CustomersByRegion.[Coffee Sales]), 'C', 'en-US')
	END AS [Total Coffee Sales]
FROM 
	(SELECT e.EmployeeID
	, e.FirstName
	, e.LastName
	, r.Region
	, cl.ClientID
	, v.ViewID
	FROM [HumanResources].[Employee] e JOIN [HumanResources].[AgentRegion] r ON e.EmployeeID = r.EmployeeID
		JOIN [App].[Client] cl ON r.Region = cl.Region
		JOIN [App].[View]v  ON cl.ClientID = v.ID
	) AS EmployeesByRegion
FULL JOIN
	(SELECT DISTINCT cu.[State]
		, cu.CustomerNum
		, o.OrderAmountKg*co.PricePerKg AS [Coffee Sales]
	FROM [Restaurant].[Customer] cu JOIN [Restaurant].[Order] o ON cu.CustomerNum = o.CustomerNum
	JOIN [Restaurant].[Coffee] co ON o.CoffeeID = co.CoffeeID
	) AS CustomersByRegion
ON EmployeesByRegion.Region = CustomersByRegion.[State]
GROUP BY EmployeesByRegion.EmployeeID, EmployeesByRegion.FirstName, EmployeesByRegion.LastName

--FR3.Q9: Create a view named vEmployeeClientCustomer based on the query in FR3.Q8.
CREATE VIEW vEmployeeClientCustomer --DO NOT RUN AGAIN
AS 
SELECT EmployeesByRegion.EmployeeID
	, EmployeesByRegion.FirstName + ' ' + EmployeesByRegion.LastName AS FullName
	, COUNT(DISTINCT EmployeesByRegion.Region) AS [Number of Regions]
	, COUNT(DISTINCT EmployeesByRegion.ClientID) AS [Number of Clients]
	, COUNT(DISTINCT EmployeesByRegion.ViewID) AS [Number of Views]
	, COUNT(DISTINCT CustomersByRegion.CustomerNum) AS [Coffee Customers]
	, CASE
		WHEN SUM(DISTINCT CustomersByRegion.[Coffee Sales]) IS NULL THEN 'Not a Coffee Agent'
		ELSE FORMAT(SUM(DISTINCT CustomersByRegion.[Coffee Sales]), 'C', 'en-US')
	END AS [Total Coffee Sales]
FROM 
	(SELECT e.EmployeeID
	, e.FirstName
	, e.LastName
	, r.Region
	, cl.ClientID
	, v.ViewID
	FROM [HumanResources].[Employee] e JOIN [HumanResources].[AgentRegion] r ON e.EmployeeID = r.EmployeeID
		JOIN [App].[Client] cl ON r.Region = cl.Region
		JOIN [App].[View]v  ON cl.ClientID = v.ID
	) AS EmployeesByRegion
FULL JOIN
	(SELECT DISTINCT cu.[State]
		, cu.CustomerNum
		, o.OrderAmountKg*co.PricePerKg AS [Coffee Sales]
	FROM [Restaurant].[Customer] cu JOIN [Restaurant].[Order] o ON cu.CustomerNum = o.CustomerNum
	JOIN [Restaurant].[Coffee] co ON o.CoffeeID = co.CoffeeID
	) AS CustomersByRegion
ON EmployeesByRegion.Region = CustomersByRegion.[State]
GROUP BY EmployeesByRegion.EmployeeID, EmployeesByRegion.FirstName, EmployeesByRegion.LastName

SELECT * FROM [dbo].[vEmployeeClientCustomer]

--FR3.Q10: Create a stored procedure named spEmployeeReport based on the view in FR3.Q9, for which you will pass the last name of the employee only. The result should be FR3.Q9 
--only for that employee. (Hint: You may use: Fullname LIKE '% ' + @Lastname)
CREATE PROC spEmployeeReport --DO NOT RUN AGAIN
@LastName NVARCHAR(30)
AS
SELECT * FROM [dbo].[vEmployeeClientCustomer]
WHERE FullName LIKE '% ' + @LastName

EXEC spEmployeeReport @LastName = 'Cena'


--FR4
--Restaurant Average Number of Views per Hour in October
SELECT RestaurantClients.[Hour]
	, AVG(RestaurantClients.[Number of Views]) AS [Average Number of Views]
	, 'Restaurant' AS [Client Type]
FROM
	(
	SELECT DATEPART(HOUR, v.ViewDate) AS [Hour]
		, COUNT(v.ViewID) AS [Number of Views]
	FROM [App].[View] v
		JOIN [App].[Client] c ON v.ID = c.ClientID
		JOIN [App].[ClientType] ct ON c.TypeID = ct.TypeID
	WHERE MONTH(v.ViewDate) = 10
	AND ct.TypeID = '13'
	GROUP BY DATEPART(HOUR, v.ViewDate)
	) AS RestaurantClients
GROUP BY RestaurantClients.[Hour]
ORDER BY RestaurantClients.[Hour] ASC;

--Non-Restaurant Average Number of Views per Hour in October
SELECT RestaurantClients.[Hour]
	, AVG(RestaurantClients.[Number of Views]) AS [Average Number of Views]
	, 'Non-Restaurant' AS [Client Type]
FROM
	(
	SELECT DATEPART(HOUR, v.ViewDate) AS [Hour]
		, COUNT(v.ViewID) AS [Number of Views]
	FROM [App].[View] v
		JOIN [App].[Client] c ON v.ID = c.ClientID
		JOIN [App].[ClientType] ct ON c.TypeID = ct.TypeID
	WHERE MONTH(v.ViewDate) = 10
	AND ct.TypeID <> '13'
	GROUP BY DATEPART(HOUR, v.ViewDate)
	) AS RestaurantClients
GROUP BY RestaurantClients.[Hour]
ORDER BY RestaurantClients.[Hour] ASC;
    """

    st.code(sql_code, language='sql')

# --- DASHBOARD ---
elif tab == "📊 Dashboard":
    st.title("📊 Interactive Dashboards")

    dashboards = {
        "🎮 Game Sales Dashboard": {
            "filename": "tableau_dashboard.html",
            "instructions": "### 🎮 Please click a genre to interact with the dashboard below",
            "height": 900
        },
        "📈 Advanced Retail Dashboard": {
            "filename": "maven_roasters_dashboard_rebuilt.html",
            "instructions": "### 📈 Analyze monthly sales trends and category performance\nPlease click the '?' icon for info on navigating the dashboard.",
            "height": 1400
        },
        "🧠 Advanced Analytics Dashboard": {
            "filename": "maven_roasters_detail_rebuilt.html",
            "instructions": "### 🧠 Explore customer and warehouse analytics\nInteract with Picker Stats Table by selecting a Picker Name and watch the data come to life!",
            "height": 2500
        }
    }

    # Dropdown to select one dashboard
    dashboard_choice = st.selectbox("Choose a dashboard to explore:", list(dashboards.keys()))
    selected = dashboards[dashboard_choice]

    # Show instructions and embedded HTML
    st.markdown(selected["instructions"])
    st.markdown("---")
    try:
        with open(os.path.join("assets", selected["filename"]), "r", encoding="utf-8") as f:
            html = f.read()
        st.components.v1.html(html, height=selected["height"], scrolling=False)
    except FileNotFoundError:
        st.error(f"Dashboard file '{selected['filename']}' not found.")
    st.markdown("---")

    # Footer (only once)
    st.markdown("Some dashboards were recreated as part of a hands-on LinkedIn Learning course by Maven Analytics.")
    st.markdown("The goal was to fully rebuild the dashboard from scratch to practice and reinforce key Tableau skills,")
    st.markdown("including advanced interactivity, calculations, formatting, and design consistency.")
    st.markdown("While the structure closely follows the original instructional version, all work shown here was implemented")
    st.markdown("independently as part of the learning process. No original course files were reused. This project helped me")
    st.markdown("strengthen my end-to-end Tableau workflow, from data preparation to final visualization.")
