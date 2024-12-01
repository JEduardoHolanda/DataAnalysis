import requests
import geopandas as gpd

def request_query(url, params):
    """
    Função para fazer a request GET de uma API.
    Inputs: params:
        - f: formato da resposta. Neste estudo, o formato json foi utilizado;
        - where : filtro da consulta. Basicamente, seria um filtro para restringir os dados que serão retornados. **'1=1'** indica para retornar todos os registros;
        - outFields : campos de saída. Define quais campos serão retornados. **'*'** indica que as saídas de coluna além da coluna de geometria.
        - geometry : define a geometria espacial para a consulta.
    Output: dados a serem retornados (json, GeoJSON, HTML) de acordo com a escolha do parâmetro de entrada "f".
    """
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            data = response.json()  # Converter para JSON
            return data
        except ValueError:  # JSON inválido
            print("Resposta não é um JSON válido.")
            return None
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

def json_to_gdf(json_data):
    """
    Função para criar um GeoDataFrame a partir de dados em formato JSON.
    Inputs: json_data: dados obtidos no formato JSON
    Output: GeoDataFrame junto com a longitude e a latitude concatenadas ao final do dataset.
    """
    
    long = [feature['geometry']['x'] for feature in json_data['features']]
    lat = [feature['geometry']['y'] for feature in json_data['features']]
    gdf_coordinates = gpd.GeoDataFrame(
        {'Longitude': long, 'Latitude': lat},
        geometry=gpd.points_from_xy(long,lat),
        crs="EPSG:4326"
    )
    
    features = json_data['features']
    attributes = [feature['attributes'] for feature in features]
    gdf = gpd.GeoDataFrame(
        attributes,
        geometry=gpd.points_from_xy(
            long,
            lat
        ),
        crs="EPSG:4326"
    )
    gdf['LONG'] = long
    gdf['LAT'] = lat

    return gdf