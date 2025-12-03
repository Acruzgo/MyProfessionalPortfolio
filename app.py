import streamlit as st
import pandas as pd
import sqlite3
import os
import streamlit.components.v1 as components

import base64

def load_image_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# Set page config
st.set_page_config(page_title="Argenis Portfolio", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("---")
st.sidebar.markdown("📧 [Email Me](mailto:acruzgo@outlook.com)")
st.sidebar.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/acruzgo/)")
tab = st.sidebar.radio("Go to", ["👨‍💼 Bio", "📘 Capstone Project", "📊 Dashboards", "🛠️ SQL Code", "📄 Resume"])


if tab == "👨‍💼 Bio":

    # --- HEADER ---
    st.markdown("""
        <div style='text-align:center; margin-top:1px;'>
            <h2 style='margin-bottom:0;'>Argenis Cruz-Gonzalez</h2>
            <h1 style='margin-top:1px;'>Professional Portfolio</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Load image as base64
    img_b64 = load_image_base64("images/me_fixed.png")
    img_tag = f"""
<img src="data:image/png;base64,{img_b64}"
     style="position:absolute; top:0; left:0;
            width:100%; height:100%;
            object-fit:cover; object-position:center;">
"""

    # Global CSS for Cards + Badges ✨
    st.markdown("""
<style>

.card {
    transition: all 0.25s ease-in-out;
    position: relative;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 18px rgba(146, 83, 255, 0.65);
}

.card-content {
    padding: 20px;
    font-size: 15px;
}

.card h3 {
    font-size: 22px !important;
    margin-bottom: 14px;
}

/* Badge Grid */
.badge-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(110px, auto));
    gap: 8px;
    justify-content: center;
}

/* Individual Item Badge */
.badge {
    background-color: #262626;
    padding: 6px 14px;
    border-radius: 10px;
    border: 1px solid #3f3f3f;
    font-size: 13px;
    text-align: center;
    transition: all 0.2s ease-in-out;
    white-space: nowrap;
    color: #dcdcdc;
}

.badge:hover {
    background-color: #5f2cff;
    color: white;
    border-color: #9e66ff;
    box-shadow: 0 0 10px rgba(146, 83, 255, 0.6);
    transform: translateY(-3px);
}

</style>
""", unsafe_allow_html=True)


    # Card Style 🍫
    card_style = """
background-color:#1f1f1f;
border:1px solid #3a3a3a;
border-radius:18px;
width:100%;
aspect-ratio:0.95 / 1;
overflow:hidden;
display:flex;
align-items:center;
justify-content:center;
text-align:center;
"""

    # Layout Centering
    outer_left, outer_center, outer_right = st.columns([1.2, 2, 1.2])
    with outer_center:

        # ROW 1 — IMAGE + ABOUT ME
        row1_col1, row1_col2 = st.columns(2)

        with row1_col1:
            st.markdown(
                f"""
<div class="card" style="{card_style}">
{img_tag}
</div>
                """,
                unsafe_allow_html=True
            )

        with row1_col2:
            st.markdown(
                f"""
<div class="card" style="{card_style}">
<div class="card-content">
<h3>💠 About Me</h3>
I work across data, analytics, and workflow optimization — using SQL,
BigQuery, dashboards, and experimentation frameworks to support
insight-driven decisions.
<br><br>
Outside work:
🎮 gaming · 🚣‍♂️ kayaking · 🎨 art · 🎧 music
</div>
</div>
                """,
                unsafe_allow_html=True
            )

        # ROW 2 — TOOLS + SKILLS
        row2_col1, row2_col2 = st.columns(2)

        # 🔧 Tools
        tools = ["Tableau", "Power BI", "Snowflake", "SSMS", "Excel", "GitHub", "Jira", "Perforce"]
        tool_items = "".join([f"<div class='badge'>{t}</div>" for t in tools])

        with row2_col1:
            st.markdown(
                f"""
<div class="card" style="{card_style}">
<div class="card-content">
<h3>🔧 Tools</h3>
<div class="badge-grid">
{tool_items}
</div>
</div>
</div>
                """,
                unsafe_allow_html=True
            )

        # 📊 Skills
        skills = [
            "SQL", "BigQuery", "R Programming", "Cohort Analysis",
            "Experimentation", "Forecasting", "Data Cleaning",
            "KPI Design", "Data Storytelling"
        ]
        skill_items = "".join([f"<div class='badge'>{s}</div>" for s in skills])

        with row2_col2:
            st.markdown(
                f"""
