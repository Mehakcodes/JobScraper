import indeedscrape.indeed_jobscape as ij
import pandas as pd

job=input("Enter the job title: ")
loc=input("Enter the location: ")
data=ij.get_indeed_jobdata(job,loc)

# create a dataframe
columns = ['title', 'company', 'location', 'salary', 'job_link']
df = pd.DataFrame(columns=columns)

# append the data to the dataframe
df=pd.concat([df,pd.DataFrame(data,columns=columns)],ignore_index=True)
print(df.head())

# save the data to an excel file
df.to_excel('data.xlsx', index=False)
