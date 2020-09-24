from pandas_ods_reader import read_ods
import matplotlib.pyplot as plt

path = "EscolaCovid.ods"

# load a sheet based on its index (1 based)
sheet_idx = 1
df = read_ods(path, sheet_idx)

# load a sheet based on its name
sheet_name = "Sheet1"
df = read_ods(path, sheet_name)

# load a file that does not contain a header row
# if no columns are provided, they will be numbered
df = read_ods(path, 1, headers=False)

# load a file and provide custom column names
# if headers is True (the default), the header row will be overwritten
df = read_ods(path, 1, columns=list('ABCDEFGHI'))
df_grupos_confinados = df[ ['B','G']]
print(df_grupos_confinados)
df.plot(x='B', y='G', label='Grupos Confinados')
plt.title('Confinamiento escuela catalana')


plt.xlabel('Dias lectivos')
plt.ylabel('Grupos confinados')
plt.savefig('grupos_confinados.png')
plt.show()
