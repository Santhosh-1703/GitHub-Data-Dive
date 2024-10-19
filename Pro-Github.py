import requests
import json
import pandas as pd
from datetime import datetime
import plotly.express as px
import mysql.connector as sql
import pymysql 
import sqlalchemy
from sqlalchemy import create_engine,text
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title='Github Data Drive',page_icon = 'https://pngimg.com/uploads/github/github_PNG80.png', layout="wide")

# Front Page Design
st.markdown("<h1 style='text-align: center; font-weight: bold; font-family: Comic Sans MS;'>Github Data Drive</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Hello Connections! 👋 Welcome to My Project Presentation 🙏</h3>", unsafe_allow_html=True)
selected_page = option_menu(
    menu_title='Options',
    options=["Home", "Analysis Zone","About"],
    icons=["house","clipboard2-data-fill","patch-question"],
    default_index=1,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "black","size":"cover", "width": "100"},
            "icon": {"color": "FF0000", "font-size": "15px"},
            "nav-link": {"font-size": "15px", "text-align": "center", "margin": "-2px", "--hover-color": "#8766FF"},
            "nav-link-selected": {"background-color": "#8766FF"}})

if selected_page == "About":
    st.markdown("<h1 style='color: green;'>Project Conclusion</h1>", unsafe_allow_html=True)
    tab1,tab2 = st.tabs(["Features","Connect with me on"])
    with tab1:
        st.header("This Streamlit application allows users to access and analyze data from Github Repository dataset.", divider='rainbow')
        st.subheader("1.    Users can select specific criteria such as Number of Stars, Forks, Open Issues.")
        st.subheader("2.    Users can access slicers and filters to explore and visualize data in various chart types. They can customize the visualization based on their preferences.")
        st.subheader("3.    The analysis zone provides users with access to different chart types derived through Python scripting.")
        st.subheader("4.    They can explore advanced visualizations, including Scatter plots, and Piecharts, to gain deeper insights into the Repository dataset.")
    with tab2:
             # Create buttons to direct to different website
            linkedin_button = st.button("LinkedIn")
            if linkedin_button:
                st.write("[Redirect to LinkedIn Profile > (https://www.linkedin.com/in/santhosh-r-42220519b/)](https://www.linkedin.com/in/santhosh-r-42220519b/)")

            email_button = st.button("Email")
            if email_button:
                st.write("[Redirect to Gmail > santhoshsrajendran@gmail.com](santhoshsrajendran@gmail.com)")

            github_button = st.button("GitHub")
            if github_button:
                st.write("[Redirect to Github Profile > https://github.com/Santhosh-1703](https://github.com/Santhosh-1703)")

elif selected_page == "Home":
    
    tab1,tab2 = st.tabs(["Github Data Scrapping","  Applications and Libraries Used! "])
    with tab1:
        st.subheader(" Data scraping using a Scraper tool helps users gather valuable insights about Trending Topics, Booming Technology, and user details. By combining this data with information from Github Repo, users can get a comprehensive view of their online presence and audience engagement. This approach enables data-driven decision-making and more effective content strategies.")
        st.write("[:open_book: Learn More  >](https://docs.github.com/en)")
        if st.button("Click here to know about Github"):
            col1, col2 = st.columns(2)
            col1.image(Image.open(r"git.jpg"), width=500)
            with col2:
                st.header(':blue[Github info]', divider='rainbow')
                st.subheader(":star: GitHub is built on top of Git, a distributed version control system, allowing multiple developers to work on projects simultaneously. It enables users to track changes, revert to previous versions, and collaborate on code efficiently through features like branching, pull requests, and issue tracking.")
                st.subheader(":star: GitHub hosts millions of open-source projects, making it a vital platform for developers to share their work, contribute to other projects, and learn from others. Users can fork repositories, suggest changes, and participate in discussions, fostering community-driven development. ")
                st.subheader(":star: GitHub provides various project management features, such as GitHub Projects (Kanban-style boards), issue tracking, milestones, and labels. These tools help teams organize their workflow, prioritize tasks, and monitor progress efficiently. ")
                st.subheader(":star: GitHub integrates with a wide range of third-party tools and services, including CI/CD platforms, project management tools, and code quality checkers. Its API allows developers to create custom integrations and automate workflows, enhancing productivity and streamlining development processes.")
    with tab2:
                st.subheader("  :bulb: Github API")
                st.subheader("  :bulb: Python")
                st.subheader("  :bulb: Pandas")
                st.subheader("  :bulb: Numpy")
                st.subheader("  :bulb: MySQL")

