import pandas as pd
import streamlit as st



st.title("Actividad 1 de Buenas prácticas - Apartado 2")
st.subheader("Compruebe que el fichero existe y que tiene 12 columnas, una para cada mes del año.")
# para esta comprobación el archivo finanzas2020_st2.csv es el original
df = pd.read_csv('finanzas2020_st2.csv', parse_dates=True)
data = pd.DataFrame(df)
st.write("Lectura del fichero Original")
st.write(data)
columnas_df = data.shape
print('Numero de Columnas:', columnas_df[1])

def check_colum(n):
    try:
        assert n == 12, "El DataFrame tiene No 12 Columnas"
        print("El DataFrame tiene 12 Columnas")
        st.write("El DataFrame tiene 12 Columnas")
    except:
        print("El DataFrame No tiene 12 Columnas")
        st.write("El DataFrame No tiene 12 Columnas")

check_colum(columnas_df[1])


st.subheader("Para cada mes compruebe que hay contenido.")
# para esta comprobación el archivo finanzas2020_st2.csv es el original pero detectamos que hay que añadir el sep e indicar que se separan por un tabulador con el \t
df = pd.read_csv('finanzas2020_st2.csv', sep='\t', parse_dates=True)
data = pd.DataFrame(df)
st.write("Lectura del fichero Original ahora indicando que la separación es por tabulación")
st.write(data)
columnas_df = data.shape
#st.write(columnas_df[1])
print('Numero de Columnas:', columnas_df[1],' podemos continuar la comprobación')

def check_data(n,data):
    try:
        assert n == 12, "El DataFrame tiene No 12 Columnas"
        print("El DataFrame tiene 12 Columnas")
        st.write("El DataFrame tiene 12 Columnas, podemos continuar la comprobación.")
        st.subheader("Compruebe que todos los datos son correctos. De no haber un dato correcto, el programa debe saber actuar en consecuencia y continuar con su ejecución.")
        for index in range(data.shape[1]):
            #st.write(f"hago el for {data.columns.values[index]}")
            if data.empty:
                st.write(f"La columna de {data.columns.values[index]}  contiene valores vacios", data.empty)
            else:
                st.write(f"La columna de {data.columns.values[index]} no contiene valores vacios, empty es", data.empty)
                #list_mes = data.tolist()
                #st.write(list_mes[0])
                #data.loc[:, index]
                #st.write(index)
                nam = data.columns.values[index]
                #st.write(data[nam].dtype)
                try:
                    assert data[nam].dtype == 'int64'
                    st.write(f"La columna de {data.columns.values[index]} Contine valores numericos")
                except:
                    st.write(f"La columna de {data.columns.values[index]} Contine valores erroneos, no numericos")

    except:
        print("El DataFrame Está Vacio")
        st.write("El DataFrame Está Vacio")


#modificamos el archivo para hacer un commit
check_data(columnas_df[1],data)
