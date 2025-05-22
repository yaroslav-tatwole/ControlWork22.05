import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Создаем пример данных
data = {
    'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B']
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Создаем count plot
plt.figure(figsize=(6, 4))
sns.countplot(x='category', data=df)

# Добавляем заголовок и метки осей
plt.title('Count Plot of Categories')
plt.xlabel('Category')
plt.ylabel('Count')

# Показываем график
plt.show()