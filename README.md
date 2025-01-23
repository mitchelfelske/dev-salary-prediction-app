# Developer Salary Prediction Application

## **Problem**
The lack of clarity regarding adequate remuneration for technology professionals, particularly in software development, creates significant challenges.

### **Consequences**
- Difficulty for developers to understand their market value.
- Challenges for companies in hiring and retaining talent, including prolonged negotiations and dissatisfaction.

## **Objective**
Develop a web application integrated with a machine learning model to predict developers' salaries based on key characteristics.

### **Key Features**
- Geographical location.
- Educational level.
- Specific role within the tech industry.
- Years of experience.

### **Benefits**
- Align expectations between professionals and employers.
- Facilitate hiring processes, salary negotiations, and career management.

## **Proposed Solution**
- Train a predictive model using Python and Scikit-learn, based on historical salary data for developers.
- Build a web application using Flask, served via Gunicorn for robustness and scalability.
- Integrate the machine learning model into the web application to allow users to input relevant variables and receive an instant salary prediction.

### **Impact**
- Transform hiring and career management practices in the tech sector by supporting data-driven decisions.
- Contribute to a more balanced and transparent tech job market.

## **Running the Application**

Open the terminal or command prompt and navigate to the application 'app' folder:

```bash
   cd /path-to-app-folder/app
```

Install the dependencies:

```bash
 pip install -r requirements.txt
```

Execute the application:

```bash
gunicorn -w 4 app:app
```
---

## **Functional Requirements (RF)**

### **RF1 - Data Input**
The application must allow users to input the following information:
- Country where the developer operates.
- Educational level (e.g., high school, undergraduate, postgraduate).
- Specific role (e.g., Front-end Developer, Machine Learning Engineer, Data Scientist).
- Years of experience in the field.

### **RF2 - Prediction Processing**
After user input, the application must process the prediction using the trained ML model and present the predicted salary.

### **RF3 - User Interface Usability**
The application must provide an intuitive and user-friendly interface guiding users through the process.

### **RF4 - Data Validation**
Validate user inputs to ensure correct format before processing predictions.

### **RF5 - Data Exploration**
Enable users to explore historical salary data through interactive visualizations and graphs.

---

## **Non-Functional Requirements (RNF)**

### **RNF1 - Performance**
The application must provide salary predictions within 5 seconds.

### **RNF2 - Scalability**
Support increased numbers of users and requests without significant performance degradation.

### **RNF3 - Security**
Ensure user data security and protect against common web vulnerabilities.

### **RNF4 - Compatibility**
Ensure compatibility with major web browsers (Chrome, Firefox, Safari, Edge).

### **RNF5 - Maintainability**
Implement well-documented and structured code to facilitate future updates.

### **RNF6 - Usability**
Provide a friendly and intuitive interface that guides the user from data input to salary prediction visualization.

---

## **Data Requirements (RD)**

### **RD1 - Database**
The application must use a database containing historical salary data categorized by country, educational level, role, and years of experience.

### **RD2 - Data Cleaning**
Include a procedure to clean and format the data for consistent and accurate predictions.

---

## **System Requirements (RS)**

### **RS1 - Technologies**
- **Web Application**: Python and Flask (backend).
- **Production WSGI Server**: Gunicorn.
- **Machine Learning Model**: Scikit-learn library.

### **RS2 - Hosting**
Host the application in an environment that supports the specified technologies, ensuring high availability and security.
