import streamlit as st
import pandas as pd
import sqlite3
import os
import streamlit.components.v1 as components
import textwrap
import base64

def load_image_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# --- GLOBAL PAGE CONFIG (collapsed sidebar) ---
st.set_page_config(
    page_title="Argenis Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- SIDEBAR + TOGGLE STYLING ---
st.markdown("""
<style>

[data-testid="stSidebar"] {
    background-color: #161616;
    border-right: 1px solid #2a2a2a;
}

/* Avatar */
.sidebar-avatar img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #A46BFD;
    box-shadow: 0 0 12px rgba(146, 83, 255, 0.5);
}

/* Name + Title */
.sidebar-name {
    margin-top: 10px;
    font-size: 15px;
    font-weight: 600;
    color: #f2f2f2;
}

.sidebar-role {
    font-size: 12px;
    color: #9b9b9b;
    margin-top: -6px;
}

<style>

/* Target the wrapper DIV found in HTML */
div.st-emotion-cache-8ezv7j {
    position: relative !important;
    z-index: 999999 !important;
}

/* Target the actual glowing button */
div.st-emotion-cache-8ezv7j button {
    background: rgba(130, 0, 255, 0.35) !important;
    border-radius: 14px !important;
    border: 2px solid rgba(180, 0, 255, 0.8) !important;

    /* 💜 MASSIVE NEON PURPLE GLOW */
    box-shadow:
        0 0 22px #8a2be2,
        0 0 44px #8a2be2,
        0 0 88px #8a2be2,
        0 0 132px rgba(138, 43, 226, 0.95) !important;

    animation: pulseGlow 2s infinite ease-in-out;
    transition: all 0.2s;
}

/* Pulse effect — always glowing */
@keyframes pulseGlow {
    0%, 100% {
        box-shadow:
            0 0 18px #bf00ff,
            0 0 55px #bf00ff,
            0 0 110px rgba(140, 0, 255, 1);
        transform: scale(1);
    }
    50% {
        box-shadow:
            0 0 35px #e000ff,
            0 0 105px #e000ff,
            0 0 160px rgba(200, 0, 255, 1);
        transform: scale(1.18);
    }
}

/* Icon brightness */
div.st-emotion-cache-8ezv7j button span[data-testid="stIconMaterial"] {
    color: #ffffff !important;
    font-size: 25px !important;
    filter: drop-shadow(0 0 10px #ffffff);
}

</style>

""", unsafe_allow_html=True)

# --- SIDEBAR PROFILE UI ---
avatar_b64 = load_image_base64("images/me_fixed.png")

st.sidebar.markdown(
    f"""
    <div style="text-align:center; padding-top:10px;">
        <span class="sidebar-avatar">
            <img src="data:image/png;base64,{avatar_b64}">
        </span>
        <div class="sidebar-name">Argenis Cruz-Gonzalez</div>
        <div class="sidebar-role">Data & Analytics Professional</div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("---")
tab = st.sidebar.radio(
    "Go to",
    ["👨‍💼 Bio", "🐍 Waze Retention Analysis (Python)", "🎮 Mobile Game Monetization Analysis (R)", "📊 Dashboards", "🔍 SQL Code", "📄 Resume"]
)
st.sidebar.markdown("---")
st.sidebar.markdown("📧 [Email Me](mailto:acruzgo@outlook.com)")
st.sidebar.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/acruzgo/)")


if tab == "👨‍💼 Bio":

    img_b64 = load_image_base64("images/me_fixed.png")

    html = f"""
    <html>
    <head>
    <style>

    /* 👇 Fade + Drop + Temporary Glow Animation for Cards */
    .fade-drop {{
        opacity: 0;
        transform: translateY(-35px);
        animation: fadeDropGlow 0.9s ease-out forwards;
    }}

    .grid .card:nth-child(1) {{ animation-delay: 0.12s; }}
    .grid .card:nth-child(2) {{ animation-delay: 0.24s; }}
    .grid .card:nth-child(3) {{ animation-delay: 0.36s; }}
    .grid .card:nth-child(4) {{ animation-delay: 0.48s; }}

    @keyframes fadeDropGlow {{
        0% {{
            opacity: 0;
            transform: translateY(-35px);
            box-shadow: 0 0 18px rgba(146,83,255,0.6);
        }}
        60% {{
            opacity: 1;
            transform: translateY(8px);
            box-shadow: 0 0 28px rgba(146,83,255,0.9);
        }}
        100% {{
            opacity: 1;
            transform: translateY(0);
            box-shadow: none;
        }}
    }}

    /* ⌨️ Faster Typing + Clean Cursor Finish */
    .typing {{
    width: 0;
    overflow: hidden;
    white-space: nowrap;
    display: inline-block;
    animation: typing 4.5s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
    }}
    
    @keyframes typing {{
        from {{ width: 0; }}
        to {{ width: 100%; }}
    }}



    .typing.finished {{
        border-right: none !important;
    }}

    @keyframes typing {{
        from {{ width: 0; }}
        to {{ width: 100%; }}
    }}

    @keyframes blink {{
        50% {{ border-color: transparent; }}
    }}

    /* 🎨 Page Styling */
    body {{
        font-family: 'Inter', sans-serif;
        background: #111;
        color: #eee;
        margin: 0;
        padding: 0;
        text-align: center;
    }}

    .wrapper {{
        max-width: 1150px;
        margin: auto;
        padding-top: 20px;
    }}

    h1, h2 {{
        margin: 0;
    }}

    /* 🟥 Card Layout + Size */
    .grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(390px, 1fr));
        gap: 28px;
        margin-top: 40px;
        justify-items: center;
    }}

    .card {{
        background: #1f1f1f;
        border: 1px solid #333;
        border-radius: 18px;
        aspect-ratio: 1 / 1;
        width: 100%;
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: .25s ease;
    }}

    .card:hover {{
        transform: translateY(-6px);
        box-shadow: 0 0 18px rgba(146,83,255,0.55);
    }}

    .content {{
        padding: 20px;
    }}

    .badges {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 8px;
        margin-top: 10px;
    }}

    .badge {{
        background:#222;
        border:1px solid #444;
        border-radius:10px;
        padding:7px 14px;
        font-size:13px;
        white-space:nowrap;
        transition:.2s;
    }}

    .badge:hover {{
        background:#5f2cff;
        border-color:#9e66ff;
        color:#fff;
        transform:translateY(-3px);
    }}

    .photo {{
        position:absolute;
        inset:0;
        width:100%;
        height:100%;
        object-fit:cover;
        border-radius:18px;
    }}

    </style>
    </head>

    <body>

    <div class="wrapper">
        <h2 class="typing" id="name">Argenis Cruz-Gonzalez</h2><br>
        <h1 class="typing" id="title">Professional Portfolio</h1>


        <div class="grid">
            <div class="card fade-drop">
                <img src="data:image/png;base64,{img_b64}" class="photo">
            </div>

            <div class="card fade-drop">
                <div class="content">
                    <h3>💠 About Me</h3>
                    I work across data, analytics, and workflow optimization —
                    using Python, SQL, dashboards, and experimentation to
                    improve decision-making.
                    <br><br>
                    Outside work:<br>
                    🎮 Gaming · 🚣‍♂️ Kayaking · 🎨 Art · 🎧 Music
                </div>
            </div>

            <div class="card fade-drop">
                <div class="content">
                    <h3>🛠️ Tools</h3>
                    <div class="badges">
                        {''.join([f"<div class='badge'>{t}</div>" for t in ["Tableau", "Power BI", "Jupyter Notebooks", "PyCharm", "Snowflake", "SSMS", "Excel", "GitHub", "Jira", "Perforce"]])}
                    </div>
                </div>
            </div>

            <div class="card fade-drop">
                <div class="content">
                    <h3>📊 Skills</h3>
                    <div class="badges">
                        {''.join([f"<div class='badge'>{s}</div>" for s in ["Python (pandas, numpy, seaborn, matplotlib)", "SQL", "BigQuery", "R Programming (tidyverse, ggplot2, reshape2, corrplot)", "Cohort Analysis", "Experimentation", "Forecasting", "Data Cleaning", "KPI Design", "Data Storytelling"]])}
                    </div>
                </div>
            </div>

        </div>
    </div>

    <!-- JavaScript: Remove cursor after typing -->
    <script>
    document.addEventListener("DOMContentLoaded", function() {{
        setTimeout(() => {{
            document.querySelectorAll(".typing").forEach(el =>
                el.classList.add("finished")
            );
        }}, 2000);
    }});
    </script>

    </body>
    </html>
    """

    components.html(html, height=1600, scrolling=True)

# --- Waze Retention Analysis (Python) (R) ---
elif tab == "🐍 Waze Retention Analysis (Python)":
    st.title("Waze User Retention & Churn Analysis (Python)")

    st.markdown("""
    ### Project Overview  
    This project explores user engagement, driving behavior, and churn patterns using the Waze public dataset.
    The analysis focuses on understanding how usage frequency, driving distance, account age, and device type
    relate to whether users stay engaged or churn.

    Built entirely in **Python**, the project uses:
    - pandas for data wrangling  
    - seaborn & matplotlib for visualization  
    - exploratory data analysis to identify churn risk signals  

    **Use the interactive report below to explore findings.**
    """)

    try:
        waze_path = os.path.join("assets", "Waze_Churn_Analysis.html")
        with open(waze_path, "r", encoding="utf-8") as f:
            waze_html = f.read()
        components.html(
            waze_html,
            height=1800,
            scrolling=True
        )

    except FileNotFoundError:
        st.error("Waze analysis file not found. Make sure Waze_Retention_Analysis.html is in the /assets folder.")

# --- Mobile Game Monetization Analysis (R) ---
elif tab == "🎮 Mobile Game Monetization Analysis (R)":
    st.title("Mobile Game Monetization Analysis – Full Capstone")

    st.markdown("""
    ### Project Overview   
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
elif tab == "🔍 SQL Code":
    st.title("SQL Snippets by Argenis")

    # --- Define SQL FIRST (outside UI containers) ---
    sql_code = """
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
    # --- Project Overview (always visible) ---
    st.markdown("""
    **SQL Business Analytics Project – Tulane University (MBA Program)**  
    This project simulates a real-world business scenario involving client behavior,
    subscription tiers, and employee performance using Microsoft SQL Server.

    **Key Highlights:**
    - Designed normalized schemas and populated datasets
    - Built analytical queries and reporting views
    - Implemented stored procedures for dynamic reporting
    """)

    st.markdown("---")
    st.caption("⬇️ Expand below to view the full SQL implementation")

    # --- SQL CODE (ONLY collapsible part) ---
    with st.expander("🧠 View Full SQL Code"):
        st.code(sql_code, language="sql", line_numbers=True)

        st.download_button(
            "📥 Download SQL Script",
            sql_code,
            "argeniscg_sql_project.sql",
            "text/plain"
        )

# --- DASHBOARDS ---
elif tab == "📊 Dashboards":
    st.title("Interactive Dashboards")

    dashboards = {
        "📈 Advanced Retail Dashboard": {
            "filename": "maven_roasters_dashboard_rebuilt.html",
            "instructions": """\
    ### Retail Sales Performance Dashboard  
    Built entirely from scratch as part of the *Advanced Tableau Desktop* course by Maven Analytics on LinkedIn Learning. This dashboard visualizes sales trends, product category breakdowns, and regional performance for a fictional coffee brand. Developed using advanced layout design, KPI cards, dynamic sheet swapping, filter menus, and custom visuals — all implemented independently.
    """,
            "height": 1400
        },
        "📋 Advanced Analytics Dashboard": {
            "filename": "maven_roasters_detail_rebuilt.html",
            "instructions": """\
    ### Customer & Warehouse Operations Dashboard  
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
