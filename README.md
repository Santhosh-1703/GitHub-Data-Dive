# GitHub Data Dive - Streamlit App

## 1. **Project Overview**

The **GitHub Data Dive** project aims to analyze a dataset of GitHub repositories to uncover trends, insights, and useful metrics such as repository activity, star growth, fork-to-star ratio, and more. The project utilizes Python for data extraction, MySQL for data storage, and Streamlit for interactive visualizations and data analysis.

## 2. **Data Extraction**

The repository data was extracted from GitHub using the **GitHub API**, authenticated with a personal access token, and focused on 10 trending topics in the data science world. Below is a step-by-step breakdown of the extraction process:

### 2.1 **GitHub API Authentication**
- A personal access token was loaded from a file (`token.txt`) to authenticate API requests.
- The token is used to ensure the API calls are authenticated and can retrieve data within GitHub's rate limits.

### 2.2 **API Query and Parameters**
- The GitHub API endpoint used for repository search: `https://api.github.com/search/repositories`.
- The search queries focused on the following trending topics:
 Here’s your list of topics capitalized and numbered:

      1. AI  
      2. Amazon-Sagemaker  
      3. Artificial-Intelligence  
      4. Bioinformatics  
      5. Biopython  
      6. Big-Data  
      7. Blockchain-Technology  
      8. Cloud-Computing  
      9. Cloud Data Platforms  
      10. Computer-Vision  
      11. Cybersecurity  
      12. Data-Analytics  
      13. Data-Engineering  
      14. Data-Mining  
      15. Data-Science  
      16. Data-Visualization  
      17. Deep-Learning  
      18. Generative-AI  
      19. Gen-AI  
      20. Hypothesis-Testing  
      21. Machine-Learning  
      22. MLOps  
      23. MongoDB  
      24. Natural-Language-Processing  
      25. Neural-Networks  
      26. NLP  
      27. PowerBI  
      28. Python  
      29. Quantum-Computing  
      30. Reinforcement Learning  
      31. SQL  
      32. Statistics  
      33. TensorFlow  
      34. Test-Automation  
      35. Time-Series-Analysis  
      36. UI/UX  

- For each topic, repositories were retrieved based on the following parameters:
  - **Query (`q`)**: Topic keyword.
  - **Sort (`sort`)**: Repositories were sorted by the number of stars, highlighting the most popular projects.
  - **Order (`order`)**: Sorted in descending order to fetch the highest-ranked repositories first.
  - **Pagination**: The data was fetched in batches of up to 100 repositories per page to maximize retrieval efficiency, and paginated results were handled using the `page` parameter.

### 2.3 **Error Handling**
- If the API request returned an unsuccessful status code, the process was halted for that topic, and an error message was logged.

## 3. **Project Methodology**

### 3.1 **Data Collection**
- The dataset consists of a collection of GitHub repositories retrieved using the GitHub API.
- Key fields include:
  - `Topic`: Topic of the repo collection.
  - `repository_name`: Name of the repository.
  - `owner`: Repository owner's username.
  - `description`: Repository description.
  - `url`: URL to the repository.
  - `programming_language`: The primary programming language used in the repository.
  - `creation_date`: Date the repository was created.
  - `last_updated_date`: Date the repository was last updated.
  - `number_of_stars`: Total number of stars the repository has received.
  - `number_of_forks`: Total number of forks.
  - `number_of_open_issues`: Number of unresolved issues in the repository.
  - `license_type`: Type of license applied to the repository.

### 3.2 **Data Storage**
- The collected data is stored in a **MySQL** database hosted on Local. The table structure includes the columns mentioned above.

### 3.3 **Data Processing**
- **Pandas** is used to clean and transform the data, preparing it for analysis in the Streamlit app.
- **Streamlit** allows for interactive filtering, trend identification, and visual representation of key metrics.

### 3.4 **Key Objectives**
- Understand repository popularity through stars, forks, and open issues.
- Identify trends in programming language usage.
- Analyze repository activity over time.
- Explore the relationship between repository license types and popularity.
  
## 4. **Streamlit Application Usage Instructions**

### 4.1 **Installation**
Ensure you have installed the required libraries:
```bash
pip install streamlit pandas mysql-connector-python python-dotenv
```

### 4.2 **Setting Up Environment Variables**
The app retrieves MySQL connection details from environment variables. Create a `.env` file in the root directory with the following format:
```
MYSQL_HOST=your-mysql-host
MYSQL_USER=your-mysql-username
MYSQL_PASSWORD=your-mysql-password
MYSQL_DATABASE=your-database-name
MYSQL_PORT=3306
```

### 4.3 **Running the Application**
To launch the Streamlit app, navigate to the project directory and run the following command:
```bash
streamlit run Pro-Github.py
```
### 4.4 **Application Features**

#### 4.4.1 **Sidebar Filters**
- **Programming Language**: Select repositories based on their primary programming language.
- **Repository Name**: Search for repositories by name.
- **License Type**: Filter repositories by their license type.
- **Repository Owners**: Filter repositories based on the owner's username.

#### 4.4.2 **General Statistics**
- **Total Repositories**: Displays the number of repositories in the dataset.
- **Average Stars and Forks**: Shows the average number of stars and forks across all repositories.

#### 4.4.3 **Popular Programming Languages**
- A Pie chart showing the most popular programming languages used in the repositories.

#### 4.4.4 **Top Repository Owners**
- A bar chart highlighting the top repository owners by the number of repositories they own.

#### 4.4.5 **Trends Over Time**
- A line chart tracking the total stars and forks over time, providing insight into trends in repository popularity.

#### 4.4.6 **Repository Data Table**
- A complete table of repositories, with an option to download the data as a CSV file.

## 5. **Key Findings**

### 5.1 **Star Growth Rate**
Repositories with a high **star growth rate** demonstrate rapid adoption and increasing popularity within the developer community. Repositories with frequent updates and active issue resolution tend to accumulate stars faster.

### 5.2 **Fork-to-Star Ratio**
Repositories with a high **fork-to-star ratio** indicate that the community is actively engaging with the project by forking it, often signaling a project that developers are using as a base for their own work.

### 5.3 **Popular Programming Languages**
The analysis revealed that certain languages, like Python and JavaScript, are dominant in terms of repository counts. These languages are often used for a wide range of applications, contributing to their popularity.

### 5.4 **Recent Star Activity**
Repositories that have gained stars recently indicate trending projects that are currently active and may reflect new or growing interest in certain technologies or languages.

## 6. **Deployment**
The app is deployed on Render at: [https://github-data-drive-vhtw.onrender.com/].
