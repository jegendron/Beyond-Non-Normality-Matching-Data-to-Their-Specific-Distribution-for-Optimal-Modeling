# Beyond Non-Normality: Matching Data to Their Specific Distribution for Optimal Modeling

### Purpose
This provides software to assess the joint distribution of a dataset beyond non-normality, testing aspects such as symmetric or skewed. The current version tests whether the residuals are distributed Normally, Student's t, or Beta.


### Files
- `Test Data - Match Joint Distributions.py` — Allows for input data to be assessed 
- `Simulation - Match Joint Distributions.py` — Showcases the ability to capture specific non-normal distributions


## <em>Here is what the first Python file does:</em>
Inputs the residual via an Excel file, then assesses what type of joint distribution it best matches

Below shows the ability for the code to capture the correct distribution, the input data is Beta distributed (left shows the data compared to the Normal distribution, middle shows the data compared to the Student's t distribution, right shows the data compared to the Beta distribution):

<img width="324" height="241" alt="Test Data - Student's t Dist" src="https://github.com/user-attachments/assets/763a13f6-4eeb-4394-8097-58f785b93712" />
<img width="324" height="241" alt="Test Data - Beta Dist" src="https://github.com/user-attachments/assets/a9cba263-6e8c-4ecd-95dd-c2d3988a6db5" />


## <em>Here is what the second Python file does:</em>
Showcases the ability to capture specific non-normality when the dependent variable is Beta or Student's t distributed.

Below shows ability for the code to capture the correct distribution (left shows when the dependent variable is Beta distributed, right shows when the dependent variable is Student's t Distributed):

<img width="324" height="241" alt="Student's t Dist Matched - Simulation" src="https://github.com/user-attachments/assets/cfd1c0ef-e922-473d-93ba-a697abbb587c" />
<img width="324" height="241" alt="Beta Dist Matched - Simulation" src="https://github.com/user-attachments/assets/2dfedc36-2616-429e-a9fe-5c38b8d2422f" />


## <em>Empirical Example:</em>
Sample datasets in experimental economics show that trust behavior was found to be Student's t distributed (bottom left), while trustworthy behavior was found to be Beta distributed (bottom right):

<img width="450" height="350" alt="Sample Student's t Dist Data - Trust in Exp Econ" src="https://github.com/user-attachments/assets/90c4631f-0c73-466b-885d-3365c8384568" />
<img width="450" height="350" alt="Sample Beta Dist Data - Trustworthiness in Exp Econ" src="https://github.com/user-attachments/assets/ef55f8b9-7e48-4347-9161-60741eb38605" />

## <em>Coming Soon:</em>
Additional distributions, currently undergoing testing.