elif selected_page == "Analysis Zone":
    df = pd.read_csv("github_cleaned_data.csv")
    tab_overview, tab_Topic_wise = st.tabs(["**Overview**", "**Topic-wise**"])
    with st.container(border=True): 
        with tab_overview:
            average_stars = df["Number_of_Stars"].mean()
            # 1. General Statistics Section
            st.header(":green[General Statistics]")
            col1,col2,col3 = st.columns(3)
            with col1:
                st.metric("**Total Repositories**", df.shape[0])
                language_count = df['Programming_Language'].value_counts().reset_index()
                language_count.columns = ['Programming_Language', 'count']

                # Create a donut chart for programming language distribution
                fig_language_donut = px.pie(
                        language_count,
                        names='Programming_Language',
                        values='count',
                        hole=0.5,
                        title='Programming Language Distribution',
                        width=600,
                        color_discrete_sequence=px.colors.sequential.Plasma
                    )
                st.plotly_chart(fig_language_donut)
                st.header(" ")

                license_count_Topic = df['License_Type'].value_counts().reset_index()
                license_count_Topic.columns = ['License_Type', 'count']

                    # Create a donut chart for license distribution for the selected Topic
                fig_license_distribution = px.pie(
                        license_count_Topic,
                        names='License_Type',
                        values='count',
                        hole=0.5,
                        title='License Distribution for Repositories',
                        width=600,
                        color_discrete_sequence=px.colors.qualitative.Set2
                    )
                st.plotly_chart(fig_license_distribution)

            with col2:
                col11,col12 = st.columns(2)
                with col11:
                    st.metric("**Average Stars**", int(df["Number_of_Stars"].mean()))
                with col12:
                    st.metric("**Average Forks**", int(df["Number_of_Forks"].mean()))
            with col2:
                st.subheader(":green[Repository Data Table]")
                df.index = df.index + 1
                df = df.drop("ID", axis=1)
                st.dataframe(df)
                st.download_button("Download Data as CSV", df.to_csv(index=False), "repositories.csv")
                st.header(" ")
                # Group by creation date to get total stars and forks over time
                df['year'] = pd.to_datetime(df['Creation_Date']).dt.year 
                trends_df = df.groupby(df["year"]).agg(
                    total_stars=('Number_of_Stars', 'sum'),
                    total_forks=('Number_of_Forks', 'sum')
                ).reset_index()
            
                st.header(":green[Trends Over Time]")
                st.line_chart(trends_df.set_index("year")[["total_stars", "total_forks"]])
            with col3:
                    # Calculating active days
                    df["Creation_Date"] = pd.to_datetime(df["Creation_Date"])
                    df["Last_Updated_Date"] = pd.to_datetime(df["Last_Updated_Date"])
                    df["Active_days"] = (df["Last_Updated_Date"] - df["Creation_Date"]).dt.days
                    st.metric("Average Active Days", int(df["Active_days"].mean()))
            with col3:
                df['year'] = pd.to_datetime(df['Creation_Date']).dt.year 
                yearly_repo_count = df['year'].value_counts().reset_index()
                yearly_repo_count.columns = ['year', 'repository_count']
                yearly_repo_count = yearly_repo_count.sort_values('year')

                    # Create a bar chart for repositories created by each year
                fig_repo_year = px.bar(
                        yearly_repo_count,
                        x='year',
                        y='repository_count',
                        title='Repositories Created by Each Year',
                        labels={'year': 'Year', 'repository_count': 'Repository Count'},
                        width=600,
                        color_discrete_sequence=['#6e40c9']
                    )
                st.plotly_chart(fig_repo_year)
                st.header("")
                st.subheader("")

                top_n = 10  
                top_repositories = df.groupby('Repository_Name')['Number_of_Open_Issues'].sum().nlargest(top_n).index
                grouped_data = df[df['Repository_Name'].isin(top_repositories)]

                # Create the Plotly Express bar chart
                fig = px.bar(
                    grouped_data,
                    x='Programming_Language',
                    y='Number_of_Open_Issues',
                    color='Repository_Name',  # Color by repository name
                    barmode='group',          # Group bars together
                    title='Number of Open Issues per Repository by Programming Language',
                    labels={'Number_of_Open_Issues': 'Number of Open Issues', 'Programming_Language': 'Programming Language'},
                )

                # Update layout for better aesthetics
                fig.update_layout(
                    xaxis_title='Programming Language',
                    yaxis_title='Number of Open Issues',
                    legend_title='Repository Name',
                    xaxis_tickangle=-45,  # Rotate x-axis labels for readability
                )

                # Display in Streamlit
                st.plotly_chart(fig)

        with tab_Topic_wise:
             with st.container(border=True):
                col21,col22 = st.columns(2)
                with col21: 
                    unique_topics = df['Topic'].unique()
                    selected_topics = st.multiselect('Select Topics', options=unique_topics, default=[unique_topics[0]])

                with col22: 
                    years = sorted(df['year'].unique())
                    default_year = years[0]
                    selected_year = st.selectbox("Select Year", years, index=years.index(default_year))
        with tab_Topic_wise:
                # Filter DataFrame based on selected Topics and Year
                filtered_df = df[(df['Topic'].isin(selected_topics)) & (df['year'] == selected_year)]

                # Create two columns in Streamlit layout for charts
                col1, col2 = st.columns(2)

                with col1:
                    # Group by language and get the top 10
                    top_languages = filtered_df['Programming_Language'].value_counts().nlargest(10).reset_index()
                    top_languages.columns = ['language', 'count']

                    # Create a donut chart for top programming languages
                    fig_top_languages = px.pie(top_languages, 
                                                names='language', 
                                                values='count', 
                                                title='Top 10 Programming Languages', 
                                                color_discrete_sequence=px.colors.qualitative.Set1,
                                                hole=0.5)
                    st.plotly_chart(fig_top_languages)
                     # Group by year and Topic, and count the number of repositories
                   # Group by year and Topic, and count the number of repositories
                    yearly_counts = filtered_df.groupby(['year', 'Topic']).size().reset_index(name='repository_count')

                    # Create a bar chart for year-wise repository counts
                    fig_yearly_counts = px.bar(yearly_counts, 
                                                x='year', 
                                                y='repository_count', 
                                                color='Topic',
                                                title='Year-wise Repository Count for Selected Topics',
                                                labels={'repository_count': 'Repository Count', 'year': 'Year'},
                                                height=400,  # Optional: adjust height as needed
                                                barmode='group'  # Optional: group bars by topic
                    )

                    # Display the bar chart in Streamlit
                    st.plotly_chart(fig_yearly_counts)


                with col2:
                    # Group by license type to get the count of each license for the selected Topic
                    license_count_topic = filtered_df['License_Type'].value_counts().reset_index()
                    license_count_topic.columns = ['License_Type', 'count']

                    # Create a donut chart for license distribution for the selected Topic
                    fig_license_distribution = px.pie(
                        license_count_topic,
                        names='License_Type',
                        values='count',
                        hole=0.5,
                        title='License Distribution for Repositories for Selected Topic',
                        color_discrete_sequence=px.colors.qualitative.Set2
                    )
                    st.plotly_chart(fig_license_distribution)

                    # Summarize repository activity for each repository within the filtered Topics
                    activity_summary_repo = filtered_df.groupby('Repository_Name')[['Number_of_Stars', 'Number_of_Forks', 'Number_of_Open_Issues']].sum().reset_index()
                    activity_summary_repo = activity_summary_repo.sort_values('Number_of_Stars', ascending=False).head(10)

                    # Create a bar chart to visualize repository activity for top repositories
                    fig_repo_activity = px.bar(activity_summary_repo, 
                                                x='Repository_Name', 
                                                y=['Number_of_Stars', 'Number_of_Forks', 'Number_of_Open_Issues'],
                                                title='Repository Activity for Selected Topics',
                                                barmode='group')
                    st.plotly_chart(fig_repo_activity)

                

            
