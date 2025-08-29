import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import geopandas as gpd
from shapely.geometry import Point

# Configuración de fuente global
plt.rcParams['font.size'] = 6
plt.rcParams['axes.titlesize'] = 6
plt.rcParams['axes.labelsize'] = 6
plt.rcParams['xtick.labelsize'] = 6
plt.rcParams['ytick.labelsize'] = 6
plt.rcParams['legend.fontsize'] = 6

# Rutas a directorios de archivos
txt_directory_path = r'C:\Users\WINDOWS\Documents\GPS_strain_CR\GPS'
shp_directory_path = r'C:\Users\WINDOWS\Documents\GPS_strain_CR\perfiles_GPS'

# Nombres de archivos
file_names = ["marga_alph10.txt", "marga_alph15.txt", "marga_alph20.txt", 
              "marga_alph25.txt", "marga_alph30.txt", "marga_alph40.txt", 
              "marga_alph50.txt", "marga_alph60.txt", "marga_alph70.txt"]

# Orden de archivos shapefile
shp_files = ["PN_W_lat.shp", "PN_C_lat.shp", "PN_E_lat.shp", "PN_N_lon.shp", "PN_S_lon.shp"]

# Mapa de colores y buffers
color_map = {os.path.splitext(file)[0]: plt.cm.tab10(i % 10) for i, file in enumerate(file_names)}
buffer_sizes = {'PN_W_lat.shp': 40000, 'PN_S_lon.shp': 10000, 
                'PN_N_lon.shp': 10000, 'PN_E_lat.shp': 40000, 
                'PN_C_lat.shp': 40000}

# Cargar datos
def load_and_clean_data(file_path):
    try:
        df = pd.read_csv(file_path, delim_whitespace=True, skiprows=0)
        df.columns = df.columns.str.strip()
        return df
    except pd.errors.ParserError as e:
        print(f"Error en {file_path}: {e}")
        return None

data_frames = []
for file in file_names:
    full_path = os.path.join(txt_directory_path, file)
    if os.path.exists(full_path):
        df = load_and_clean_data(full_path)
        if df is not None:
            df['label'] = os.path.splitext(file)[0]
            data_frames.append(df)

all_data = pd.concat(data_frames)
all_data['geometry'] = all_data.apply(lambda row: Point(row['x'], row['y']), axis=1)
geo_data = gpd.GeoDataFrame(all_data, geometry='geometry', crs='EPSG:4326').to_crs(epsg=32620)

shapefiles = {name: os.path.join(shp_directory_path, name) for name in shp_files}
gdfs = {name: gpd.read_file(path).to_crs(epsg=32620) for name, path in shapefiles.items()}

# Categorías de datos
categories = ['dilation', 'rotation', 'maxShear']

# Crear figura con subgráficos
fig, axs = plt.subplots(nrows=len(gdfs), ncols=len(categories), figsize=(9, 18), 
                        gridspec_kw={'hspace': 0.5, 'wspace': 0.5})

for col_idx, column in enumerate(categories):
    for row_idx, (name, gdf) in enumerate(gdfs.items()):
        buffered_gdf = gdf.buffer(buffer_sizes[name])
        buffer_union = buffered_gdf.unary_union
        selected_data = geo_data[geo_data.geometry.within(buffer_union)].copy()

        if selected_data.empty:
            continue

        # Línea del perfil
        line = gdf.geometry.unary_union
        # Calcular distancia proyectada acumulada en km
        selected_data["dist_km"] = selected_data.geometry.apply(lambda p: line.project(p) / 1000.0)

        x_all = []
        y_all = []
        for label, df in selected_data.groupby('label'):
            axs[row_idx, col_idx].scatter(df['dist_km'], df[column], s=5, c=color_map[label], label=label)
            x_all.extend(df['dist_km'])
            y_all.extend(df[column])
        
        if len(x_all) > 1:
            x_all = np.array(x_all)
            y_all = np.array(y_all)
            p = np.polyfit(x_all, y_all, 5)
            x_fit = np.linspace(min(x_all), max(x_all), 1000)
            y_fit = np.polyval(p, x_fit)
            axs[row_idx, col_idx].plot(x_fit, y_fit, color='black', linestyle='--')
        
        axs[row_idx, col_idx].set_title(f"{column.capitalize()} - {name.split('.')[0]}")
        axs[row_idx, col_idx].set_xlabel('Distancia a lo largo del perfil (km)')
        axs[row_idx, col_idx].set_ylabel(column.capitalize())
        axs[row_idx, col_idx].tick_params(axis='y', rotation=90)
        axs[row_idx, col_idx].ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

fig.suptitle("Parámetros de Deformación a lo largo de perfiles GPS", fontsize=12)
fig.tight_layout(rect=[0, 0, 1, 0.96])

handles, labels = axs[0, 0].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
fig.legend(by_label.values(), by_label.keys(), loc='upper center', bbox_to_anchor=(0.5, 1.02), 
           fancybox=True, shadow=True, ncol=3)

plt.show()
