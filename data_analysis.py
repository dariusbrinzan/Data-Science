import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Cyberpunk_2077_Steam_Reviews.csv'
cyberpunk_reviews = pd.read_csv(file_path)

cyberpunk_reviews['Hours Played'] = pd.to_numeric(cyberpunk_reviews['Hours Played'].str.replace(',', ''), errors='coerce')
cyberpunk_reviews['Date Posted'] = pd.to_datetime(cyberpunk_reviews['Date Posted'], format='%m/%d/%Y', errors='coerce')
cyberpunk_reviews['Voted Helpful'] = pd.to_numeric(cyberpunk_reviews['Voted Helpful'], errors='coerce')
cyberpunk_reviews_clean = cyberpunk_reviews.dropna(subset=['Voted Helpful', 'Rating'])

# 1. Boxplot: Voted Helpful vs Rating
plt.figure(figsize=(10, 6))
cyberpunk_reviews_clean.boxplot(column='Voted Helpful', by='Rating', grid=False, showfliers=False)
plt.title('Voted Helpful by Rating')
plt.suptitle('')
plt.ylabel('Voted Helpful')
plt.xlabel('Rating')
plt.show()

# 2. Line Plot: Number of Reviews over Time
reviews_by_date = cyberpunk_reviews.groupby(cyberpunk_reviews['Date Posted'].dt.to_period('M')).size()

plt.figure(figsize=(10, 6))
reviews_by_date.plot(kind='line')
plt.title('Number of Reviews Over Time')
plt.ylabel('Number of Reviews')
plt.xlabel('Date Posted')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 3. Scatter Plot: Hours Played vs Voted Helpful
plt.figure(figsize=(10, 6))
plt.scatter(cyberpunk_reviews_clean['Hours Played'], cyberpunk_reviews_clean['Voted Helpful'], alpha=0.5, color='purple')
plt.title('Hours Played vs Voted Helpful')
plt.xlabel('Hours Played')
plt.ylabel('Voted Helpful')
plt.xlim(0, 2000)  # Limit the x-axis for better visualization
plt.grid(True)
plt.show()