<div class="card" style="{card_style}">
<div class="card-content">
<h3>📊 Skills</h3>
<div class="badge-grid">
{skill_items}
</div>
</div>
</div>
                """,
                unsafe_allow_html=True
            )




# --- CAPSTONE PROJECT ---
elif tab == "📘 Capstone Project":
    st.title("📘 Mobile Game Monetization Analysis – Full Capstone")

    st.markdown("""
    ### 🎮 Overview  
    This capstone explores monetization patterns in a free-to-play mobile game dataset  
    using R, ggplot2, dplyr, and statistical analysis techniques.

    **Click the legend below to view the full interactive report.**
    """)

    try:
        capstone_path = os.path.join("assets", "F2P_Capstone.html")
        with open(capstone_path, "r", encoding="utf-8") as f:
            capstone_html = f.read()

        # IMPORTANT: only embed the HTML here, nowhere else
        components.html(
            capstone_html,
            height=1800,       # keep it contained vertically
            scrolling=True     # scroll only inside the iframe
        )

    except FileNotFoundError:
        st.error("Capstone file not found. Make sure F2P_Capstone.html is in the /assets folder.")


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
    # SQL Project Overview (Collapsible Section)
    with st.expander("Project Overview - *click to expand*"):
        st.markdown("""
    **SQL Business Analytics Project – Tulane University (MBA Program)**  
    This project was developed as part of an MBA-level SQL course, simulating a real-world business scenario involving client behavior, subscription tiers, and employee performance. Using Microsoft SQL Server, I created normalized schemas, imported and cleaned datasets, and built logic-driven queries to extract actionable insights.

    **Key Highlights:**
    - Designed and populated relational schemas using `CREATE TABLE`, `BULK INSERT`, and foreign keys
    - Wrote complex queries to answer business questions across client segmentation, sales attribution, and operational performance
    - Built dynamic views and stored procedures for employee-specific reporting
    - Joined datasets across multiple schemas (App, HR, Restaurant) and used `GROUP BY`, `CASE`, `UNION`, `HAVING`, and aggregation logic
    - Delivered 10+ insights on clients, cities, coffee sales, device usage, and subscription revenue

    **Tools Used:** SQL Server Management Studio (SSMS), Snowflake-compatible syntax
        """)
    st.code(sql_code, language='sql')

# --- DASHBOARDS ---
elif tab == "📊 Dashboards":
    st.title("📊 Interactive Dashboards")

    dashboards = {
        "📈 Advanced Retail Dashboard": {
            "filename": "maven_roasters_dashboard_rebuilt.html",
            "instructions": """\
    ### 📈 Retail Sales Performance Dashboard  
    Built entirely from scratch as part of the *Advanced Tableau Desktop* course by Maven Analytics on LinkedIn Learning. This dashboard visualizes sales trends, product category breakdowns, and regional performance for a fictional coffee brand. Developed using advanced layout design, KPI cards, dynamic sheet swapping, filter menus, and custom visuals — all implemented independently.
    """,
            "height": 1400
        },
        "🧠 Advanced Analytics Dashboard": {
            "filename": "maven_roasters_detail_rebuilt.html",
            "instructions": """\
    ### 🧠 Customer & Warehouse Operations Dashboard  
    Also created independently during the *Advanced Tableau Desktop* course by Maven Analytics. This dashboard simulates operational business intelligence through customer cohorts, picker performance, and fulfillment KPIs. Built using parameter actions, multi-measure displays, set-driven interactivity, and advanced calculated fields — all constructed from a blank Tableau canvas.
    """,
            "height": 2500
        }
    }

    # Dropdown to select one dashboard
    dashboard_choice = st.selectbox("Choose a dashboard to explore:", list(dashboards.keys()))
    selected = dashboards[dashboard_choice]

    # Show text + embed
    st.markdown(selected["instructions"])
    st.markdown("---")

    try:
        with open(os.path.join("assets", selected["filename"]), "r", encoding="utf-8") as f:
            html = f.read()
        st.components.v1.html(html, height=selected["height"], scrolling=True)
    except FileNotFoundError:
        st.error(f"Dashboard file '{selected['filename']}' not found.")

    st.markdown("---")

    # Project notes footer
    st.markdown("""
    ---

    📌 **Dashboard Project Notes:**  
    The *Retail* and *Analytics* dashboards were fully built from scratch as part of the *Advanced Tableau Desktop* course by Maven Analytics on LinkedIn Learning. While the business scenarios were part of the course, every chart, filter, action, and layout was recreated independently to demonstrate mastery of Tableau's advanced design, logic, and storytelling capabilities.
    """)

# --- RESUME ---
elif tab == "📄 Resume":
    st.title("📄 My Resume")

    st.image("images/Argenis_Cruz-Gonzalez_Resume.png", width=850)

    st.markdown("📥 Prefer a PDF copy?")
    st.download_button(
        label="Download My Resume (PDF)",
        data=open("assets/Argenis_Cruz-Gonzalez_Resume.pdf", "rb").read(),
        file_name="Argenis_Cruz-Gonzalez_MBA_Resume.pdf",
        mime="application/pdf"
    )
