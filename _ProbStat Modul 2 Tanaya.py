#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [1, 2, -5, 0.3, 6, -2, 4]  # numeric vector
b = ["one", "two", "three"]     # character vector
c = [True, True, True, False, True]  # logical vector
print(a)
print(b)
print(c)


# In[2]:


#MATRIKS
import numpy as np
cells = [3, 15, -27, 38]
r_tanaya = ["R1", "R2"]
c_tanaya = ["C1", "C2"]
tanaya_matrix = np.matrix(cells).reshape(2, 2)
print(tanaya_matrix)


# In[3]:


import pandas as pd
import numpy as np

tanaya1 = [1, 2, 3, 4]
tanaya2 = ["red", "white", "red", np.nan]  # Menggunakan np.nan untuk merepresentasikan NA
tanaya3 = [True, True, True, False]

data_naya = pd.DataFrame({'ID': tanaya1, 'Color': tanaya2, 'Passed': tanaya3})
print(data_naya)


# In[4]:


import pandas as pd

data_naya = pd.DataFrame({'id': list('abcdefghij'), 'x': list(range(1, 11)), 'y': list(range(11, 21))})
print(data_naya)


# In[5]:


pip install mysql-connector-python


# In[18]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tanaya_houseprices1"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM tanaya_houseprices_1;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[24]:


import pandas as pd
#mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

#filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[df['COL 6'] == 'No']

#menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[22]:


import pandas as pd

df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

df_filtered = df[(df['COL 6'] == 'No') | (df['COL 7'] == 'East')]


print(df_filtered)


# In[31]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PS2[Tanaya]"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM DataPrak"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[32]:


import pandas as pd
#mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

#filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[df['Gender'] == 'Female']

#menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[ ]:




